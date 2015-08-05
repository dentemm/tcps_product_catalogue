from django.shortcuts import render
from django.contrib import messages
from django.views.generic import TemplateView


# Create your views here.
class DashboardView(TemplateView):
	template_name = 'dashboard_home.html'

