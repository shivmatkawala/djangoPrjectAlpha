from django.db import models

# Create your models here.

class Signup(models.Model):
    custId = models.IntegerField(auto_created=True, primary_key=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20) # Latter create a dropdown for this kind of fields
    
    class Meta:
        db_table = "signupInfo"
        
    def __str__(self):
        return f"{self.firstname}, {self.lastname}, {self.email}"
    
        