from django.urls import path
from . import views
urlpatterns = [
    path('',views.signup,name='signup'),
    path('addUser',views.addUser,name='addUser'),
    path('index',views.index,name='index'),
    path('add',views.add,name='add'),
    path('edit',views.edit,name='edit'),
    path('update/<str:id>',views.update,name='update'),
    path('delete/<str:id>',views.delete,name='delete'),
    path('logon',views.logon,name='logon'),
    path('loggedin',views.loggedin,name='loggedin'),
    path('logout',views.log_out,name='logout')
]
