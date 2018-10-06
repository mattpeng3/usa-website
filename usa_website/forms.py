from django import forms

from .models import Blog

class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'body',)

class AttendanceForm(forms.Form):
    post = forms.CharField(max_length=12, label="Berkeley SID")
