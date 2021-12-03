from django.urls import path, include
from basic_portfolio import views

app_name = 'basic_portfolio'

urlpatterns = [
    path('university_projects/', views.uniprojects, name='uniprojects'),
    path('about/', views.about, name='about'),
    path('contact/', views.contactform, name='contactform'),
]
