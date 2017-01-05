from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(label='nickname', max_length=16, error_messages={
        'required': 'plz type ur nickname',
        'max_length': 'too long'
    })
 
    email = forms.EmailField(label='email', error_messages={
        'required': 'plz type ur email',
        'invalid': 'format warn'
    })
 
    content = forms.CharField(label='content', error_messages={
        'required': 'plz type ur content',
        'max_length': 'too long'
    })
