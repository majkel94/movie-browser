import django.forms
from django.contrib.auth import get_user_model, forms


class SignUpForm(forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = django.forms.PasswordInput(
            attrs={'placeholder': 'Password'})
        self.fields['password2'].widget = django.forms.PasswordInput(
            attrs={'placeholder': 'Confirm Password'})

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username':  django.forms.TextInput(
                attrs={'placeholder': 'Username'}
            ),
        }

