import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class PollManager(models.Manager):
    pass

class Poll(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(max_length=50)
    sdate = models.DateField()
    edate = models.DateField()
    archived = models.BooleanField(default=False)
    tvotes = models.BigIntegerField(default=0, editable=False)
    objects = PollManager()

    
    def __str__(self):
        return 'Poll Category - %s'% self.category

    def __repr__(self):
        return 'Poll Category - %s\nTotal Votes - %d'\
        % (self.category, self.tvotes)

class Candidate(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    votes = models.BigIntegerField(default=0, editable=False)
    img_link = models.URLField(max_length=500, blank=True, default=None)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def __str__(self):
        return 'Candidate Name - %s %s' % (self.fname, self.lname)

    def __repr__(self):
        return 'Candidate Name - %s %s\nCurrent Votes - %d'\
        % (self.fname, self.lname, self.votes)


class UserManager(BaseUserManager):
    
    def create_user(self, email, first_name=None, last_name=None, 
        is_organizer=False, password=None, is_admin=False, 
        is_active=False, is_staff=False, **kwargs):
        if not email:
            raise ValueError('Email is required.')
        if not password:
            raise ValueError('Password is required.')
        if not first_name:
            raise ValueError('Firstname is required.')
        if not last_name:
            raise ValueError('Lastname is required.')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.is_organizer = is_organizer
        user.is_superuser = user.admin = is_admin
        user.active = is_active
        user.staff = is_staff
        user.save(using=self._db)
        return user

    def create_staff_user(self, email, first_name, last_name, password=None):
        user = self.create_user(
            email, 
            first_name=first_name,
            last_name=last_name,
            password=password,
            is_staff=True,
            is_active=True
            )
        return user



    def create_superuser(self, email,first_name, last_name,password=None, **kwargs):
        user = self.create_user(
            email, 
            first_name=first_name,
            last_name=last_name,
            password=password,
            is_staff=True,
            is_active=True,
            is_admin=True
            )
        return user

class User(AbstractUser):
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_organizer = models.BooleanField(default=False, blank=True)
    email = models.EmailField(max_length=100, unique=True, blank=False)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) 
    admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = UserManager() 

    @property
    def is_staff(self):
         # "Is the user a member of staff?"
         return self.staff

    @property
    def is_admin(self):
         # "Is the user a admin member?"
         return self.admin

    @property
    def is_active(self):
         # "Is the user active?"
         return self.active

class VoteLogs(models.Model):
    poll_id = models.UUIDField(default=uuid.uuid4, editable=False)
    user_id = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return 'Poll id - %s\nUser id - %s' % (self.poll_id, self.user_id)