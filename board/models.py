from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    title= models.CharField(max_length=100,default=None)

    def __str__(self):
        return self.name


class Board(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, null=True)

    def __str__(self):
        return self.title

class File(models.Model):
    file =models.FileField(upload_to='files/%Y/%m/%d/',null=True)
    created_date =models.DateTimeField(auto_now_add=True)
    post =models.ForeignKey(Board, null=True, on_delete=models.CASCADE)

    def delete(self, *args, **kwargs):
        self.file.delete()
        super(File,self).delete(*args, **kwargs)

    def __str__(self):
        return  self.file.name