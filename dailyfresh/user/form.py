from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label='用户名')
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm', widget=forms.PasswordInput)

    def pwd_validate(self, p1, p2):
        return p1 == p2
