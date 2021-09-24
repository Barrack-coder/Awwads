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
  
]