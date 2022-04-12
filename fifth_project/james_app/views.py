from django.shortcuts import render
from james_app.models import User
# Create your views here.
def index(request):
    webpage=User.objects.order_by('First_name')
    my_dict={'User_data':webpage}
    return render(request,'james_app/index.html',context=my_dict)

def base(request):
    return render(request,'james_app/base.html')
