# core/forms.py
import re
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Order

FULLNAME_RE = re.compile(r"^[А-Яа-яЁё ]+$")
PHONE_RE = re.compile(r"^\+7\(\d{3}\)-\d{3}-\d{2}-\d{2}$")

class RegisterForm(forms.Form):
    username = forms.CharField(label="Логин", min_length=3, max_length=150,
        widget=forms.TextInput(attrs={"class":"input", "placeholder":"Придумайте логин"}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class":"input", "placeholder":"Минимум 8 символов"}), min_length=8)
    full_name = forms.CharField(label="ФИО", max_length=150,
        widget=forms.TextInput(attrs={"class":"input", "placeholder":"Иванов Иван Иванович"}))
    phone = forms.CharField(label="Телефон", max_length=20,
        widget=forms.TextInput(attrs={"class":"input", "placeholder":"+7(999)-123-45-67"}))
    email = forms.EmailField(label="Email", max_length=254,
        widget=forms.EmailInput(attrs={"class":"input", "placeholder":"name@example.ru"}))


    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise ValidationError("Логин уже занят.")
        return username

    def clean_full_name(self):
        full_name = self.cleaned_data["full_name"].strip()
        if not FULLNAME_RE.match(full_name):
            raise ValidationError("ФИО: только кириллица и пробелы.")
        return full_name

    def clean_phone(self):
        phone = self.cleaned_data["phone"].strip()
        if not PHONE_RE.match(phone):
            raise ValidationError("Телефон в формате +7(XXX)-XXX-XX-XX.")
        return phone

class LoginForm(forms.Form):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={"class":"input"}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class":"input"}))
    
class OrderForm(forms.ModelForm):
    desired_datetime = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local", "class": "input"}),
        input_formats=["%Y-%m-%dT%H:%M"]
    )

    class Meta:
        model = Order
        fields = ["address","contact_phone","contact_email","desired_datetime","service","payment_type","other_service","other_service_text"]
        widgets = {
            "address": forms.TextInput(attrs={"class": "input", "placeholder": "Например: ул. Ленина, 10, кв. 5"}),
            "contact_phone": forms.TextInput(attrs={"class": "input", "placeholder": "+7(999)-123-45-67"}),
            "contact_email": forms.EmailInput(attrs={"class": "input", "placeholder": "name@example.ru"}),
            "service": forms.Select(attrs={"class": "input"}),
            "payment_type": forms.Select(attrs={"class": "input"}),
            "other_service_text": forms.TextInput(attrs={"class": "input", "placeholder": "Опишите услугу"}),
        }
    def clean_contact_phone(self):
        phone = self.cleaned_data["contact_phone"].strip()
        if not PHONE_RE.match(phone):
            raise ValidationError("Телефон в формате +7(XXX)-XXX-XX-XX.")
        return phone

    def clean(self):
        cleaned = super().clean()
        other = cleaned.get("other_service")
        text = (cleaned.get("other_service_text") or "").strip()
        if other and not text:
            self.add_error("other_service_text", "Опишите, какая услуга требуется.")
        if not other:
            cleaned["other_service_text"] = ""
        return cleaned