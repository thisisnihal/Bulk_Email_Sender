from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q


def home_view(request):
    return render(request, 'send_email_app/home.html')

def create_employee(request):
    message=""
    success=True
    if request.method == "POST":
        try:
            name = request.POST['name']
            email = request.POST['email']
            designation = request.POST['designation']
            if not all([name, email, designation]):
                raise ValidationError("All fields are required!")
            print(name, email, designation)
            Employee.objects.create(
                f_Name = name,
                f_Email = email,
                f_Designation = designation
            )
            message="Employee Successfully created!"
            return render(request, "send_email_app/create_employee.html", {"message": message, "success" : success})
        except ValidationError as e:
            messages.error(request, f'Validation Error: {str(e)}')
            success=False
            message=f"Validation Error"
        except IntegrityError as e:
            messages.error(request, 'User with this data already exist')
            success=False
            message="User with this data already exist"
        except Exception as e:
            messages.error(request, f'An unexpected error occurred: {str(e)}')
            success=False
            message="Internal error occured"
    return render(request, "send_email_app/create_employee.html", {"message": message, "success" : success})


def employee_list(request, message=""):
    employees = Employee.objects.all()
    search_query = request.GET.get('search', '')
    selected_designation = request.GET.get('designation', '')
    message=message if message else ""
    success=True
    designations = list(set(employee.f_Designation for employee in employees))
    designations = ["All"] + designations
    if search_query:
        employees = employees.filter(
             Q(f_Name__icontains=search_query) | Q(f_Email__icontains=search_query) | Q(f_Designation__icontains=search_query)
        )
    if selected_designation and selected_designation != "All":
        employees = employees.filter(f_Designation=selected_designation)

        
    return render(request, 'send_email_app/employee_list.html', {'employees': employees, "designations": designations, "message": message, "success" : success})


def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, f_Id=employee_id)
    employee.delete()
    message=f"Employee '{employee.f_Name}' deleted successfully"
    success=True
    messages.success(request, 'Employee deleted successfully')
    return employee_list(request, message)


def employee_emails_view(request):
    if request.method == "POST":
        selected_emails = request.POST.getlist('emails') 

        if not selected_emails:
            return render(request, 'send_email_app/employee_list.html')

        return render(request, 'send_email_app/employee_emails.html', {
            'email_list': selected_emails,
        })
    return redirect('employee_list')


def send_bulk_email(request):
    if request.method == "POST":
        subject = request.POST.get('subject')
        email_content = request.POST.get('email_content')
        selected_emails = request.POST.get('selected_emails').split(', ')

        if not email_content or not selected_emails:
            return render(request, 'send_email_app/employee_emails.html', {
            'email_list': selected_emails,
            "message": "Please enter recepient and message!",
            "success": False
            })

        try:
            for email in selected_emails:
                send_mail(
                    subject=subject, 
                    message="",
                    html_message=email_content,
                    from_email=settings.DEFAULT_FROM_EMAIL, 
                    recipient_list=[email],
                    fail_silently=False,
                )
            return render(request, 'send_email_app/employee_emails.html', {
            'email_list': selected_emails,
            "message": "Email sent successfully!",
            "success": True
        })
        except Exception as e:
            return render(request, 'send_email_app/employee_emails.html', {
            'email_list': selected_emails,
            "message": "error while sending Emails!",
            "success": False
        })

    return render(request, 'send_email_app/employee_emails.html', {
            'email_list': selected_emails,
            "message": "Invalid Request",
            "success": False
        })







def status(request, messages):
    return render("end_email_app/status", messages)