from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
import datetime as dt

from django.db.models.deletion import CASCADE




# Create your models here.

class photos(models.Model):
    # title field
    title = models.CharField(max_length=100)
    #image field
    image = CloudinaryField('image')
    
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError(" User must have an email address")
        if not username:
            raise ValueError(" User must have an username!")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password = password,
            username=username,
        )
        user.email = email
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
class Users(AbstractBaseUser):
    username = models.CharField( max_length=80, unique=True)
    email = models.CharField( max_length=100, unique=True)
    phone_number = models.CharField(max_length = 15,blank =True)
    profile_photo = CloudinaryField('image', default='image/upload/v1632754417/24-248253_user-profile-default-image-png-clipart-png-download_obstgc.png')
    bio= models.TextField(null=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(default=dt.datetime.now)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    password_reset = models.CharField( max_length=50, default="e5viu3snjorndvd")
    password = models.CharField( max_length=100)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'username']
 
    objects=MyAccountManager()
    
class categories(models.Model):
    categories= models.CharField(max_length=100)

    def __str__(self):
        return self.categories

    def save_category(self):
        self.save()

    @classmethod
    def delete_category(cls,categories):
        cls.objects.filter(categories=categories).delete()
        
class Award(models.Model):
    title = models.TextField()
    image = CloudinaryField('image',default='x.png')
    description = models.CharField(max_length=150,null=True)
    user = models.ForeignKey('Users', on_delete=models.CASCADE,null=True,default=1)
 
    def __str__(self):
        return self.title
    
    
class Profile(models.Model):
    avatar = models.ImageField(upload_to='avatars/')
   

    def __str__(self):
        return self
class Rating(models.Model):
    design = models.IntegerField(blank=True,default=0)
    usability = models.IntegerField(blank=True,default=0)
    creativity = models.IntegerField(blank=True,default=0)
    content = models.IntegerField(blank=True,default=0)
    overall_score = models.IntegerField(blank=True,default=0)
    project = models.ForeignKey(Award,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    
   
    
