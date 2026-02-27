from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *
# Create your views here.
def HomePage(request):
    data=tbl_user.objects.get(id=request.session['uid'])
    return render(request,'User/HomePage.html',{'data':data})

def MyProfile(request):
    data=tbl_user.objects.get(id=request.session['uid'])
    return render(request,'User/MyProfile.html',{'data':data})

def EditProfile(request):
    data=tbl_user.objects.get(id=request.session['uid'])
    if request.method=="POST":
        data.user_name=request.POST.get('txt_name')
        data.user_email=request.POST.get('mail')
        data.user_contact=request.POST.get('txt_contact')
        data.user_address=request.POST.get('txt_address')
        data.save()
        return render(request,'User/EditProfile.html',{'msg':"profile Updated"})
    else:
        return render(request,'User/EditProfile.html',{'data':data})

def ChangePassword(request):
    data=tbl_user.objects.get(id=request.session['uid'])
    if request.method == "POST":
        Old_Password = request.POST.get('old_pass')
        New_Password = request.POST.get('new_pass')
        Re_type = request.POST.get('re_pass')
        password=data.user_password
        if Old_Password == password:
            if New_Password == Re_type:
                data.user_password=Re_type
                data.save()
                return render(request,'User/ChangePassword.html',{'msg':"Password Updated"})

            else:
                return render(request,'User/ChangePassword.html',{'msg':"Password Mismatched"})

        else:
            return render(request,'User/ChangePassword.html',{'msg':"Enter Correct Password"})

    return render(request,'User/ChangePassword.html')

def Complaint(request):
    userid=tbl_user.objects.get(id=request.session['uid'])
    complaintdata=tbl_complaint.objects.filter(user_id=request.session['uid'])
    if request.method == "POST":
        title=request.POST.get('txt_title')
        content=request.POST.get('txt_content')
        tbl_complaint.objects.create(complaint_title=title,complaint_content=content,user_id=userid)
        return render(request,'User/Complaint.html',{'msg':"Inserted"})
    else:   
        return render(request,'User/Complaint.html',{'complaintdata':complaintdata})

def Feedback(request):
    feedbackdata=tbl_feedback.objects.all()
    userid=tbl_user.objects.get(id=request.session['uid'])
    if request.method=='POST':
        feedback_content=request.POST.get('txt_feedback')
        tbl_feedback.objects.create(user_id=userid,feedback_content=feedback_content)
        return render(request,'User/Feedback.html',{'msg':"Inserted"})
    else:
        return render(request,'User/Feedback.html',{'feedbackdata':feedbackdata})


def DeafUserList(request):
    data=tbl_deafuser.objects.all()
    return render(request,'User/DeafUserList.html',{'abcd':data})

def requestdeaf(request,duid):
    duser=tbl_deafuser.objects.get(id=duid)
    user=tbl_user.objects.get(id=request.session['duid'])
    tbl_request.objects.create(user_id=user,deafuser_id=duser)
    return render(request,'User/DeafUserList.html',{'msg':"Msg Send"})

def logout(request):
    del request.session['uid']
    return redirect("Guest:Index")

def SignLanguageDetection(request):
    return render(request,'User/SignLanguageDetection.html',)
