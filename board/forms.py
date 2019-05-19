from django import forms
from django.core.exceptions import ValidationError
from .models import Post
import re


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'due_chk', 'due_date', 'complete_chk')        
        due_date = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d', attrs={'class': 'datepicker'}),
                                   input_formats=('%Y-%m-%d', )
                                   )


    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("due_chk"):
            value = str(cleaned_data.get("due_date"))
            if not re.match(r'\d{4}-\d{2}-\d{2}', value):
                raise ValidationError("날짜형식을 맞춰주세요. YYYY-MM-DD")
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'todo_title_edit'})
       
        
            
            
  