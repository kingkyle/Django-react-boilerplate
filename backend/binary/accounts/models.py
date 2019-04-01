from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

from .utils import account_ID


class AccountsManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None):
        if not email:
            raise ValueError('Please Provide a valid email address')
        if email and self.model.objects.filter(email__iexact=email).exists():
            raise ValueError("Email Address is Already in Use")
        if not first_name:
            raise ValueError('Please Enter a legal first name')
        if not last_name:
            raise ValueError('Please Enter a legal last name')
        accountId = account_ID()
        while self.model.objects.filter(accountId=accountId).exists():
            accountId = account_ID()
        user = self.model(
            email=self.normalize_email(email).lower(),
            first_name=first_name,
            last_name=last_name,
            accountId=accountId
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_admin(self, email, password=None):
        if not email:
            raise ValueError('Please enter Email')
        accountId = account_ID()
        while Accounts.objects.filter(accountId=accountId).exists():
            accountId = account_ID()

        user = self.model(email=self.normalize_email(
            email).lower(), accountId=accountId)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        if not email:
            raise ValueError('Please Enter Email')
        if email and self.model.objects.filter(email__iexact=email).exists():
            raise ValueError("Email Address is Already in Use")
        accountId = account_ID()
        while Accounts.objects.filter(accountId=accountId).exists():
            accountId = account_ID()
        user = self.model(
            email=self.normalize_email(email),
            is_superuser=True,
            is_active=True,
            is_staff=True,
            accountId=accountId
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class Accounts(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    email = models.EmailField(max_length=225, unique=True)
    accountId = models.CharField(max_length=225, unique=True)
    join_ip = models.GenericIPAddressField(default='127.0.0.1')
    is_active = models.BooleanField(default=True, help_text=_(
        '''Designates whether this user should be
                                         treated as active.'''
        'Unselect this instead of deleting accounts.'))
    is_staff = models.BooleanField(default=False, help_text=_(
        'Designates whether the user can log into this admin site.'))

    objects = AccountsManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.accountId

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name

    class Meta:
        verbose_name = _('account')
        verbose_name_plural = _('accounts')
