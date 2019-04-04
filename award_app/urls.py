from django.conf import settings
from django.conf.urls import url
from . import views
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.home,name = 'welcome'),
    url(r'^profile/(\d+)', views.profile, name='profile'),
    url(r'^new/profile', views.new_profile, name='edit_profile'),
    url(r'^search/', views.search_project, name='search_project'),
    url(r'^new/project', views.project, name='project'),
    url(r'^votes/(\d+)',views.votes,name="votes"),
    url(r'^api/project/$', views.ProjectList.as_view()),
    url(r'^api/profile/$', views.ProfileList.as_view()),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)               