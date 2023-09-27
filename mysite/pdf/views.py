from io import DEFAULT_BUFFER_SIZE
from django import template
from django.shortcuts import redirect, render
from .models import Profile
import pdfkit
from django.http import HttpResponse, response
from django.template import loader
import io
from users.models import Profile as user_profile_auth
from django.contrib.auth.decorators import login_required
# Create your views here.

def accept(request):

    if request.method == "POST":
        user_linked = request.user
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        phone = request.POST.get("phone","")
        summary = request.POST.get("summary","")
        degree = request.POST.get("degree","")
        school = request.POST.get("school","")
        university = request.POST.get("university","")
        skills  = request.POST.get("skills","")
        projects = request.POST.get("projects","")
        previous_work = request.POST.get("previous_work","")

        profile = Profile(user_linked=user_linked,name=name,email=email,phone=phone,summary=summary,degree=degree,school=school,university=university,skills=skills,projects=projects,previous_work=previous_work)
        profile.save()
        return redirect('list')
        
    return render(request,'pdf/accept.html')

def resume(request,id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('pdf/resume.html')
    html = template.render({'user_profile':user_profile})
    options = {
        'page-size':'Letter',
        'encoding':'UTF-8',
    }
    config = pdfkit.configuration(wkhtmltopdf=r'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
 
    #Must be 'option=options' and add 'configuration=config'
    pdf = pdfkit.from_string(html,False,options=options,configuration=config)
    # pdf = pdfkit.from_string(html,False,options)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition']='attachment'
    filename = "resume.pdf"

    return response

@login_required
def list(request):
    user = request.user
    profiles = Profile.objects.filter(user_linked=user)
    return render(request,'pdf/list.html',{'profiles':profiles})
