from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *
from DeafUser.models import *


# Create your views here.
def district(request):
    dis=tbl_district.objects.all()#select
    if request.method == "POST":
        districtcount=tbl_district.objects.filter(district_name=request.POST.get("dis_txt")).count()
        if districtcount>0:
            return render(request,'Admin/district.html',{'msg': " district already exist"})  
        else:
            tbl_district.objects.create(district_name=request.POST.get("dis_txt"))#insert
            return redirect("Admin:district")
    return render(request,'Admin/district.html',{'district':dis})#select


def delDistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return render(request,'Admin/district.html',{'msg':"District Deleted"})

def editDistrict(request,eid):
    editData=tbl_district.objects.get(id=eid)
    if request.method == "POST":
        editData.district_name=request.POST.get('dis_txt')
        editData.save()
        return render(request,'Admin/district.html',{'msg':"District Updated"})
    else:
        return render(request,'Admin/district.html',{'editData':editData})
    

def category(request):
    catg=tbl_category.objects.all()
    if request.method == "POST":
        tbl_category.objects.create(category_name=request.POST.get("cat_txt"))
        return redirect("Admin:category")
    return render(request,'Admin/Category.html',{'category':catg})

def delcatg(request,cat):
    tbl_category.objects.get(id=cat).delete()
    return render(request,'Admin/category.html', {'msg':"category deleted"})

def editCatg(request,edi):
    editData=tbl_category.objects.get(id=edi)
    if request.method== "POST":
        editData.category_name=request.POST.get('cat_txt')
        editData.save()
        return render(request,'Admin/Category.html',{'msg':"District Updated"})
    else:
        return render(request,'Admin/Category.html',{'editData':editData})
        



def AdminRegistration(request):
    reg=tbl_admin.objects.all()
    if request.method == "POST":
        emailcount=tbl_user.objects.filter(user_email=email).count()
        if emailcount>0:
            return render(request,'Guest/Login.html',{'msg': " email already exist"})  
        else:
            tbl_admin.objects.create(admin_name=request.POST.get("txt_name"),admin_email=request.POST.get("txt_mail"),admin_pass=request.POST.get("txt_pass"))
            return redirect("Admin:AdminRegistration")
    return render(request,'Admin/AdminRegistration.html',{'registration':reg})

def delAdmin(request,adm):
    tbl_admin.objects.get(id=adm).delete()
    return render(request,'Admin/AdminRegistration.html',{'msg':"adminregistration deleted"})

def editAdmin(request,dei):
    editData=tbl_admin.objects.get(id=dei)
    if request.method == "POST":
        editData.admin_name=request.POST.get('txt_name')
        editData.admin_email=request.POST.get('txt_mail')
        editData.admin_pass=request.POST.get('txt_pass')
        editData.save()   
        return render(request,'Admin/AdminRegistration.html',{'msg':"messege updated"})
    else:
        return render(request,'Admin/AdminRegistration.html',{'editData':editData})

def place(request): 
    districtData=tbl_district.objects.all() #select (get values) create loop in options to get value
    placeData=tbl_place.objects.all()
    if request.method == "POST": #insert
         place=request.POST.get('place_txt') 
         district=tbl_district.objects.get(id=request.POST.get('sel_district'))
         placecount=tbl_place.objects.filter(place_name=place).count()
         if placecount>0:
             return render(request,'Admin/place.html',{'msg': " place already exist"}) 
         else:
             tbl_place.objects.create(place_name=place,district=district)  #insert
             return render(request,'Admin/place.html',{'msg':"place insertedd"})
    else: 
            return render(request,'Admin/place.html',{'districtData':districtData,'placeData':placeData})

def delplace(request,plc):
    tbl_place.objects.get(id=plc).delete()
    return render(request,'Admin/place.html',{'msg':"place deleted"})


def SubCategory(request):
    categoryData=tbl_category.objects.all()
    subcategoryData=tbl_subcatgory.objects.all()  #select
    if request.method == "POST":
        SubCatgory=request.POST.get('sub_txt')
        category=tbl_category.objects.get(id=request.POST.get('select_category'))
        tbl_subcatgory.objects.create(subcatgory_name=SubCategory,category=category)
        return render(request,'Admin/SubCategory.html',{'msg':"subcategory inserted"})
    else: 
        return render(request,'Admin/SubCategory.html',{'categoryData':categoryData,'subcategoryData':subcategoryData})

def delsubcategory(request,sid):
    tbl_subcatgory.objects.get(id=sid).delete()
    return render(request,'Admin/SubCategory.html',{'msg':"deleted"})

def editsubcategory(request,cid):
    categoryData=tbl_category.objects.all()
    editsubcategory=tbl_subcatgory.objects.get(id=cid)
    if request.method=="POST":
        subcat=request.POST.get('sub_txt')
        categoryid=tbl_category.objects.get(id=request.POST.get('select_category'))
        editsubcategory.subcatgory_name=subcat
        editsubcategory.category=categoryid
        editsubcategory.save()
        return render(request,"Admin/SubCategory.html",{'msg':'Updated'})
    else:
        return render(request,"Admin/SubCategory.html",{'editsubcategory':editsubcategory,'categoryData':categoryData})


def editplace(request,pcl):
    districtDataData=tbl_district.objects.all()
    editplace=tbl_place.objects.get(id=pcl)
    placeData=tbl_place.objects.all()
    if request.method=="POST":
        placee=request.POST.get('place_txt')
        districtid=tbl_district.objects.get(id=request.POST.get('sel_district'))
        editplace.place_name=placee
        editplace.district=districtid
        editplace.save()
        return render(request,"Admin/place.html",{'msg':"updated"})
    else:
         return render(request,"Admin/place.html",{'districtData':districtDataData,'editplace':editplace,'placeData':placeData})

def HomePage(request):
    return render(request,'Admin/HomePage.html')

def User(request):
    data=tbl_user.objects.all()
    return render(request,'Admin/User.html',{'abcd':data})

def acceptuser(request,aid):
    userdata=tbl_user.objects.get(id=aid)
    userdata.user_status=1
    userdata.save()
    return render(request,'Admin/User.html',{'msg':"verified"})

def rejectuser(request,rid):
    userdata=tbl_user.objects.get(id=rid)
    userdata.user_status=2
    userdata.save()
    return render(request,'Admin/User.html',{'msg':"verified"})

def Reply(request,vid):
    viewdata=tbl_complaint.objects.get(id=vid)
    if request.method=='POST':
        viewdata.complaint_reply=request.POST.get('reply_txt')
        viewdata.complaint_status=1
        viewdata.save()
        return render(request,'Admin/Reply.html',{'msg':"Reply Sended"})
    else:
        return render(request,'Admin/Reply.html')

def ViewComplaint(request):
    viewData=tbl_complaint.objects.all()
    return render(request,'Admin/ViewComplaint.html',{'viewData':viewData})

def DeafUser(request):
    data=tbl_deafuser.objects.all()
    return render(request,'Admin/DeafUser.html',{'abcd':data})


def acceptdeafuser(request,aid):
    userdata=tbl_deafuser.objects.get(id=aid)
    userdata.user_status=1
    userdata.save()
    return render(request,'Admin/DeafUserList.html',{'msg':"verified"})

def rejectdeafuser(request,rid):
    userdata=tbl_deafuser.objects.get(id=rid)
    userdata.user_status=2
    userdata.save()
    return render(request,'Admin/DeafUserList.html',{'msg':"verified"})

def logout(request):
    del request.session['aid']
    return redirect("Guest:Index")