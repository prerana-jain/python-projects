from pickle import TRUE
from django.db import models

# Create your models here.



class Book(models.Model):
    created_at = models.DateTimeField(auto_now_add=TRUE)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    isbn = models.CharField(max_length=10,primary_key=TRUE)
    # dueDate = models.DateTimeField(auto_now_add=TRUE)

    def __str__(self):
       return(f"{self.isbn} {self.title}")




