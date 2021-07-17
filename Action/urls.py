from django.urls import path
from Action import views

urlpatterns = [
    path('index/', views.index,name="index"),
    path('home/',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('register/',views.register,name="register"),
    path('contactus/',views.contactus,name="contactus"),
    path('showdata/',views.showdata,name="showdata"),
    path('edit/<int:id>',views.edit,name="edit"),
    path('update/<int:id>',views.update,name="update"),
    path('delete/<int:id>',views.delete,name="delete"),

]