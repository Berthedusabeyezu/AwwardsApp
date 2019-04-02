from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http  import HttpResponse
from django.contrib.auth.models import User
from .forms import NewProfileForm,NewProjectForm
from .models import Project,Profile
# Create your views here.



def home(request):
    projects=Project.objects.all()
    return render(request, 'welcome.html',{'projects':projects})

@login_required(login_url='/accounts/login/')
def profile(request, profile_id):
    return render(request, 'welcome.html')
@login_required(login_url='/accounts/login/')
def profile(request,id):
    project = User.objects.get(id = id)
    profile = Profile.objects.get(project = project)
    return render(request, 'profile.html',{"profile":profile})

@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
   
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()   
        return redirect('welcome')
    
    else:
        form = NewProfileForm()
    return render(request, 'new-profile.html', {"form": form})

def search_project(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        search_projects = project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-award/search.html',{"message":message,"projects": search_projects})
      
    else:
        message = "You haven't searched for any term"
        return render(request, 'all-award/search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def projects(request):
    project = Project.objects.all()
    return render(request, 'welcome.html',{"project":project})

@login_required(login_url='/accounts/login/')
def project(request):
    current_user = request.user 
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('welcome')

    else:
        form = NewProjectForm()
    return render(request, 'project.html', {"form": form})
