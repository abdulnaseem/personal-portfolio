from django import forms
from basic_portfolio.models import Contact

class NewContact(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea, required=True)
    class Meta:
        model = Contact
        fields = ('email', 'subject', 'message')
