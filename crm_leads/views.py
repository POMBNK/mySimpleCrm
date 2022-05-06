from django.http import HttpRequest, HttpResponseRedirect, QueryDict
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ModelLeadForm, ModelLeadFormUpdate
from .models import Lead


def lead_list(request:HttpRequest)-> render:
   '''This function shows a list of leads at the page from queryset '''
   context = {
      "leads": Lead.objects.all()
   }
   return render(request,'crm_leads/lead_list.html', context)


def lead_details(request:HttpRequest,pk:int)-> render:
   '''This function shows a list of details about current lead'''
   context = {
      "lead":Lead.objects.get(id=pk)
   }
   return render(request,'crm_leads/lead_details.html',context)


def lead_create(request:QueryDict)->render:
   '''This function renders the page with form to create a new lead'''
   leadform = ModelLeadForm()
   print(request.POST)
   if request.method == "POST":
      print("receiving a POST request...")
      # create a form instance and populate it with data from the request: (from documentation)
      leadform = ModelLeadForm(request.POST)
      if leadform.is_valid():
         print("Your form is passed the validation")
         leadform.save()
         return HttpResponseRedirect(reverse("leads"))
      else:
         leadform = ModelLeadForm()
   return render(request,'crm_leads/lead_create.html',{'leadform':leadform})


def lead_update(request:QueryDict,pk:int)->render:
   '''This function renders the page with form to update an existing lead'''
   lead = Lead.objects.get(id=pk)
   leadform_update = ModelLeadFormUpdate(instance=lead)
   print(request.POST)
   if request.method == "POST":
      print("receiving a POST request...")
      leadform_update = ModelLeadFormUpdate(request.POST,instance=lead)
      if leadform_update.is_valid():
         print("Your form is passed the validation")
         leadform_update.save()
         return redirect(f'/leads/{pk}')
      else:
         leadform_update = ModelLeadFormUpdate()   
   return render(request,'crm_leads/lead_update.html',{'leadform_update':leadform_update,"lead":lead})   
