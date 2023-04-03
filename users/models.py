from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,BaseUserManager,PermissionsMixin
class UserManager(BaseUserManager):
    def create_user(self, phone, password=None,is_active=True):
        if not phone:
            raise ValueError('Users must have an phone')
        user = self.model(
            phone=phone,
            is_active = is_active
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_staffuser(self, phone, password,is_active=True,is_staff=True):
        user = self.create_user(
            phone,
            password=password,

            is_active = is_active
        )
        user.save(using=self._db)
        user.is_staff = is_staff
        return user
    def create_superuser(self,phone, password,is_active=True,is_staff=True,is_superuser=True):
        user = self.create_user(
            phone,
            password=password,
            is_active=is_active
        )
        user.is_superuser =is_superuser
        user.is_staff = is_staff
        user.save(using=self._db)
        return user
class User(AbstractBaseUser,PermissionsMixin):
    class Role(models.TextChoices):
        MANAGER = 'manager','Manager'
        DIRECTOR = 'director','Director'
        TEACHER  = 'teacher','Teacher'
    phone = models.CharField(
        verbose_name='Phone Number',
        max_length=15,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # a admin user; non super-user
    is_superuser = models.BooleanField(default=False)  # a superuser
    fullname = models.CharField(max_length=100,null=True,blank=True)
    role = models.CharField(max_length=150,choices=Role.choices,null=True,blank=True)
    # notice the absence of a "Password field", that is built in.
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []  # UsernameField(phone) & Password are required by default.
    def get_full_name(self):
        # The user is identified by their email address
        return self.fullname
    def __str__(self):
        return self.phone
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    objects = UserManager()
    ################# Director ########################
class DirectorManager(BaseUserManager):
    def create_user(self, phone, password=None,is_active=True,fullname=None):
        if not phone or len(phone) <= 0:
            raise ValueError("Phone field is required !")
        if not password:
            raise ValueError("Password is must !")
        user = self.model(
            phone = phone,
            is_active =is_active
        )
        user.fullname = fullname
        user.set_password(password)
        user.save(using=self._db)
        return user
    def get_queryset(self, *args, **kwargs):
        result = super().get_queryset(*args, **kwargs)
        return result.filter(role=User.Role.DIRECTOR)
class Director(User):
    base_role = User.Role.DIRECTOR
    def save(self, *args, **kwargs):
        self.role = self.base_role
        return super().save(*args, **kwargs)
    class Meta:
        proxy = True
    objects = DirectorManager()
    ################# Manager ########################
class ManagerManager(BaseUserManager):
    def create_user(self, phone, password=None,is_active=True,fullname=None):
        if not phone or len(phone) <= 0:
            raise ValueError("Phone field is required !")
        if not password:
            raise ValueError("Password is must !")

        user = self.model(
            phone = phone,
            is_active =is_active
        )
        user.fullname = fullname
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_queryset(self, *args, **kwargs):
        result = super().get_queryset(*args, **kwargs)
        return result.filter(role=User.Role.MANAGER)
class Manager(User):
    base_role = User.Role.MANAGER
    def save(self, *args, **kwargs):
        self.role = self.base_role
        return super().save(*args, **kwargs)
    class Meta:
        proxy = True
    objects = ManagerManager()
    ################# Teacher ########################
class TeacherManager(BaseUserManager):
    def create_user(self, phone, password=None,is_active=True):
        if not phone or len(phone) <= 0:
            raise ValueError("Phone field is required !")
        if not password:
            raise ValueError("Password is must !")
        user = self.model(
            phone = phone,
            is_active =is_active
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def get_queryset(self, *args, **kwargs):
        result = super().get_queryset(*args, **kwargs)
        return result.filter(role=User.Role.MANAGER)
class Teacher(User):
    base_role = User.Role.TEACHER
    def save(self, *args, **kwargs):
        self.role = self.base_role
        return super().save(*args, **kwargs)
    class Meta:
        proxy = True
    objects = TeacherManager()
