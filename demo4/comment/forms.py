from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ['name', 'email', 'url', 'content']
        widgets = {
            'content': forms.Textarea(),
            'url': forms.URLInput()
        }
