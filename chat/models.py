from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from team.models import Team

class DirectMessage(models.Model):
	sentFrom = models.ForeignKey(User,on_delete=models.CASCADE,related_name='directFrom')
	sentTo   = models.ForeignKey(User,on_delete=models.CASCADE,related_name='directTo')
	message  = models.CharField(max_length=200)
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
   		title=str(self.created_date)+" "+str(self.sentFrom)+" "+str(self.sentTo)
   		return title

class GroupMessage(models.Model):
	sentFrom = models.ForeignKey(User,on_delete=models.CASCADE,related_name='groupFrom')
	sentTo   = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='groupTo')
	message  = models.CharField(max_length=200)
	created_date = models.DateTimeField(default=timezone.now)

	# class Meta:
 #        order_with_respect_to = '-created_date'

	def __str__(self):
		title=str(self.created_date)+" "+str(self.sentFrom)+" "+str(self.sentTo)
		return title
