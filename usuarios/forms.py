from django import forms

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label='Nome Usuario',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': "Usuario"
            }
        )
    )
    senha=forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(),
    )


class CadastroForms(forms.Form):
    foto_perfil = forms.ImageField(
        label='Foto de Perfil',
        required=False
    )
    nome_usuario=forms.CharField(
        label='Nome Usuario',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': "Usuario"
            }
        )
    )
    sobrenome=forms.CharField(
        label='Sobrenome',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': "Sobrenome"
            }
        )
    )
    email=forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'placeholder': "Ex: nome@email.com"
            }
        )
    )
    senha=forms.CharField(
        label='Senha',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': "Digite a senha"
            }
        )
    )
    senha_check=forms.CharField(
        label='Nome Usuario',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': "Confirmar Senha "
            }
        )
    )
