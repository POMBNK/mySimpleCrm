from django.http import HttpRequest, HttpResponseRedirect, QueryDict
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import LeadForm
from .models import Agent, Lead


def lead_list(request:HttpRequest)-> render:
   '''This function shows a list of leads at the page from queryset '''
   context = {
      "leads": Lead.objects.all()
   }
   return render(request,'crm_leads/lead_list.html', context)


def lead_details(request:HttpRequest,pk:int)-> render:
   print(request.GET)
   '''This function shows a list of details about current lead'''
   context = {
      "lead":Lead.objects.get(id=pk)
   }
   return render(request,'crm_leads/lead_details.html',context)


def lead_create(request:QueryDict)->render:
   '''This function renders the page with form to create a new lead'''
   leadform = LeadForm()
   print(request.POST)
   if request.method == "POST":
      print("receiving a POST request...")
      # create a form instance and populate it with data from the request: (from documentation)
      leadform = LeadForm(request.POST)
      if leadform.is_valid():
         print("Your form is passed the validation")
         first_name = leadform.cleaned_data['first_name']
         last_name = leadform.cleaned_data['last_name']
         age = leadform.cleaned_data['age']
         agent = Agent.objects.get(id=1) # temporary plug to check how forms are working
         Lead.objects.create(
            first_name = first_name,
            last_name = last_name,
            age = age,
            agent = agent
         )
         return HttpResponseRedirect(reverse("pisya"))
      else:
         leadform = LeadForm()
   return render(request,'crm_leads/lead_create.html',{'leadform':leadform})