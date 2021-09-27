from django.http import request
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.conf import settings
from django.conf.urls.static import static
from django.urls.resolvers import URLPattern
from django.core.exceptions import ObjectDoesNotExist
from .models import Users, categories,Award,Profile,Rating
from django.contrib.auth.hashers import make_password

from django.contrib import messages
from django.contrib.auth import authenticate,login as signin,logout as signout
from django.contrib.auth.decorators import login_required



# Create your views here.


def index(request):
    award=Award.objects.all()
    return render(request,'index.html',{'awards':award})


def dir(request):
    return render(request,'dir.html',)



def create_profile(request):
    return render(request,'create_profile.html',)




def profile(request):
    return render(request,'profile.html',)



@login_required(login_url='/user_login')
def new_award(request):
    if request.method=="POST":
        title=request.POST.get('title')
        description=request.POST.get('description')
        image=request.FILES.get('image')  
        award = Award(title=title, description=description,image=image,user=request.user)
        award.save()
        messages.add_message(request, messages.SUCCESS, 'Uploaded successfully!')       
        return redirect(new_award)
    else:
        
        return render(request,'new_award.html',)

def search_results(request):
        return render(request,'search.html',)
    
    
   
def sitee(request):
    current_user = request.user
    profile =Profile.objects.get(user=current_user)
    sitee_id =1


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
        return redirect("index")

    except:
        return None
    
def user_profile(request,username):
    return render(request,'user-profile.html',)



def register(request):
    if request.method=="POST":
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        e_username=Users.objects.filter(username=username).count()
        email_exist=Users.objects.filter(email=email).count()
        if e_username>0:
            messages.add_message(request, messages.ERROR, 'Username exist')
            return redirect(register)
        elif email_exist>0:
            messages.add_message(request, messages.ERROR, 'Email exist')
            return redirect(register)
        else:
            if password!=confirm_password:
                messages.add_message(request, messages.ERROR, 'Username exist')
                return redirect(register)
            else:
                user = Users(username=username, email=email,phone_number=phone,password=make_password(password))
                user.save()
                messages.add_message(request, messages.SUCCESS, 'Saved successfully!')
                return redirect(user_login)
    else:
        return render(request, "wards/register.html")
    
    

def user_login(request):
     if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        user= authenticate(email=email, password=password)
        if user is not None:
            signin(request,user )
            return redirect(index)
        else:
            messages.add_message(request, messages.ERROR, 'Invalid Credentials!')
            return redirect(user_login)
     else:
        return render(request, "wards/login.html")

def logout(request):
    signout(request)
    messages.add_message(request, messages.SUCCESS, 'Logout successfully!')
    return redirect(user_login)










# if settings.DEBUG:
#     URLPattern += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)