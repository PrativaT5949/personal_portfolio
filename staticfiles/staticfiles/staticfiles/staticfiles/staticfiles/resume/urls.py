from django.urls import path
from .views import ResumeView
from . import views
app_name = "resume"

urlpatterns = [
    path('', views.ResumeView.as_view(), name='index'),
]
