from django import forms

class EmailSender(forms.Form):
    email = forms.EmailField()

    def __str__(self):
        return self.email

