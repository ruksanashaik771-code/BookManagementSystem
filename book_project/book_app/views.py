from django.http import HttpResponse
from django.shortcuts import render
from  .models import UserModel
# Create your views here.
def home_page(request):
    return render(request,'home.html')
def profile_page(request):
    return render(request,'profile.html',{"name":"amit","email":"amit@gmail.com","role":"admin",
                                        "user_data":[{"name":"mohith","email":"mohith@gmail.com"},
                                        {"name":"mohan","email":"mohan@gmail.com"}]})
def contact_page(request):
    return render(request,'contacts.html',{"range":range(0,10)})
def skills_page(request):
    return render(request,'skills.html',{"skill1":"reading","skill2":"sleeping","skill3":"studying"})
def proj_page(request):
    return render(request,'project.html',{"proj1":"weather application","proj2":"protfolio page"})
def marks_page(request):
    return render(request,'marks.html',{"marks":30,"role":"marks"})
def add_user(request):
    if request.method=="POST":

        name=request.POST.get("name")
        email=request.POST.get("email")
        # print(name,email) to print in terminal
        data=UserModel.objects.create(
            name=name,email=email
        )#TO SEND IN MYSQL
        return HttpResponse("user successfully added")
    return render(request,"user_form.html")

