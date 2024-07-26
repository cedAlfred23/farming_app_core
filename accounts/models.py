from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .manager import UserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, verbose_name=_('email address'))
    first_name = models.CharField(max_length=30, blank=True, verbose_name=_('first name'))
    last_name = models.CharField(max_length=30, blank=True, verbose_name=_('last name'))
    phone_number = models.CharField(max_length=15, blank=True, verbose_name=_('phone number'))
    is_staff = models.BooleanField(default=False, help_text=_('Designates whether the user can log into this admin site.'))
    is_verified = models.BooleanField(default=False, help_text=_('Designates whether the user has verified their email.'))
    is_superuser = models.BooleanField(default=False, help_text=_('Designates whether the user is a staff.'))
    is_farmer = models.BooleanField(default=False, help_text=_('Designates whether the user is a farmer.'))
    is_active = models.BooleanField(default=True, help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["first_name", "last_name", "phone_number"]

    objects = UserManager()

    def __str__(self):
        return self.email
    
    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def tokens(self):
        pass
        # refresh = RefreshToken.for_user(self)
        # return {
        #     'refresh': str(refresh),
        #     'access': str(refresh.access_token)
        # }

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


class OneTimePassword(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    code=models.CharField(max_length=6, unique=True)

    def __str__(self):
        return f'{self.user.first_name}-passcode'