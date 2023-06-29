from django.shortcuts import redirect, render
from django.contrib import messages 
from django.contrib import auth 
from django.contrib.auth import authenticate , login ,logout

from main.models import Moderator, User, Worker



# Create your views here.
def my_view(request):

    return render(request,"index.html")




def user_home(request):
    username = request.session.get('username')
    context = {'username':username}                            

    return render(request,"userhome.html",context)

def worker_home(request):
    
    return render(request,"worker_home.html")

def admin_home(request):

    return render(request,"admin_home.html")



def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'admin' and password == 'admin':
            print("Login successful")
            return redirect('/admin_home')
               
        user = auth.authenticate(request, username = username,password = password)
        
        print (user)
        if user is None:
            messages.error(request , 'invalid password')
            return redirect('/login_view')
        else:
            if isinstance(user, Moderator):
                login(request, user)
                return redirect('moderator_home')
            elif isinstance(user, User):
                login(request, user)
                return redirect('user_home')
            elif isinstance(user, Worker):
                login(request, user)
                return redirect('worker_home')
    return render(request,"login.html")

  

def logout_view(request):
    logout(request)
    return redirect('/login_view')




def user_reg(request):
    if request.method != "POST":
        return render(request,'userreg.html')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    password = request.POST.get('password')
    dob =request.POST.get('dob')
    address = request.POST.get('address')
    phoneno = request.POST.get('phoneno')
    user_bio =request.POST.get('user_bio')  
    email=request.POST.get('email')
    user_image=request.FILES.get('user_image')
    location=request.POST.get('location')
    _type=request.POST.get('type')

    user=User.objects.filter(username = username)
    if user.exists():
        messages.info(request,'username already exists ')
        return redirect('/user_reg')

    user = User.objects.create(
       first_name = first_name,
       last_name = last_name,
       username = username,
       address =address,
       dob =dob,
       phone_no = phoneno,
       user_bio = user_bio,
       location = location,
       email = email,
       user_image = user_image,
       type = _type

    )
    user.set_password(password)
    user.save()
    messages.info(request,'registered sucessfully')
    return redirect('/user_reg')

    


def worker_reg(request):
    if request.method != "POST":
       return render(request,'workerreg.html')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    password = request.POST.get('password')
    dob =request.POST.get('dob')
    address = request.POST.get('address')
    phoneno = request.POST.get('phoneno')
    user_bio =request.POST.get('user_bio')  
    email=request.POST.get('email')
    user_image=request.FILES.get('user_image')
    location=request.POST.get('location')
    _type=request.POST.get('type')

    
    worker=Worker.objects.filter(username = username)
    if worker.exists():
        messages.info(request,'username already exists ')
        return redirect('/worker_reg')
    
    worker = Worker.objects.create(
       first_name = first_name,
       last_name = last_name,
       username = username,
       address =address,
       dob =dob,
       phone_no = phoneno,
       user_bio = user_bio,
       location = location,
       email = email,
       user_image = user_image,
       type = _type

    )
    worker.set_password(password)
    worker.save()
    messages.info(request,'registered sucessfully')
    return redirect('/worker_reg')



   
def contact_view(request):

    return render(request,"contact.html")


def about_view(request):

    return render(request,"about.html")

