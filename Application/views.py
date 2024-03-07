
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from Application.models import Mydata
from django.core.files.storage import FileSystemStorage

# Create your views here.

def home(request):
     return render(request,"home.html")



def show(request):
     data=Mydata.objects.all()
     return render(request,"show.html",{'data':data})
    
def search(request):
    return render(request,"search.html")
 
def searchid(request):
    data=Mydata.objects.all()
    if request.method=="GET":
        st=request.GET.get('q')
        if st!=None:
         data=Mydata.objects.filter(Id=st)  
        return render(request,"searchid.html",{'data':data})

     
def send(request):
    if request.method =='POST' and request.FILES['image']:
        myfile=request.FILES['image']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        url=fs.url(filename)
        FNAME=request.POST['fname']
        LNAME=request.POST['lname']
        GENDER=request.POST['gender']
        CITY=request.POST['city']
        PHNO=request.POST['phno']
        Mydata(Fname=FNAME,Lname=LNAME,Gender=GENDER,City=CITY,Phone_no=PHNO,image=url).save()
        msg="Data Save Successfully"
        return render(request,"home.html",{'msg':msg})

    else:
        return HttpResponse("<h1> Not Found</h1>")
    
    

def delete(request):
    ID=request.GET['id']
    Mydata.objects.filter(Id=ID).delete()
    return HttpResponseRedirect("show")

















def edit(request):
    ID=request.GET['id'] 
    for data in Mydata.objects.filter(Id=ID):
         FNAME=data.Fname
         LNAME=data.Lname
         GENDER=data.Gender
         CITY=data.City
         PHNO=data.Phone_no
         myfile=data.image
        
    return render(request,"edit.html",{'ID':ID,'Fname':FNAME,'Lname':LNAME,'Gender':GENDER,
                                       'City':CITY,'Phone_no':PHNO,'image':myfile})


def RecordEdited(request):
    if request.method=='POST' and request.FILES['imagenew']:
        myfile=request.FILES['imagenew']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        url=fs.url(filename)
        ID=request.POST['ID']
        FNAME=request.POST['fname']
        LNAME=request.POST['lname'] 
        GENDER=request.POST['gender']
        CITY=request.POST['city']
        PHNO=request.POST['phno']
        Mydata(Id=ID,Fname=FNAME,Lname=LNAME,Gender=GENDER,City=CITY,Phone_no=PHNO,image=url).save()
        return HttpResponseRedirect("show")
    else:
        return HttpResponse("<h1>404 Not Found</h1>")