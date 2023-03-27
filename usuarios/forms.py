from django import forms

class LoginForms(forms.Form):
    name_login=forms.CharField(
        label='Nome de Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                'placeholder': 'Ex.: João da Silva'
            }
        )
    )

    senha=forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                'placeholder': "Digite sua senha"
            }
        )
    )