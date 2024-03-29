from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    cate_name = models.CharField(max_length=50, unique=True, verbose_name='Category name')
    slug = models.SlugField(max_length=100, unique=True)
    desc = models.TextField(max_length=500, blank=True)
    cate_img = models.ImageField(upload_to='photos/categories', blank=True)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.cate_name 



