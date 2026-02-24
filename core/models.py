# core/models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField("ФИО", max_length=150)
    phone = models.CharField("Телефон", max_length=20)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return self.full_name

class Service(models.Model):
    name = models.CharField("Название услуги", max_length=120, unique=True)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.name


class OrderStatus(models.Model):
    name = models.CharField("Название статуса", max_length=30, unique=True)

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

    def __str__(self):
        return self.name

class Order(models.Model):
    PAYMENT_CHOICES = [
        ("cash", "Наличные"),
        ("card", "Банковская карта"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    service = models.ForeignKey(Service, on_delete=models.PROTECT, verbose_name="Услуга")
    status = models.ForeignKey(OrderStatus, on_delete=models.PROTECT, verbose_name="Статус")

    address = models.CharField("Адрес", max_length=255)
    contact_phone = models.CharField("Контактный телефон", max_length=20)
    contact_email = models.EmailField("Email")
    desired_datetime = models.DateTimeField("Дата и время оказания услуги")
    payment_type = models.CharField("Тип оплаты", max_length=10, choices=PAYMENT_CHOICES)

    other_service = models.BooleanField("Иная услуга", default=False)
    other_service_text = models.CharField("Описание иной услуги", max_length=255, blank=True)

    cancel_reason = models.CharField("Причина отмены", max_length=255, blank=True)

    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        

    

    def __str__(self):
        return f"Заявка №{self.id}"