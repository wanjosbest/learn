from django import forms
from api.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=("category","title","content","slug",)


