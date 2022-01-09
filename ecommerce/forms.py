from django import forms

class ContactForm(forms.Form):
    fullname = forms.CharField(label='Your name', max_length=100, widget=forms.TextInput(attrs={
       'class': 'form-control',
       'id' : 'form_full_name',
       'placeholder' : 'Enter Name Here '}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
       'class': 'form-control',
       'id' : 'form_email',
       'placeholder' : 'Your email '}))
    content = forms.CharField( max_length=1000,widget=forms.Textarea(attrs={
       'class': 'form-control',
       'id' : 'form_content',
       'placeholder' : 'Your message '}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if "gmail.com" not in email:
            raise forms.ValidationError("Email has to been gmail.com")
            
        return email