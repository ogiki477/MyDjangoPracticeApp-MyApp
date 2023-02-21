from django import forms
from blogApp.models import Post,Comment

class PostForm(forms.ModelForm):

    class meta():
        model = Post
        fields = ('author','title','text')

        widgets = {

            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
         } 






class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author','text')

        widgets = {

            'author':forms.TextInput(attrs={'class':"textinputclass"}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})

        }




