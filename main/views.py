from django.shortcuts import redirect, render
from django.contrib import messages 
from django.contrib import auth 
from django.contrib.auth import authenticate , login ,logout


from main.models import Moderator, User, Worker ,Job_post



# Create your views here.
def my_view(request):

    return render(request,"index.html")



def user_home(request):
    username = request.session.get('username')
    users =User.objects.all()
    for i in users:
        if i.username == username:
            f_name=i.first_name
            l_name=i.last_name
            img=i.user_image
    
    
    user= User.objects.get(username=username )
    job_posts = Job_post.objects.filter(user_id=user)
    worker = Worker.objects.all() 
    
           
    context = {'username':username,'f_name':f_name,'l_name':l_name,'img':img, 'history':job_posts, 'worker':worker}                            
    
    return render(request,"userhome.html",context)

def worker_home(request):
    username = request.session.get('username')
    users =Worker.objects.all()
    for i in users:
        if i.username == username:
            f_name=i.first_name
            l_name=i.last_name
            img=i.user_image

    post =Job_post.objects.all()        
    context = {'username':username,'f_name':f_name,'l_name':l_name,'img':img , 'post':post}
    
    return render(request,"workhome.html",context)


def moderator_home(request):

    return render(request,"moderator_home.html")



def admin_home(request):
    if request.method != "POST":
        return render(request,'admin_home.html')
    username = request.POST.get('username')
    password = request.POST.get('password')    
    address = request.POST.get('address')
    phone = request.POST.get('phoneno')   
    email=request.POST.get('email')    
    location=request.POST.get('location')
   

    moderator=Moderator.objects.filter(username = username)
    if moderator.exists():
        messages.info(request,'username already exists ')
        return redirect('/admin_home')

    moderator = Moderator.objects.create(
      
       username = username,
       address =address,      
       phone = phone,       
       location = location,
       email = email,      

    )
    moderator.set_password(password)
    moderator.save()
    messages.info(request,'registered sucessfully')
    return redirect('/admin_home')




def job_post(request):
    username = request.session.get('username')
    users =User.objects.all()
    for i in users:
        if i.username == username:
            f_name=i.first_name
            l_name=i.last_name
            img=i.user_image
    context = {'username':username,'f_name':f_name,'l_name':l_name,'img':img}

    if request.method == "POST":
        job_title=request.POST.get('job_title')
        job_description=request.POST.get('job_description')
        location=request.POST.get('location')
        address=request.POST.get('address')
        time=request.POST.get('time')
        date=request.POST.get('date')
        min_wage=request.POST.get('min_wage')
        max_wage=request.POST.get('max_wage')
        exp_lvl=request.POST.get('exp_lvl')
        expected_time=request.POST.get('expected_time')
        photo=request.FILES.get('photo')

        user_id = request.session.get('id')

        Job_post.objects.create(
        job_title=job_title, 
        job_description=job_description,
        location=location,
        address=address,
        time=time,
        date=date,
        min_wage=min_wage,
        max_wage=max_wage,
        exp_lvl=exp_lvl,
        expected_time=expected_time,
        photo=photo,
        user_id=user_id           

        )
        messages.info(request,'created sucessfully')
        
    return render(request,"jobpost.html",context)



    
    



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
                return _extracted_from_login_view_21(request, user, 'user_home')
            elif isinstance(user, Worker):
                return _extracted_from_login_view_21(request, user, 'worker_home')
    return render(request,"login.html")


# TODO Rename this here and in `login_view`
def _extracted_from_login_view_21(request, user, arg2):
    login(request, user)
    request.session['username'] = request.user.username
    request.session['id'] = request.user.id
    return redirect(arg2)

  

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

def worker_valid(request):

    return render(request,"workervalidation.html")

   
def contact_view(request):

    return render(request,"contact.html")


def about_view(request):

    return render(request,"about.html")

