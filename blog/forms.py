from django import forms
from .models import BlogModel    

class CreateForm(forms.ModelForm):
    author = forms.CharField(label='Your name', max_length=100)
    title = forms.CharField(label='Your Title', max_length=200)
    post = forms.CharField(label='Add Post',widget=forms.Textarea(attrs={'class':'post', 'id':'post'}))
    class Meta:
        model = BlogModel
        fields = '__all__'

    def clean_author(self):
        author = self.cleaned_data['author'].upper()
        return author

