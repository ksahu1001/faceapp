from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    Email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "Email")

        def save(self, commit=True):
            user = super(NewUserForm, self).save(commit=False)
            user.Email = self.cleaned_data['Email']
            if commit:
                user.save()
                return user


