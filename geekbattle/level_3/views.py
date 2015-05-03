from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Question
from level_2.forms import DocumentForm
from level_1.models import Answer
# Create your views here.

def home(request):
	if request.method == "GET":
		return render(request,'level_1/home.html')	
	else:
		obj=Answer.objects.get(user=request.user)
  		if obj.s3 == 0: 
			return render(request,'level_1/home.html')		         
		form = DocumentForm()
		question = Question.objects.get(id=str(1)) 
        	return render(request,
       		 'level_3/home.html',
        	{'form': form,'question':question.description}
    		)

def save(request):
 if request.method == "GET":
		return render(request,'level_1/home.html')	
 else:
  form = DocumentForm(request.POST, request.FILES)
  obj=Answer.objects.get(user=request.user)
  if obj.s3 < 0:
   handle=open('/home/kushagra/PROJECTS/geekbattle/static/files2/'+str(request.user),'w+b')
   if request.FILES == {}:
    handle.write("Null")   
    handle.close() 
   else:   
    handle.write(request.FILES['docfile'].read())   
    handle.close()
   obj.s3 = 0
   obj.save() 	
  return render(request,'level_1/home.html')					

