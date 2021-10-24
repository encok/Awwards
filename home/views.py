from django.shortcuts import render,redirect
from projects.models import project
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from projects.models import project
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator

# Create your views here.



class Home(TemplateView):
    context = {}
    template_name = 'home/home.html'

    def get(self, request, *args, **kwargs):
        user = request.user.id
        if user:
            return redirect('userhome')
        data = project.objects.all()
        self.context['data'] = data
        return render(request,self.template_name , self.context)

        # search function

    def search_results(request):
        if 'titles' in request.GET and request.GET['titles']:
            search_term = request.GET.get("titles")
            searched_projects = Home.search_by_projects(search_term)
            
            message = f'{search_term}'
            
            return render(request,'search.html',{"message":message,"projects":searched_projects})
        
        else:
            message = "You haven't searched for any term"
            return render(request,'search.html',{"message":message,"projects":searched_projects})

