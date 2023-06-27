from django.shortcuts import redirect, render
from django.contrib import messages 
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate , login ,logout

User = get_user_model()

# Create your views here.
def my_view(request):

    return render(request,"index.html")




def user_home(request):
    username = request.session.get('username')
    context = {'username':username}                            

    return render(request,"user_home.html",context)

def worker_home(request):
    
    return render(request,"worker_home.html")



def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, 'invalid username')
            return redirect('/login_view')

        user =authenticate(username = username,password = password)

        if user is None:
            messages.error(request , 'invalid password')
            return redirect('/login_view')
        else:
            if user.type == 'user':
                login(request,user)
                request.session['username'] = request.user.username
                return redirect('/user_home')
            else:
                login(request,user)
                request.session['username'] = request.user.username
                return redirect('/worker_home')
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

    return render(request,'workerreg.html')
   
def contact_view(request):

    return render(request,"contact.html")


def about_view(request):

    return render(request,"about.html")

