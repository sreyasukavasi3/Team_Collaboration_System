from django.urls import path
from team import views
from django.urls import path,include

urlpatterns = [
    path('', views.index, name='team'),
    path('new', views.newTeam, name='newTeam'),
    path('<str:team>/editTimeline', views.editTimeline, name='editTimeline'),
    path('<str:team>/addMembers',views.addMembers, name='addMembers'),
    path('<str:team>/edit/', views.editTeam, name='editTeam'),
    path('<str:team>/viewTimeline', views.viewTimeline, name='viewTimeline'),
    path('<str:team>/viewMembers',views.viewMembers, name='viewMembers'),
    path('<str:team>/view/', views.viewTeam, name='viewTeam'),
    path('<str:team>/<str:task>/grade/', views.grade, name='grade'),
    path('<str:team>/<str:task>/', include('upload.urls')),
]
