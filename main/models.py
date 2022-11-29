from django.db import models
import time
# Create your models here.

class Covid19(models):
    State_Name = models.CharField(max_length=15) 
    Date_of_Record = models.DateField(default=time.now) 
    No_of_Samples  = models.IntegerField()
    No_of_Deaths   = models.IntegerField() 
    No_of_Positive = models.IntegerField() 
    No_of_Negative = models.IntegerField() 
    No_of_Discharge= models.IntegerField() 