from .models import Comment, Post, Category
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False, empty_label="Select a category")

    class Meta:
        model = Post
        fields = ['title', 'content', 'featured_image', 'excerpt', 'status','category']
        