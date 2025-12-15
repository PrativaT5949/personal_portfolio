from django.urls import path
from .views import ProjectView
app_name = "project"
urlpatterns = [
    path('', ProjectView.as_view(), name='index'),
]
