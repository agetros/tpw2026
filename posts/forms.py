from django import forms

from .models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "categories"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].label = "Título"
        self.fields["content"].label = "Contenido de la publicación"
        self.fields["categories"].label = "Categorías"
        self.fields["title"].widget.attrs.update({"class": "form-control"})
        self.fields["content"].widget.attrs.update({"class": "form-control"})
        self.fields["categories"].widget.attrs.update({"class": "form-control"})


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].label = "Escribe tu comentario"
        self.fields["content"].widget.attrs.update({"class": "form-control", "rows": 3})
