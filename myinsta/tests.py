from django.test import TestCase

from myinsta.models import Post, Like, Profile,User

class ImageTestCase(TestCase):
    def setUp(self):
        # create a user
        user = User.objects.create(
            username='test_user',
           
        )
        Post.objects.create(
            photo_name='test_image',
            image='https://upload.wikimedia.org/wikipedia/commons/4/49/Flag_of_Kenya.svg',
            photo_caption='test image',
            
            user_id=user.id
        )

    def test_image_name(self):
        image = Post.objects.get(photo_name='test_image')
        self.assertEqual(image.photo_name, 'test_image')

    def test_image_id(self):
        user = User.objects.create(
            username='newuser',
            
        )
        photo = Post.objects.create(
            photo_caption='test post',
            image='https://upload.wikimedia.org/wikipedia/commons/4/49/Flag_of_Kenya.svg',
            
            user_id=user.id
        )

    def test_image_posted_at(self):
        user = User.objects.create(
            username='newuser',
            
        )
        photo = Post.objects.create(
            photo_caption='test post',
            image='https://upload.wikimedia.org/wikipedia/commons/4/49/Flag_of_Kenya.svg',
            
            user_id=user.id
        )

    def test_image_user(self):
        user = User.objects.create(
            username='newuser',
            
        )
        photo = Post.objects.create(
            photo_caption='test post',
            image='https://upload.wikimedia.org/wikipedia/commons/4/49/Flag_of_Kenya.svg',
            
            user_id=user.id
        )
    def test_image_photo_caption(self):
        user = User.objects.create(
            username='newuser',
            
        )
        photo = Post.objects.create(
            photo_caption='test post',
            image='https://upload.wikimedia.org/wikipedia/commons/4/49/Flag_of_Kenya.svg',
            
            user_id=user.id
        )
    def test_image_liked(self):
        user = User.objects.create(
            username='newuser',
            
        )
        photo = Post.objects.create(
            photo_caption='test post',
            image='https://upload.wikimedia.org/wikipedia/commons/4/49/Flag_of_Kenya.svg',
            
            user_id=user.id
        )