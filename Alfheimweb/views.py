# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import TemplateView

class TasksView(TemplateView):

    template_name="Alfheimweb/Alfheimweb.html"
def measure(request):
	return HttpResponse("201")
