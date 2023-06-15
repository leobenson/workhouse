from django.shortcuts import render

# Create your views here.
def my_view(request):

    return render(request,"index.html")

def login_view(request):

    return render(request,"login.html")


def user_reg(request):

    return render(request,"userreg.html")


def worker_reg(request):

    return render(request,"workerreg.html")


def contact_view(request):

    return render(request,"contact.html")


def about_view(request):

    return render(request,"about.html")

