from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from .models import Post,Curs

class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

admin.site.register(Curs)
admin.site.register(Post, PostAdmin)