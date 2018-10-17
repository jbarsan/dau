from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser)
from django.utils.translation import gettext_lazy as _


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, matricula, nome, sobrenome, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not matricula:
            raise ValueError('Usuário precisa ter uma matrícula válida')

        user = self.model(
            matricula=matricula,
            nome=nome,
            sobrenome=sobrenome
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, matricula, nome, sobrenome, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            matricula,
            password=password,
            nome=nome,
            sobrenome=sobrenome
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    matricula = models.CharField(_('Matrícula'), max_length=6, primary_key=True)
    nome = models.CharField(_('Nome'), max_length=50)
    sobrenome = models.CharField(_('Sobrenome'), max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(_('Administrador'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'matricula'
    REQUIRED_FIELDS = ('nome', 'sobrenome',)

    class Meta:
        db_table = 'Usuario'
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return '{} {}'.format(self.matricula, self.nome)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
