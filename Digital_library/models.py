from django.db import models

class Books(models.Model):
    id = models.IntegerField(primary_key=True)
    Book_name = models.CharField(max_length=50)
    Author_name = models.CharField(max_length=50)
    Book_img = models.CharField(max_length=200)
    Book_pdf = models.CharField(max_length=50)

    class Meta:
        db_table = "Books"

class user(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Password = models.CharField(max_length=50)
    Author_name = models.CharField(max_length=50,null=True)

    class Meta:
        db_table = "user"

