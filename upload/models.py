from django.db import models
from django.contrib.auth.models import User
from team.models import Team,Timeline
from django.utils import timezone

class File(models.Model):
	name = models.CharField(max_length=255, blank=True)
	teamName = models.ForeignKey(Team,on_delete=models.CASCADE)
	task = models.ForeignKey(Timeline,on_delete=models.CASCADE)
	file = models.FileField(upload_to='uploads/')
	uploaded_at = models.DateTimeField(default=timezone.now)
	uploadedBy = models.ForeignKey(User,on_delete=models.CASCADE)
	approved = models.CharField(max_length=10,null=True)

	class Meta:
		unique_together = (('name','uploadedBy', 'task'),)

	def __str__(self):
		title=str(self.file.name)
		return title

class Suggestion(models.Model):
	file = models.ForeignKey(File,on_delete=models.CASCADE)
	suggestedBy = models.ForeignKey(User,on_delete=models.CASCADE)
	suggestedAt = models.DateTimeField(default=timezone.now)
	suggestion = models.CharField(max_length=2000)

	class Meta:
		unique_together = (('file','suggestedBy', 'suggestedAt'),)

	def __str__(self):
		title=str(self.file.name)+" - "+str(self.suggestedBy)+" - "+str(self.suggestedAt)
		return title

class Approval(models.Model):
	file = models.ForeignKey(File,on_delete=models.CASCADE)
	approvedBy = models.ForeignKey(User,on_delete=models.CASCADE)
	approvedAt = models.DateTimeField(auto_now_add=True)
	grade = models.CharField(max_length=10)


	class Meta:
		unique_together = (('file','approvedBy'),)

	def __str__(self):
		title=str(self.file)+" - "+str(self.approvedBy)
		return title
