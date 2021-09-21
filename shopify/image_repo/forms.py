from django import forms
from .models import Repository
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class ImageForm(forms.ModelForm):
    class Meta:
        model = Repository
        fields = ['imageName', 'image', ]
        labels = {
            "imageName": "Image Name",
            "image": "Image",
        }

        widgets = {
            'imageName': forms.TextInput(attrs={'class': 'form-control col-4'}),
        }


class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }

    password1 = forms.CharField(label=_("Password"),
                                widget=forms.PasswordInput(attrs={'class': 'form-control col-3'}))

    password2 = forms.CharField(label=_("Password Confirmation"),
                                widget=forms.PasswordInput(attrs={'class': 'form-control col-3'}),
                                help_text=_("Enter the same password as above, for verification."))

    class Meta:
        model = User
        fields = ("username", "first_name",)

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control col-3'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control col-3'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "Name"

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        validate_password(password1)
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
