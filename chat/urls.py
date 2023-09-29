from django.urls import path
from chat import views


urlpatterns = [
	path('', views.index, name='chat'),
	path('continueChat/<str:name>', views.continueChat, name='continueChat'),
	path('continueGroupChat/<str:name>', views.continueGroupChat, name='continueGroupChat'),
	path('chatNow', views.chatNow, name='chatNow'),
	path('groupChatNow', views.groupChatNow, name='groupChatNow'),
]