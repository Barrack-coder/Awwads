from django.http import request
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.conf import settings
from django.conf.urls.static import static
from django.urls.resolvers import URLPattern
from django.core.exceptions import ObjectDoesNotExist
from .models import categories,Award,Profile,Rating


# Create your views here.


def index(request):
	return render(request,'index.html',)


def dir(request):
    return render(request,'dir.html',)


@login_required(login_url='/wards/login/')
def create_profile(request):
    return render(request,'create_profile.html',)



@login_required(login_url='/wards/login/')
def profile(request):
    return render(request,'profile.html',)



@login_required(login_url='/wards/login/')
def new_award(request):
    return render(request,'new_award.html',)

def search_results(request):
        return render(request,'search.html',)
    
    
@login_required(login_url='/wards/login/')    
def sitee(request,sitee_id):
    current_user = request.user
    profile =Profile.objects.get(username=current_user)

    try:
        award = Award.objects.get(id=sitee_id)
    except:
        raise ObjectDoesNotExist()

    try:
        ratings = Rating.objects.filter(award_id=sitee_id)
        design = Rating.objects.filter(award_id=sitee_id).values_list('design',flat=True)
        usability = Rating.objects.filter(award_id=sitee_id).values_list('usability',flat=True)
        creativity = Rating.objects.filter(award_id=sitee_id).values_list('creativity',flat=True)
        content = Rating.objects.filter(awrd_id=sitee_id).values_list('content',flat=True)
        total_design=0
        total_usability=0
        total_creativity=0
        total_content = 0
        print(design)
        for rate in design:
            total_design+=rate
        print(total_design)

        for rate in usability:
            total_usability+=rate
        print(total_usability)

        for rate in creativity:
            total_creativity+=rate
        print(total_creativity)

        for rate in content:
            total_content+=rate
        print(total_content)

        overall_score=(total_design+total_content+total_usability+total_creativity)/4

        print(overall_score)

        award.design = total_design
        award.usability = total_usability
        award.creativity = total_creativity
        award.content = total_content
        award.overall_score = overall_score

        award.save()

    except:
        return None
    
def user_profile(request,username):
    return render(request,'user-profile.html',)










# if settings.DEBUG:
#     URLPattern += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)