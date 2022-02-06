from django.urls import path
from . import views

urlpatterns=[
   path('',views.index,name = 'index'),
   path('profile/', views.profile, name='profile'),
   path('update_profile/<int:id>', views.update_profile, name='update_profile'),
   path('add_post/', views.add_post, name='add_post'),
   path('comments/<post_id>', views.comments, name='comments'),
   
]