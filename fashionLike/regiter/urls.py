from django.urls import path
from . import views
from .views import Fashion_like

app_name = "regiter"

urlpatterns = [
    #path("my_view/",views.my_view,name="my_view"),
    #path("myform/",views.myform,name="myform"),
    #path("showform/",views.showform,name="showform"),
    #path("myformreg/",views.showformregister,name="showformreg"),
    path("Fashion/",Fashion_like.as_view(),name="register"),
    path("Fashion/<int:id>/",Fashion_like.as_view(),name="onedata"),
    path("",views.index,name="index"),
]