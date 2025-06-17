from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(
                attrs={'rows': 3, 'placeholder': 'Add your comment here.'}
            ),
        }
        labels = {
            'text': '',
        }

        def clean_text(self):
            text = self.cleaned_data.get('text', '').strip()
            if not text:
                raise forms.ValidationError("Comment can't be empty.")
            return text
