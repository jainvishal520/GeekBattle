from django.db import models
from django.contrib.auth.models import User
from UserAccount.models import UserModel
# Create your models here.

class Question(models.Model):
    description = models.TextField()
    choice_1 = models.TextField()
    choice_2 = models.TextField()
    choice_3 = models.TextField()
    choice_4 = models.TextField()
    answer = models.IntegerField(default=0)	
    def __str__(self):
        return str(self.id)
    class Meta:
        db_table = 'question'
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class Answer(models.Model):
    user = models.ForeignKey(User)
    answer_list = models.CommaSeparatedIntegerField(max_length=255)
    active_status_list = models.CommaSeparatedIntegerField(max_length=255)
    s1 = models.IntegerField(default=-1)
    s2 = models.IntegerField(default=-1)
    s3 = models.IntegerField(default=-1)				
    def __str__(self):
        return str(self.user)
    class Meta:
    	    db_table = 'answer'
    	    verbose_name = 'Answer'
    	    verbose_name_plural = 'Answers'


institute_option=(('Amity University Student','Amitian'),('Other University Student','Non-Amitian'))
gender_option=(('male','Male'),('female','Female'))
class user_details(models.Model):
	detail_status=models.BooleanField(default=False)
	user=models.ForeignKey(User)
	institute_filter=models.CharField(max_length=30,choices=institute_option)
	institute=models.CharField(max_length=1000)
	prog=models.CharField(max_length=100)
	address=models.CharField(max_length=1000)
	city=models.CharField(max_length=50)
	state=models.CharField(max_length=50)
	#country=models.CharField(max_length=1000)
	name=models.CharField(max_length=100)
	gender=models.CharField(max_length=6,choices=gender_option)
	"""dob_day=models.IntegerField()
	dob_month=models.IntegerField()
	dob_year=models.IntegerField()"""
	#dob=models.CharField(max_length=11)
	phone=models.CharField(max_length=20,blank=True)
	mobile=models.CharField(max_length=15)
	email=models.EmailField()
	

	def __unicode__(self):
		return str(self.user)
