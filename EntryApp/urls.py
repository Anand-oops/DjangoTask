from django.urls import path
from EntryApp import views

urlpatterns = [
    path('',views.homepage),
    path('save',views.save)
]