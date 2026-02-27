from django.db import models
from Guest.models import *
# Create your models here.
class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=50)
    complaint_content=models.CharField(max_length=50)
    complaint_date=models.DateField(auto_now_add=True)
    complaint_reply=models.CharField(max_length=50)
    complaint_status=models.IntegerField(default=0)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_feedback(models.Model):
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    feedback_content=models.CharField(max_length=50)

class tbl_request(models.Model):
    request_status=models.IntegerField(default=0)
    request_date=models.DateField(auto_now_add=True)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    deafuser_id=models.ForeignKey(tbl_deafuser,on_delete=models.CASCADE)

class tbl_signlanguagefile(models.Model):
    signlanguage_photo = models.FileField("Assets/DeafUser/Photo")
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    signlanguage_result=models.CharField(max_length=50)



