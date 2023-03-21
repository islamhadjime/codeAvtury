from django import forms
from .models import Comment



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Напишите ваша Имя'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Напишите ваша Mail'}),
            'body': forms.Textarea(attrs={'placeholder': 'Текст комментарии'}),

        }

