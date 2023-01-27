from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MinValueValidator, MaxValueValidator


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None, **kwargs):
        if username is None:
            raise TypeError('Users must have an username.')
        if email is None:
            raise TypeError('Users must have an email.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')
        if email is None:
            raise TypeError('Superusers must have an email.')
        if username is None:
            raise TypeError('Superusers must have an username.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(
        db_index=True, unique=True,  null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"


class Game(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    name = models.CharField(max_length=16)
    pseudo = models.CharField(max_length=16)
    position = models.CharField(max_length=30, default='start')
    gold = models.IntegerField(validators=[MinValueValidator(1)], default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user_id} - {self.name}"


class Team(models.Model):
    game_id = models.ForeignKey(
        'Game', related_name='team', on_delete=models.CASCADE)
    model_id = models.IntegerField(null=True, blank=True)
    order = models.IntegerField(validators=[MinValueValidator(1),
                                            MaxValueValidator(6)])
    lvl = models.IntegerField(validators=[MinValueValidator(0),
                                          MaxValueValidator(100)], null=True, blank=True)
    pv = models.IntegerField(null=True, blank=True)
    mana = models.IntegerField(null=True, blank=True)
    exp = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.game_id} - {self.order}"


class PetStore(models.Model):
    game_id = models.ForeignKey(
        'Game', related_name='petStore', on_delete=models.CASCADE)
    model_id = models.IntegerField(null=True, blank=True)
    order = models.IntegerField(validators=[MinValueValidator(1),
                                            MaxValueValidator(30)])
    lvl = models.IntegerField(validators=[MinValueValidator(0),
                                          MaxValueValidator(100)], null=True, blank=True)
    pv = models.IntegerField(null=True, blank=True)
    mana = models.IntegerField(null=True, blank=True)
    exp = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.game_id} - {self.order}"


class Bag(models.Model):
    game_id = models.ForeignKey(
        'Game', related_name='bag', on_delete=models.CASCADE)
    model_id = models.IntegerField(null=True, blank=True)
    order = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(4)])
    amount = models.IntegerField(validators=[MinValueValidator(0),
                                             MaxValueValidator(99)], null=True, blank=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.game_id} - {self.order}"


class PDF(models.Model):
    name = models.CharField(max_length=50)
    pdf = models.FileField(upload_to='pdf')

    def __str__(self):
        return f"{self.name}"
