from django import forms
from aplicativo.models import Usuario
from aplicativo.models import Curso

class FormCadastroUser(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nome', 'email', 'senha') 
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'email': forms.EmailInput(attrs={'placeholder': 'usuario@email.com', 'class': 'form-control form-control-lg'}),
            'senha': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
        }

class FormCadastroCurso(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ('nome','autor','duracao','preco')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'autor': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'duracao': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control form-control-lg','step':'0.01'})
    }
        
class FormLogin(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('email','senha')
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'usuario@email.com', 'class': 'form-control form-control-lg'}),
            'senha': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'})
        }
