from pyexpat import model
from statistics import mode
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager




class Curs(models.Model):
    curs_name = models.CharField(max_length=200,verbose_name="названия курсы")


    def __str__(self):
        return self.curs_name


    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

        
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')




class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=200,verbose_name="Имя Поста")
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')

    img  = models.ImageField(upload_to="Posts/Img",blank=True,null=True,verbose_name="Изображения Поста")
    body = RichTextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    curs_name = models.ForeignKey(Curs,on_delete=models.CASCADE)
    file      = models.FileField(upload_to="Post/Fil",blank=True,null=True,verbose_name="Файл")
    object = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()



    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ('-publish',)

    def __str__(self):
        return "Дата: {}, Названия: {}".format(self.created,self.title)



    def get_absolute_url(self):
        return reverse("detail_post", kwargs={"pk": self.pk})


class Comment(models.Model): 
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80) 
    email = models.EmailField() 
    body = models.TextField() 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    active = models.BooleanField(default=True) 
 
    class Meta: 
        ordering = ('created',) 
 
    def __str__(self): 
        return 'Comment by {} on {}'.format(self.name, self.post)



