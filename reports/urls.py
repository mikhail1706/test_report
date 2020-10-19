from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.ReportCreate.as_view(), name='report_create'),
]
