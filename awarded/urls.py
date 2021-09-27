from django.conf.urls import url,include
from django.urls.conf import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
      url(r'^$',views.index,name='Index'),
      url(r'^dir/',views.dir, name='dir'),
      url(r'^create/profile$',views.create_profile, name='create-profile'),
      url(r'^profile/',views.profile, name='profile'),
      path('new_award',views.new_award, name='new-award'),
      url(r'^search/',views.search_results, name='search_results'),
      path('sitee',views.sitee,name='sitee'),
      url(r'^user/(?P<username>\w{0,50})',views.user_profile,name='user-profile'),
      path('register',views.register,name='register'),
      path('user_login',views.user_login,name='user_login'),
      path('logout',views.logout,name='logout'),
  
]