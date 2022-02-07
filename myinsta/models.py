from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
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
    def display_posts(cls):
      posts = cls.objects.all().order_by('-posted_at')
      return posts
    
    
    @property
    def saved_likes(self):
      return self.postlikes.count()
    
    @classmethod
    def search_by_photo_name(cls,search_term):
        instaapp = cls.objects.filter(photo_name__icontains=search_term)
        return instaapp
    
    def delete_post(self):
      self.delete()

    @property
    def saved_comments(self):
        return self.comments.all()

    @classmethod
    def search_by_username(cls,search_term):
        myinsta = cls.objects.filter(username__icontains=search_term)
        return myinsta    
    
    def __str__(self):
     return "%s photo" % self.photo_name 

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    def str(self):
        return self.value 

class Profile(models.Model):
    profile_photo=CloudinaryField('image')
    name=models.TextField(max_length=50)
    user=models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    bio=models.TextField(null=True, max_length=1000)
    email=models.CharField(null=True, max_length=50)
    phone_number=models.IntegerField(null=True)
    likes = models.ForeignKey(Like, on_delete=models.SET_NULL, null=True, related_name='likes', blank=True)

    @receiver(post_save , sender = User)
    def create_profile(instance,sender,created,**kwargs):
      if created:
        Profile.objects.create(user = instance)

    @receiver(post_save,sender = User)
    def save_profile(sender,instance,**kwargs):
      instance.profile.save()

      def __str__(self):
        return f'{self.user.username} profile'


     

class Comment(models.Model):
    comment = models.CharField(max_length=250,null=True)
    post = models.ForeignKey(Post,on_delete = models.CASCADE,related_name='comments',null=True)
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name='comments',null=True)

    @classmethod
    def display_comment(cls,post_id):
        comments = cls.objects.filter(post_id = post_id)
        return comments   

# LIKE_CHOICES={
#     ('Like','Like'),
#     ('Unlike','Unlike',)
# }
# class Like(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
#     value = models.CharField(choices=LIKE_CHOICES,default='like',max_length=10)

#     def str(self):
#         return self.value 

# class Follow(models.Model):
#     follower=models.ForeignKey(User,related_name='followers',on_delete=models.CASCADE)
#     followed=models.ForeignKey(User,related_name='followed',on_delete=models.CASCADE)

#     def __str__(self):
#         return self.follower        










