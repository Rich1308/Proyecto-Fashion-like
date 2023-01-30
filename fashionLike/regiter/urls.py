from django.urls import path
from . import views

app_name = "regiter"

urlpatterns = [
    path("my_view/",views.my_view,name="my_view"),
    path("myform/",views.myform,name="myform"),
    path("showform/",views.showform,name="showform"),
    path("myformreg/",views.showformregister,name="showformreg"),
]