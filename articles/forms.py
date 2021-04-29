from django import forms

from .models import Articles


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Articles
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['autofocus'] = True
        self.fields['slug'].widget.attrs['placeholder'] = 'ending of the link'
        self.fields['intro'].widget.attrs['placeholder'] = '100 - 400 characters'
        self.fields['article_content'].widget.attrs['placeholder'] = 'min 250 characters'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'add-article-form-field'
