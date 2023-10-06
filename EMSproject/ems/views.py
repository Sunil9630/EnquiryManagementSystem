from django.shortcuts import render
from django.http import JsonResponse
from .models import AdminDataBase,userDashboardDataBase,UserDataBase

def homePageView(request):
    return render(request,'home.html')


def aregistration(request):
    if request.method == 'POST':

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        user = AdminDataBase.objects.filter(email=email)

        if user:
            msg= "User already exist"
            return render(request,'aregistration.html',{'msg':msg})
        else:
            newdatainsert = AdminDataBase(firstname=fname,email=email,lastname=lname,contact=contact,password=password)
            newdatainsert.save()
            return render(request,'aregistration.html')
    return render(request,'aregistration.html')

    

def adminloginpage(request):
    if request.method=='POST':
        # print(request.POST)
        email=request.POST.get('email')
        fname=request.POST.get('fname')
        user=AdminDataBase.objects.get(email=email)
        if user:
            if user.firstname==fname:
                request.session['fname']=user.firstname
                request.session['email']=user.email
                return render(request,'adminloginpage.html')
        else:
            msg="First Name not matched"
            return render(request,'adminloginpage.html',{'msg':msg})
    else:
        msg="user dose not exit"
        return render(request,'adminloginpage.html',{'msg':msg})




def userDashboard(request):
     if request.method == 'POST':
        query = request.POST['txtarea']
        return render(request,'aregistration.html',{'msg':query})
     return render(request,'userDashboard.html')
 
def uregistration(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']
        user = UserDataBase.objects.filter(email=email)
        if user:
            msg= "User already exist"
            return render(request,'uregistration.html',{'msg':msg})
        else:
            newdatainsert = AdminDataBase.objects.create(firstname=fname,email=email,lastname=lname,contact=contact,password=password)
            return render(request,'home.html')
    return render(request,'uregistration.html')

def userloginpage(request):
     return render(request,'userloginpage.html')