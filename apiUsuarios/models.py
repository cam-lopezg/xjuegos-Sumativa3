from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class TipoUsuario(models.Model):
    tipo = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.tipo

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser debe tener is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    nombre = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50, unique=True)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)
    fecha_nacimiento = models.DateField()  # Campo obligatorio de fecha de nacimiento
    direccion = models.CharField(max_length=255, null=True, blank=True)  # Campo opcional de dirección

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname', 'nombre', 'fecha_nacimiento']  # Incluir fecha_nacimiento en campos requeridos para superusuarios

    def __str__(self):
        return self.nickname