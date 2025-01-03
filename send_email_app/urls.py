from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('employee_list/', views.employee_list, name='employee_list'),
    path('create_employee/', views.create_employee, name='create_employee'),
    path('delete_employee/<int:employee_id>/', views.delete_employee, name='delete_employee'),
    path('employee/emails/', views.employee_emails_view, name='employee_emails'),
    path('send_bulk_email/', views.send_bulk_email, name='send_bulk_email'),
    path('status/', views.status, name="status"),

]
