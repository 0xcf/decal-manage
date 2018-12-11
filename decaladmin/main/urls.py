from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lab/<str:lab>', views.lab, name='lab'),
    path('student/<str:student>', views.student, name='student'),
]
