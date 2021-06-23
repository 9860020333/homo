from django import forms


class EmailForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={"name": "email", "id": "email", "type": "email", "placeholder": "Email"}))
    subject = forms.CharField(max_length=254, widget=forms.TextInput(attrs={"name": "subject", "id": "subject","placeholder": "Enter Subject"}))
    body = forms.CharField(widget=forms.Textarea(attrs={"name": "message", "id": "message","onblur": "this.placeholder = 'Enter Message'", "placeholder": " Enter Body"}))
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"name": "name", "id": "name","placeholder": "Enter your name"}))

    def __str__(self):
        return self.Email
