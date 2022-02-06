from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    profile_photo=CloudinaryField('image')
    name=models.TextField(max_length=50)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField(null=True, max_length=1000)
    email=models.CharField(null=True, max_length=50)
    phone_number=models.IntegerField(max_length=20)

    @receiver(post_save , sender = User)
    def create_profile(instance,sender,created,**kwargs):
      if created:
        Profile.objects.create(user = instance)

    @receiver(post_save,sender = User)
    def save_profile(sender,instance,**kwargs):
      instance.profile.save()

class Post(models.Model):
    image = CloudinaryField('image')
    photo_name = models.CharField(max_length=60)
    posted_at = models.DateTimeField(auto_now_add=True)
    photo_caption = models.TextField()
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    liked= models.ManyToManyField(User,default=None,blank=True,related_name='liked')

    def save_post(self):
        self.save()


    @classmethod
    def display_photos(cls):
      photos = cls.objects.all().order_by('-posted_at')
      return photos
    
    
    @property
    def saved_likes(self):
      return self.photolikes.count()
    
    @classmethod
    def search_by_photo_name(cls,search_term):
        instaapp = cls.objects.filter(photo_name__icontains=search_term)
        return instaapp
    
    def delete_post(self):
      self.delete()

    @property
    def saved_comments(self):
        return self.comments.all()
    
    def _str_(self):
     return "%s photo" % self.photo_name      









