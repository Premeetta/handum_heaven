from django.urls import path
from User import views
app_name = "User"
urlpatterns = [
    path('HomePage/',views.HomePage,name="HomePage"),  
    path('MyProfile/',views.MyProfile,name="MyProfile"),
    path('EditProfile/',views.EditProfile,name="EditProfile"),
    path('ChangePassword/',views.ChangePassword,name="ChangePassword"),
    path('Complaint/',views.Complaint,name="Complaint"),  
    path('Feedback/',views.Feedback,name="Feedback"),  
    path('DeafUserList/',views.DeafUserList,name="DeafUserList"),
    path('requestdeaf/<int:duid>/',views.requestdeaf,name="requestdeaf"),
    path('logout/',views.logout,name="logout"),
    path('SignLanguageDetection/',views.SignLanguageDetection,name="SignLanguageDetection"),


]