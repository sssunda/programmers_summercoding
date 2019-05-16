from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields=('title', 'text', 'due_chk', 'due_date')
        due_date = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d', attrs={'class': 'datepicker'}),
        input_formats=('%Y-%m-%d', )
        )