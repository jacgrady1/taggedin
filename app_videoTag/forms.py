from django import forms
from string import lower
from django.contrib.auth.models import User

from models import *
from forms import *



#==========================================
class Photo(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture']


class Basic(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture']

class PasswordForm(forms.Form):
    password1 = forms.CharField(max_length = 200, 
                                label='Password', 
                                widget = forms.PasswordInput())
    password2 = forms.CharField(max_length = 200, 
                                label='Confirm password',  
                                widget = forms.PasswordInput())

    def clean(self):
        # Calls our parent (forms.Form) .clean function, gets a dictionary
        # of cleaned data as a result
        cleaned_data = super(RegistrationForm, self).clean()

        # Confirms that the two password fields match
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords did not match.")

        # We must return the cleaned data we got from our parent.
        return cleaned_data



class RegistrationForm(forms.Form):
    username = forms.CharField(max_length = 20)
    email = forms.EmailField(max_length=200)
    password1 = forms.CharField(max_length = 200, 
                                label='Password', 
                                widget = forms.PasswordInput())
    password2 = forms.CharField(max_length = 200, 
                                label='Confirm password',  
                                widget = forms.PasswordInput())


    # Customizes form validation for properties that apply to more
    # than one field.  Overrides the forms.Form.clean function.
    def clean(self):
        # Calls our parent (forms.Form) .clean function, gets a dictionary
        # of cleaned data as a result
        cleaned_data = super(RegistrationForm, self).clean()

        # Confirms that the two password fields match
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords did not match.")

        # We must return the cleaned data we got from our parent.
        return cleaned_data


    # Customizes form validation for the username field.
    def clean_username(self):
        # Confirms that the username is not already present in the
        # User model database.
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__exact=username):
            raise forms.ValidationError("Username is already taken.")

        # We must return the cleaned data we got from the cleaned_data
        # dictionary
        return username







class ChangeForm(forms.Form):
    oldpassword = forms.CharField(max_length = 20,
                                label='oldpassword',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'required':'true'}))
    password1 = forms.CharField(max_length = 20, 
                                label='Password', 
                                widget=forms.PasswordInput(attrs={'class': 'form-control','required':'true'}))
    password2 = forms.CharField(max_length = 20, 
                                label='Confirm password',  
                                widget=forms.PasswordInput(attrs={'class': 'form-control','required':'true'}))

    # Customizes form validation for properties that apply to more
    # than one field.  Overrides the forms.Form.clean function.
    def clean(self):
        # Calls our parent (forms.Form) .clean function, gets a dictionary
        # of cleaned data as a result
        cleaned_data = super(ChangeForm, self).clean()

        # Confirms that the two password fields match
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords did not match.")

        # We must return the cleaned data we got from our parent.
        return cleaned_data


class ForgetForm(forms.Form):
    username = forms.EmailField(max_length = 20,
                                label='Email(Username)',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'required':'true'}))

    # Customizes form validation for properties that apply to more
    # than one field.  Overrides the forms.Form.clean function.
    def clean_username(self):
        # Confirms that the username is not already present in the
        # User model database.
        username = self.cleaned_data.get('username')
        if not User.objects.filter(username__exact=username):
            raise forms.ValidationError("Username does not exist.")

        # We must return the cleaned data we got from the cleaned_data
        # dictionary
        return username


class GetBackForm(forms.Form):

    password1 = forms.CharField(max_length = 20, 
                                label='Password', 
                                widget=forms.PasswordInput(attrs={'class': 'form-control','required':'true'}))
    password2 = forms.CharField(max_length = 20, 
                                label='Confirm password',  
                                widget=forms.PasswordInput(attrs={'class': 'form-control','required':'true'}))

    # Customizes form validation for properties that apply to more
    # than one field.  Overrides the forms.Form.clean function.
    def clean(self):
        # Calls our parent (forms.Form) .clean function, gets a dictionary
        # of cleaned data as a result
        cleaned_data = super(GetBackForm, self).clean()

        # Confirms that the two password fields match
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords did not match.")

        # We must return the cleaned data we got from our parent.
        return cleaned_data


class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ['text','description','docfile']
        widgets = {
        'discription': forms.Textarea(attrs={'class':"form-control" ,'rows':"3",'placeholder':"description"}),
        'docfile' : forms.FileInput() }

    
class TaggingForm(forms.ModelForm):
    class Meta:
        model = Tagging
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class':"form-control",'rows':"1" ,'placeholder':"tagtag..."}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', )
        widgets = {'picture' : forms.FileInput() }  





    


        
