
from django.contrib import admin
from django.urls import path ,include
from.import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('',views.signup),
    path('loginn/',views.loginn),
    path('todopage/',views.todo),
    path('edit_todo/<int:srno>',views.edit_todo,name='edit_todo'),
    path('delete_todo/<int:srno>',views.delete_todo),
    path('signout/',views.signout,name='signout'),
    path('signup/', views.signup, name='signup'),
]
