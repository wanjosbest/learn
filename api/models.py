from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.urls import reverse

class category(models.Model):
    title=models.CharField(max_length=100,null=True)

    class Meta:
        verbose_name_plural="categories"

    def __str__(self):
      return self.title

class Post(models.Model):
    category=models.ForeignKey(category, related_name="category",null=True,on_delete=models.CASCADE)
    title=models.CharField(max_length=100,null=True)
    content=models.TextField(max_length=5000,null=True)

    image=models.ImageField(upload_to="images", null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    slug=models.SlugField(max_length=200,null=True)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("postdetails", kwargs={"slug": self.slug})   



