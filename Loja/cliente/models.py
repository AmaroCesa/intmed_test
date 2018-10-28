from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class Cliente(AbstractUser):
    """
        Clinte para login de usuário.
    """
    telefone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    telefone = models.CharField(validators=[telefone_regex], max_length=17, blank=True, null=True) 

