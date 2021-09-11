from django.db import models

# Create your models here.
class Info(models.Model):
    fname= models.CharField(max_length=100)
    lname= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    number= models.CharField(max_length=100)
    position=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    jobtype=models.CharField(max_length=100)
    sdate=models.CharField(max_length=100)

    def __str__(self):
        return self.fname



class answers(models.Model):
    name= models.CharField(max_length=100)
    answer1=models.CharField(max_length=1000)
    answer2=models.CharField(max_length=1000)
    answer3=models.CharField(max_length=1000)

class markslist(models.Model):
    name= models.CharField(max_length=100)
    commentrate=models.FloatField(max_length=7)
    resumematchper=models.FloatField(max_length=7)
    botscore=models.FloatField(max_length=7)
    avg=models.FloatField(max_length=7)
    result={"Name":name , "commentrate":commentrate , "resumematchper":resumematchper , "botscore":botscore , "avg":avg}
    
    def dic(self):
        print(self.result)
        return self.avg
