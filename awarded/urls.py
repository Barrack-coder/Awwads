from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
      url(r'^$',views.index,name='Index'),
      url(r'^dir/',views.dir, name='dir'),
      url(r'^create/profile$',views.create_profile, name='create-profile'),
      url(r'^profile/',views.profile, name='profile'),
      url(r'^new/award$',views.new_award, name='new-award'),
      url(r'^search/',views.search_results, name='search_results'),
      url(r'^sitee/(\d+)',views.sitee,name='sitee'),
      url(r'^user/(?P<username>\w{0,50})',views.user_profile,name='user-profile'),
      # url(r'^register/$',views.register,name='register'),
      # url(r'^user_login/$',views.user_login,name='user_login'),
  
]