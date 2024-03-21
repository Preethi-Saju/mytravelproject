from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    objteam=Team.objects.all()
    return render(request,"index.html",{'result':obj,'result1':objteam})
# def about(request):
#     return render(request,"about.html")
# def contact(request):
#     return HttpResponse("<b>Contacts:</b>")
# def details(request):
#     return render(request,"details.html")
# def thanks(request):
#     return HttpResponse("<b>Thankyou</b>")