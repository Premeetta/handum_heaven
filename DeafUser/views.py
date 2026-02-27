from django.shortcuts import render,redirect
from DeafUser.models import *
from Admin.models import*
from Guest.models import*


def HomePage(request):
    data=tbl_deafuser.objects.get(id=request.session['duid'])
    return render(request,'DeafUser/HomePage.html',{'data':data})

def MyProfile(request):
    data=tbl_deafuser.objects.get(id=request.session['duid'])
    return render(request,'DeafUser/MyProfile.html',{'data':data})

def EditProfile(request):
    data=tbl_deafuser.objects.get(id=request.session['duid'])
    if request.method=="POST":
        data.deafuser_name=request.POST.get('txt_name')
        data.deafuser_email=request.POST.get('mail')
        data.deafuser_address=request.POST.get('txt_address')
        data.save()
        return render(request,'DeafUser/EditProfile.html',{'msg':"profile Updated"})
    else:
        return render(request,'DeafUser/EditProfile.html',{'data':data})

def ChangePassword(request):
    data=tbl_deafuser.objects.get(id=request.session['duid'])
    if request.method == "POST":
        Old_Password = request.POST.get('old_pass')
        New_Password = request.POST.get('new_pass')
        Re_type = request.POST.get('re_pass')
        password=data.deafuser_password
        if Old_Password == password:
            if New_Password == Re_type:
                data.user_password=Re_type
                data.save()
                return render(request,'DeafUser/ChangePassword.html',{'msg':"Password Updated"})

            else:
                return render(request,'DeafUser/ChangePassword.html',{'msg':"Password Mismatched"})

        else:
            return render(request,'DeafUser/ChangePassword.html',{'msg':"Enter Correct Password"})

    return render(request,'DeafUser/ChangePassword.html')
# Create your views here.



def logout(request):
    del request.session['duid']
    return redirect("Guest:Index")
