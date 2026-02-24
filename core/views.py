# core/views.py
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404

from .forms import RegisterForm, LoginForm, OrderForm
from .models import Profile, Order, OrderStatus

def home_view(request):
    return render(request, "home.html")

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
                email=form.cleaned_data["email"],
            )
            Profile.objects.create(
                user=user,
                full_name=form.cleaned_data["full_name"],
                phone=form.cleaned_data["phone"],
            )
            messages.success(request, "Регистрация успешна. Войдите в систему.")
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "auth/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data["username"]
            p = form.cleaned_data["password"]
            user = authenticate(request, username=u, password=p)
            if user is None:
                messages.error(request, "Неверный логин или пароль.")
            else:
                login(request, user)
                return redirect("cabinet")
    else:
        form = LoginForm()
    return render(request, "auth/login.html", {"form": form})

@login_required
def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def cabinet_view(request):
    orders = Order.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "cabinet.html", {"orders": orders})

@login_required
def create_order_view(request):
    # статус "новая заявка"
    new_status = get_object_or_404(OrderStatus, name="новая заявка")

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.status = new_status
            order.save()
            messages.success(request, "Заявка создана.")
            return redirect("cabinet")
    else:
        # можно автозаполнить контакты из профиля
        initial = {}
        try:
            prof = request.user.profile
            initial["contact_phone"] = prof.phone
            initial["contact_email"] = request.user.email
        except Exception:
            pass
        form = OrderForm(initial=initial)

    return render(request, "order_create.html", {"form": form})