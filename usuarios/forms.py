from django import forms

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label="Nome de Login", 
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: Paulo Gomes"
            }
        )
    )
    senha=forms.CharField(
        label="Senha", 
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )

class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label="Nome de Cadastro", 
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: Paulo Gomes"
            }
        )
    )

    email=forms.EmailField(
        label="Email", 
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: paulogomes@gmail.com"
            }
        )
    )

    senha1=forms.CharField(
        label="Senha", 
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )

    senha2=forms.CharField(
        label="Confirme sua Senha", 
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha novamente"
            }
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")   

        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("Nome de cadastro não pode conter espaços")
            else:
                return nome
            
    def clean_senha2(self):
        senha1 = self.cleaned_data.get("senha1")
        senha2 = self.cleaned_data.get("senha2")
        
        if senha1 and senha2:
            if senha1 != senha2:
                raise forms.ValidationError("As senhas não considem")
            else:
                return senha2