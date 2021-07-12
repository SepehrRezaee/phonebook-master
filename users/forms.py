from django import forms


class LoginForm(forms.Form):
    """
    The login form
    """
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(LoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
