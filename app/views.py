from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def main(request):
    return render(request,"Login_form.html")

def login(request):
    username = request.POST['textfield']
    password = request.POST['textfield2']

    if Login.objects.filter(username=username,password=password).exists():
        login_get = Login.objects.get(username=username,password=password)
        request.session['lid'] = login_get.id
        if login_get.type == 'admin':
            return HttpResponse('''<script>alert('Admin Login Success');window.location='/admin_home'</script>''')
        elif login_get.type == 'university':
            return HttpResponse('''<script>alert('University Login Success');window.location='/universityHomepage'</script>''')
        else:
            return HttpResponse('''<script>alert('Invalid');window.location='/'</script>''')
    else:
        return HttpResponse('''<script>alert('Invalid');window.location='/'</script>''')


def admin_home(request):
    return render(request,"admin/admin_homepsge.html")


def manage_university(request):
    return render(request,"admin/manage_university.html")

def reply_complaint(request):
    return render(request,"admin/reply_complaint.html")

def view_complaints(request):
    return render(request,"admin/view_complaints.html")

def view_employers(request):
    return render(request,"admin/view_employers.html")

def view_feedback(request):
    return render(request,"admin/view_feedback.html")

def view_ceritficate(request):
    return render(request, "admin/view_certificate.html")




def generate_certificate(request):
    return render(request,"university/generate_certificate.html")

def sendComplaint(request):
    return render(request,"university/sendComplaint.html")

def sendFeedback(request):
    return render(request,"university/sendFeedback.html")
def universityHomepage(request):
    return render(request,"university/universityHomepage.html")

def uploadHistory(request):
    return render(request,"university/uploadHistory.html")

def uploadTemplate(request):
    return render(request,"university/uploadTemplate.html")


