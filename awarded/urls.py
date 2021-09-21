from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
      url(r'^$',views.index,name='Index'),
      url(r'^dir/',views.dir, name='dir'),
      url(r'^create/profile$',views.create_profile, name='create-profile'),
    
  
]