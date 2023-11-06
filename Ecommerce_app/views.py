from datetime import date
from imaplib import _Authenticator

from django.http import HttpResponse
from django.shortcuts import redirect, render

from Ecommerce_app.models import card_data, user_regestration

# Create your views here.

def hello(req):
    if (req.session.has_key('ref_count')):
        req.session['ref_count']=req.session['ref_count']+1
    else:
         req.session['ref_count']=1
    print(req.session['ref_count'])
    card_posts = card_data.objects.all()
    return render(req,'index.html',{'card_posts': card_posts})

def search(req):
    search_name = req.POST['TEXT_FIELD']
    print(search_name)
    if card_data.objects.filter(product_name__icontains=search_name).count()>0:
        matching_data=card_data.objects.filter(product_name__icontains=search_name)
        print(matching_data)
        return render(req,'search_page.html',{"matching_data":matching_data})
    else:
        return HttpResponse('<h1 style="text-align:center">Sorry Product is Not found Check Spelling')

def login(req):
    return render(req,'login.html')

def all_product(req):
     card_posts = card_data.objects.all()
     return render(req,'index.html',{'card_posts': card_posts})
def hello1(req):
    card_posts = card_data.objects.all()[:8]
    return render(req,'index.html',{'card_posts': card_posts})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if 'Nikhil'==username and '123'==password:
              card_posts = card_data.objects.all()[:8]
              print(card_posts)
              return render(request,'index.html',{'card_posts': card_posts})
        else:
            return HttpResponse("<script>alert('Username and password not correct exists....');location.href='/login_view/'</script>")
    else:
        return render(request,'login.html')


def regestartion(req):
     today1 = date.today()
     if user_regestration.objects.filter(user_name=req.POST.get('signup-username')).count()>0:
            return HttpResponse("<script>alert('Username already exists....');location.href='/login_view/'</script>")
     else:
         newuser1=user_regestration(
            user_name = req.POST.get('signup-username'),
            user_email = req.POST.get('signup-Email'),
            user_mobile = req.POST.get('signup-Mobile'),
            user_address = req.POST.get('signup-Address'),
            user_password = req.POST.get('signup-password'),
            reg_Date = today1,
            )
         newuser1.save()
         return render(req,'index.html')

def Bye_page(req,arg1):
    card_posts = card_data.objects.all().filter(id=arg1)
    return render(req,'Bye_page.html',{"card_posts":card_posts})


def address(req):
    return render(req,'address.html')

def succesfull(req):
    return render(req,'succesfull.html')

def Feedback(req):
    return render(req,'feedback.html')