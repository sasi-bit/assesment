from django.db import models

# Create your models here.
class mutual(models.Model):
    schema_code=models.CharField(max_length=100)
    schema_name=models.CharField(max_length=100)


    def __str__(self):
        return self.schema_name
    
