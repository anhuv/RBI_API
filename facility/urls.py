from django.urls import path

from . import views
from .views import ListCreateFacilityView, UpdateDeleteFacilityView 

urlpatterns = [
    path('facility', views.ListCreateFacilityView.as_view()),
    path('facility/<int:pk>', views.UpdateDeleteFacilityView.as_view()),
]

