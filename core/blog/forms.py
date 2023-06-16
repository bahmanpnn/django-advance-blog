from django import forms
from .models import Post


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "auhtor",
            "title",
            "content",
            "status",
            "category",
            "published_date",
        ]
        # exclude=['image','created_date','updated_date']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            # "auhtor",
            "category",
            "title",
            "content",
            "status",
            "published_date",
        ]
