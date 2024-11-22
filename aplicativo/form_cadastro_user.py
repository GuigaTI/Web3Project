from django import forms
from aplicativo.models import Usuario
from aplicativo.models import Curso
from aplicativo.models import Foto
from django.contrib.auth.forms import PasswordChangeForm


class FormCadastroUser(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nome', 'email', 'senha','imagem') 
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'email': forms.EmailInput(attrs={'placeholder': 'usuario@email.com', 'class': 'form-control form-control-lg'}),
            'senha': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}),
            'imagem': forms.FileInput(attrs={'accept': 'image/*'})
        }

class FormCadastroCurso(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ('nome','autor','duracao','preco','imagem')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'autor': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'duracao': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control form-control-lg','step':'0.01'}),
            'imagem': forms.FileInput(attrs={'accept': 'image/*'})
    }
        
class FormLogin(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('email','senha')
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'usuario@email.com', 'class': 'form-control form-control-lg'}),
            'senha': forms.PasswordInput(attrs={'class': 'form-control form-control-lg'})
        }

class FotoForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ['titulo', 'imagem']

        widgets = {
                'imagem': forms.FileInput(attrs={'accept': 'image/*'})
                }
        
class FormAlterarSenha(PasswordChangeForm):
    def __init__(self, user=None, *args, **kwargs):
        super(FormAlterarSenha, self).__init__(user, *args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Senha Atual'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nova Senha'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirme Nova Senha'})