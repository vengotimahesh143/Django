from django.shortcuts import render,redirect
from django.http import HttpResponse
from Action.models import *

# Create your views here.
def index(req):
	return render(req,'Action/index.html')
def home(req):
	return render(req,'Action/home.html')
def about(req):
	return render(req,'Action/about.html')
def register(req):
	if req.method=="POST":
		name=req.POST['hname']
		age=req.POST['age']
		email=req.POST['email']
		password=req.POST['password']
		hmname=req.POST['mname']

		data=Heroin_register(h_name=name,h_age=age,h_email=email,h_password=password,h_manager=hmname)
		data.save()
		return HttpResponse("data added successfully")
	return render(req,"Action/register.html")
def contactus(req):
	if req.method=="POST":
		pname=req.POST['cname']
		pmobile=req.POST['mobile']
		pemail=req.POST['email']
		pcomplaint=req.POST['complaint']
		pgender=req.POST['gender']

		data=Contact_complaint(c_name=pname,c_mobileno=pmobile,c_email=pemail,c_gender=pgender,c_complaint=pcomplaint)
		data.save()
		return render(req,'Action/index.html')
	return render(req,'Action/contact.html')
def showdata(req):
	data=Contact_complaint.objects.all()

	return render(req,'Action/showdata.html',{"data":data})
def edit(req,id):
	data=Contact_complaint.objects.get(id=id)
	print(data)
	return render(req,'Action/update.html',{"data":data})

def update(req,id):
	if req.method=="POST":
		pname=req.POST['cname']
		pmobile=req.POST['mobile']
		pemail=req.POST['email']
		pcomplaint=req.POST['complaint']
		pgender=req.POST['gender']

		obj=Contact_complaint.objects.filter(id=id).update(c_name=pname,c_mobileno=pmobile,c_email=pemail,c_gender=pgender,c_complaint=pcomplaint)
		return redirect('/Action/showdata')


def delete(req,id):
	data=Contact_complaint.objects.get(id=id)
	data.delete()
	return render(req,'Action/index.html')