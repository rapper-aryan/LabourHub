from django.urls import path,include
from . import views


urlpatterns = [
    path("",views.HomePage,name="homepage"),
    path("register/",views.RegisterPage,name="registerpage"),
    path("empregister/",views.EmpRegisterPage,name="empregisterpage"),
    path("log/",views.LoginPage,name="loginpage"),
    path("emplogin/",views.EmpLoginPage,name="emploginpage"),
    path("about/",views.AboutPage,name="aboutpage"),
    path("booking/",views.BookingPage,name="bookingpage"),

    path('manage/',views.ManageLab, name='managelab'),
    path('add/',views.Add, name='add'),
    path('edit/',views.Edit, name='edit'),
    path('update/<str:id>',views.Update, name='update'),
    path('delete/<str:id>',views.Delete, name='delete'),


    path('manageemp/',views.ManageEmp, name='manageemp'),
    path('addemp/',views.AddEmp, name='addemp'),
    path('editemp/',views.EditEmp, name='editemp'),
    path('updateemp/<str:id>',views.UpdateEmp, name='updateemp'),
    path('deleteemp/<str:id>',views.DeleteEmp, name='deleteemp'),

]