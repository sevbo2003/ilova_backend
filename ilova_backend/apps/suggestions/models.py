from django.db import models
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()


class ProblemType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Status(models.TextChoices):
    SOLVED = "Muvaffaqiyatli"
    PENDING = "Kutilmoqda"
    FAKE = "Yolg'on"


class Problem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="problems")
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    images = models.FileField(upload_to="%Y/%m/%d/")
    date = models.DateTimeField(auto_now_add=True)
    problem_types = models.ManyToManyField(ProblemType, related_name="problems")
    description = models.CharField(max_length=1000)
    status = models.CharField(max_length=100, choices=Status.choices, default=Status.PENDING)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
