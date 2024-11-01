from django.urls import path
from . import views


urlpatterns = [
    path("",views.index,name="index"),
    path('login/',views.LoginView.as_view(),name='login'),
    path('login/',views.LogoutView.as_view(),name='logout'),
    path('register/',views.RegisterView.as_view(),name='register'),
    path("break/",views.break_time,name="break_time"),
    path("lunch/",views.lunch_time,name="lunch_time"),
    path("work/<int:id>/",views.work,name="work")

]
