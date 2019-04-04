from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http  import HttpResponse
from django.contrib.auth.models import User
from .forms import NewProfileForm,NewProjectForm,VotesForm
from .models import Project,Profile,Votes
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProjectSerializer,ProfileSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly
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

@login_required(login_url='/accounts/login/')
def search_project(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        project = Project.search_project(search_term)
        message = f"{search_term}"

        return render(request, 'all-award/search.html',{"message":message,"project":project})
      
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

def votes(request,id):
    current_user = request.user
    post = Project.objects.get(id=id)
    votes = Votes.objects.filter(project=post)
  
    if request.method == 'POST':
            vote = VotesForm(request.POST)
            if vote.is_valid():
                design = vote.cleaned_data['design']
                usability = vote.cleaned_data['usability']
                content = vote.cleaned_data['content']
                rating = Votes(design=design,usability=usability,content=content,user=request.user,project=post)
                rating.save()
                return redirect('project')      
    else:
        form = VotesForm()
        return render(request, 'vote.html', {"form":form,'post':post,'user':current_user,'votes':votes})

class ProjectList(APIView):
    def get(self, request, format=None):
        all_project = Project.objects.all()
        serializers = ProjectSerializer(all_project, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        permission_classes = (IsAdminOrReadOnly,)

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        permission_classes = (IsAdminOrReadOnly,)