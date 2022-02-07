from django.urls import path
from . import views

urlpatterns=[
   path('',views.index,name = 'index'),
   path('profile/', views.profile, name='profile'),
   path('update_profile/<int:id>', views.update_profile, name='update_profile'),
   path('add_post/<int:id>', views.add_post, name='add_post'),
   path('comments/<post_id>', views.comments, name='comments'),
   path('search/', views.search, name='search'),
   # path('like/<int:id>', views.like_post, name='like_post'),
   # path('follow/<user_id>', views.follow, name='follow'),
   path('like/<id>', views.like, name='like'),
   path('unlike/<id>', views.unlike, name='unlike'),

  
]