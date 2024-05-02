from django.shortcuts import render
from django.http import HttpResponse
import os
from pathlib import Path
from .models import Gallery
BASE_DIR = Path(__file__).resolve().parent.parent
# Create your views here.


def home(request):
	return render(request,'akhil.html')

def gallery(request):
	
	path=str(BASE_DIR)+"/static/akhil_img/"
	images=sorted(os.listdir(path))
	
	with open(str(BASE_DIR)+"/static/akhil_gallery.txt","r") as file:
		data=file.readlines()
		for i in range(len(data)):
			data[i]=data[i].rstrip("\n")
			
	objec=[]
	for i in range(len(images)):
		gallery1=Gallery()
		gallery1.img= images[i]
		
		if i%2==0:
			gallery1.even=True
		else:
			gallery1.even=False
		if i < len(data):
			gallery1.text=data[i]
		else:
			gallery1.text="❤️"
		objec.append(gallery1)
	
		
		
	
		
	return render(request,'gallery.html',{'object':objec})
	


