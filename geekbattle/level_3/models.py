from django.db import models


class Question(models.Model):
    description = models.TextField()
    def __str__(self):
        return str(self.id)
    class Meta:
    	    db_table = 'question2'
    	    verbose_name = 'Question'
    	    verbose_name_plural = 'Questions'

