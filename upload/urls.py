from django.urls import path,include
from upload import views

urlpatterns = [
    path('upload/', views.index, name='upload'),
    path('view/', views.view, name='view'),
    path('suggest/<str:filename>/<str:uploadedBy>/', views.suggest, name='suggest'),
    path('viewSuggestions/<str:filename>/<str:uploadedBy>/', views.viewSuggestions, name='viewSuggestions'),
    path('approve/<str:filename>/<str:uploadedBy>/', views.approve, name='approve'),
    path('viewApprove/<str:filename>/<str:uploadedBy>/', views.viewApprove, name='viewApprove'),
]
