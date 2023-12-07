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
        widget=forms.PasswordInput(
            attrs={
                'placeholder': "********"
            }
        ),
    )


class CadastroForms(forms.Form):
    foto_perfil = forms.ImageField(
        label='Foto de Perfil',
        required=False,
        widget=forms.FileInput(
            attrs={
                'class': 'selecionar-arquivo-imagem'
            }
        )
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
        label='Confirmar Senha',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': "Confirmar Senha"
            }
        )
    )

    # Validar nome de cadastro sem espaços
    def clean_nome_usuario(self):
        nome = self.cleaned_data.get('nome_usuario')

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('O nome usuario não pode ter espaços')
            else:
                return nome

    # Validar igualdade de senha de cadastro
    def clean_senha_check(self):
        senha = self.cleaned_data.get('senha')
        senha_check = self.cleaned_data.get('senha_check')

        if senha and senha_check:
            if senha != senha_check:
                raise forms.ValidationError('Senhas não iguais')
            else:
                return senha_check