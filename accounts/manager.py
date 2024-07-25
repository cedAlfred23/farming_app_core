from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_('Please enter a valid email address'))
        
    def create_user(self, email, first_name, last_name, phone_number, password, **extra_fields):
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:    
            raise ValueError(_('The Email field must be set'))
        
        if not first_name:
            raise ValueError(_('The First Name field must be set'))
        
        if not last_name:
            raise ValueError(_('The Last Name field must be set'))
        
        user = self.model(email=email, first_name=first_name, last_name=last_name, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, first_name, last_name, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_verified', True)
        extra_fields.setdefault('is_superuser', True)
        
        # if extra_fields.get('is_admin') is not True:
        #     raise ValueError(_('Superuser must have is_admin=True.'))
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        
        user = self.create_user(email, first_name, last_name, phone_number, password, **extra_fields)
        user.save(using=self._db)
        return user