from django.core.mail import EmailMultiAlternatives

def sendWelcome(email,otp):
	subject,from_email, to = 'Welcome','zeushubsolutions@gmail.com', email
	text_content = 'Welcome to ZeusHub IT Solutions. To succesfully create a new user enter your OTP - {}'.format(otp)
	html_content = '<p>Welcome to ZeusHub IT Solutions.To succesfully create a new user enter your OTP -  <strong>{}</strong></p>'.format(otp)
	msg = EmailMultiAlternatives(subject, text_content, from_email, to)
	msg.attach_alternative(html_content, "text/html")
	msg.send()

def removedFromTeam(email,team):
	subject,from_email, to = 'Removed from Team','zeushubsolutions@gmail.com', email
	text_content = 'You have been removed from Team - {}'.format(team)
	html_content = '<p>You have been removed from Team -  <strong>{}</strong></p>'.format(team)
	msg = EmailMultiAlternatives(subject, text_content, from_email, to)
	msg.attach_alternative(html_content, "text/html")
	msg.send()

def addToTeam(email,teamMember):
	subject,from_email, to = 'Added to a Team','zeushubsolutions@gmail.com', email
	text_content = 'You have succesfully been added to Team - {}'.format(teamMember.teamName,teamMember.role)
	html_content = '<p>You have succesfully been added to <br>Team -  <strong>{}</strong><br>Role - {}</p>'.format(teamMember.teamName,teamMember.role)
	msg = EmailMultiAlternatives(subject, text_content, from_email, to)
	msg.attach_alternative(html_content, "text/html")
	msg.send()

def newTask(email,task):
	subject,from_email, to = 'New Task Assigned','zeushubsolutions@gmail.com', email
	text_content = 'New Task has been assigned in Team - {} Task - {} Task Details - {} Task deadline - {}'.format(task.teamName,task.task,task.taskDetails,task.deadline)
	html_content = '<p>New Task has been assigned in <br> Team - {}<br> Task - {}<br> Task Details - {}<br> Task deadline - {}'.format(task.teamName,task.task,task.taskDetails,task.deadline)
	msg = EmailMultiAlternatives(subject, text_content, from_email, to)
	msg.attach_alternative(html_content, "text/html")
	msg.send()

def graded(email,task):
	subject,from_email, to = 'Congratulations, your project has been graded','zeushubsolutions@gmail.com', email
	text_content = 'Your Project has been Graded Team - {} Task - {} Task Details - {} Task deadline - {} Grade - {}'.format(task.teamName,task.task,task.taskDetails,task.deadline,task.grade)
	html_content = '<p>Your Project has been Graded <br>Team - {}<br>Task - {}<br>Task Details - {}<br>Task deadline - {}<br>Grade - {}'.format(task.teamName,task.task,task.taskDetails,task.deadline,task.grade)
	msg = EmailMultiAlternatives(subject, text_content, from_email, to)
	msg.attach_alternative(html_content, "text/html")
	msg.send()
