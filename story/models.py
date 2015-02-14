from django.db import models

# Create your models here.


###################################
###### VENDOR TABLE 
###################################
class posts(models.Model):
	author = models.CharField(max_length = 30)
	title  = models.CharField(max_length = 30)
