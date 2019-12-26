from projects import views
from django.urls import path

app_name = 'projects'

urlpatterns = [
    path('', views.all_projects, name='all_projects'),
    path('<int:pk>', views.project_detail, name='project_detail'),
]
