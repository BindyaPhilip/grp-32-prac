from django.contrib.auth.forms import UserCreationForm  # Import the built-in UserCreationForm for user registration
from django.contrib.auth.models import User  # Import the User model to use its fields
from django import forms  # Import Django's forms module

# Define a custom form for user registration that extends UserCreationForm
class RegisterUserForm(UserCreationForm):
    # Define an email field with a specific widget for styling
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    
    # Define fields for first name and last name with specific styling
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        # Specify the model to be used for the form
        model = User
        # Specify which fields to include in the form
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        # Call the parent class's constructor to initialize the form
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        # Add CSS class to the username, password1, and password2 fields for styling
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
