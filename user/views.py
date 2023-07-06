from  django.http import HttpResponse
import json
from django.shortcuts import render,redirect

from user.models import Data, Register
def index(request):
    return render(request,'openlayer_web_map/index.html')  

def showregister(request):
    return render(request,'app/register.html')

def homepage(request):
    return render(request,'app/login.html')

def register(request):
        name=request.GET['name']
        password=request.GET['password']
        mobno=request.GET['mobno']
        email=request.GET['email']
        try:
            register=Register.objects.create(name=name,password=password,mobno=mobno,email=email)
            
        except:
            return render(request,'app/register.html',{'message':'User is already present','name':name,'password':password,'mobno':mobno,'email':email})    
        return render(request,'app/login.html',{'message':'Registration successfully'})

def Add_data(request):
    name=request.GET['name']
    password=request.GET['password']
    mobno=request.GET['mobno']
    email=request.GET['email']
    Register.objects.create(name=name,password=password,mobno=mobno,email=email)
    return render(request,'app/login.html',{"message":"registration is  successfull.Please login now"})

def checkname(request):
    print(request.GET["name"])
    message="name already present"
    try:
        obj1=Register.objects.get(name=request.GET["name"])
        print(obj1)
    except:
        message='name does not exist'

    data={
        'message':message
       
        }
    jsondata=json.dumps(data) # dumps() converts python dictionary into JSON String
    print(jsondata)
    response=HttpResponse(f'{jsondata}',content_type='application/json')
    return response


def login(request): 
    name=request.GET['name']
    password=request.GET['password']
    
    if name==request.GET['name'] and password==request.GET['password']:

        return render(request,'app/datamanagement.html',{'message':'welcome User'}) 
    
    try:
       userfromdb=Register.objects.get(name=name)
     
    except:
        return render(request,'app/login.html',{"message":"Wrong name"})

    if(userfromdb.password==password):        
        data=data[0]        
        request.session['name']=name
        request.session['mobno']=0
        
    else:
        return render(request,'app/login.html',{'message':"Wrong password"})

def endpage(request):
    del request.session['name']
    return redirect(request,'app/register.html')

def logout(request):
    del request.session['name']
    del request.session['password']
    del request.session['email']
    del request.session['mobno']
    return redirect('http://register/')


def adddata(request):
    name=request.GET['name']
    password=request.GET['password']
    mobno=request.GET['mobno']
    email=request.GET['email']
    
    Data.objects.create(name=name,password=password,mobno=mobno,email=email)
    
    return render (request,'app/datamanagement.html',{"message":"data is added in database"})  
    

def viewdata(request):

    Data1=Data.objects.get(name=request.GET['name'],password=request.GET['password'],mobno=request.GET['mobno'],email=request.GET['email'],pickup=request.GET['pickup'],drop=request.GET['drop'],area=request.GET['area'])
    data={
        'name':Data1.name,
        'password':Data1.password,
        'email':Data1.email,
        'mobno':Data1.mobno,
       
    }
    json_data=json.dumps(data)
    response=HttpResponse(f'{json_data}',content_type='application/json')
    return response

    
def updatedata(request):
    updatequest=Data.objects.filter(name=request.GET['name'],password=request.GET['password'],mobno=request.GET['mobno'],email=request.GET['email'])
    updatequest.update(name=request.GET['name'],password=request.GET['password'],mobno=request.GET['mobno'],email=request.GET['email'])
    return render(request,'app/datamanagement.html',{'message':'data is updated'})
    
def deletedata(request):
    Data.objects.filter(name=request.GET["name"]).delete()
    return render(request,'app/datamanagement.html',{"message":"data is deleted"})


