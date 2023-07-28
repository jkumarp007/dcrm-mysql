from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:record_id>', views.record_view, name='record_view'),
    path('record-remove/<int:record_id>', views.record_delete, name='record_delete'),
    path('record-edit/<int:record_id>/', views.record_edit, name='record_edit'),
    path('record-add/', views.record_add, name='record_add'),
    
    
    
]

