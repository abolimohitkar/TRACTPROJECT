from django.db import models

class Register(models.Model):
    name=models.CharField(max_length=200,primary_key=True)
    password=models.CharField(max_length=200)
    mobno=models.IntegerField()
    email=models.CharField(max_length=200)


    def __str__(self):
        return "{},{},{}".format(self.name,self.password,self.mobno,self.email)

    class Meta:
        db_table='user'    

class Data(models.Model):
    name=models.CharField(max_length=200,primary_key=True)
    password=models.CharField(max_length=200)
    mobno=models.IntegerField()
    email=models.CharField(max_length=200)
    # pickup=models.CharField(max_length=200)
    # drop=models.CharField(max_length=200)
    # area=models.CharField(max_length=200)
    

    def __str__(self):
        return"{},{},{},{},{},{}".format(self.name,self.password,self.mobno,self.email)

    class Meta:
        db_table="data"


# class Score(models.Model):
#     name=models.CharField(max_length=45,primary_key=True)
#     subject=models.CharField(max_length=200)
#     score=models.IntegerField()
#     def __str__(self):
#         return"{},{},{}".format(self.name,self.subject,self.score)
 
#     class Meta:
#         db_table='score'
