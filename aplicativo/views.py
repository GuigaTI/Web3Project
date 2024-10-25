from datetime import timedelta
from django.shortcuts import render
from aplicativo.form_cadastro_user import FormCadastroUser,FormCadastroCurso,FormLogin
from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from aplicativo.models import Usuario,Curso


# Create your views here.
def home(request):
    return render(request,"index.html")


def cadastrar_user(request):
  novo_user = FormCadastroUser(request.POST or None)

  #salvar usuario
  if request.POST:
     if novo_user.is_valid():
        email = novo_user.cleaned_data['email']
        senha = novo_user.cleaned_data['senha'] 

        if Usuario.objects.filter(email=email).exists():
         messages.error(request,"Usuario já existente")
         return redirect('cadastrar_user')

        novo_user.instance.senha = make_password(senha) 
        novo_user.save()
        messages.success(request,"Usuario criado com sucesso")
        return redirect('home')
  
  context = {
   'form' : novo_user
  }
  
  return render(request,'cadastro.html',context)

def exibir_usuario(request):
   usuarios = Usuario.objects.all().values()

   context = {
      'dados' : usuarios
   }
   return render(request,'usuarios.html',context)

def cadastrar_curso(request):
  novo_curso = FormCadastroCurso(request.POST or None)

  #salvar curso
  if request.POST:
     if novo_curso.is_valid():
        novo_curso.save()
        messages.success(request,"Curso criado com sucesso")
        return redirect('home')
  
  context = {
   'form' : novo_curso
  }
  
  return render(request,'cadastroCurso.html',context)

def exibir_curso(request):
   cursos = Curso.objects.all().values()

   context = {
      'dados' : cursos
   }
   return render(request,'cursos.html',context)

def form_login(request):
   formLogin = FormLogin(request.POST or None)
   if request.POST:
      _email = request.POST['email']
      _senha = request.POST['senha']
      
      try:
         usuario = Usuario.objects.get(email = _email)      
         if check_password(_senha,usuario.senha):
            #Define o tempo da sessao em segundos
            request.session.set_expiry(timedelta(seconds=60))
            #Variacel de sessao
            request.session['email'] = _email
            messages.success(request,"Usuario logado com sucesso")
            return redirect('dashboard')
         else:
            messages.error("Senha incorreta")
      except:
            messages.error(request, 'Usuario não encontrado!')
            return redirect('form_login')

   context = {
      'form' : formLogin
   }
   return render(request,'form-login.html',context)

def dashboard(request):
   #Recupera a variavel de sessao

   if 'email' not in request.session:
      return redirect('home')

   email = request.session.get('email')
   context = {
      'username' : email
   }
   return render(request,'dashboard.html',context)

def editar_usuario(request,id_usuario):
   usuario = Usuario.objects.get(id=id_usuario)
   form = FormCadastroUser(request.POST or None,instance=usuario)
   if request.POST:
      if form.is_valid():
         form.save()
         return redirect('exibir_usuario')
   context = {
      'form' : form
   }

   return render(request,'editar_usuario.html',context)

def excluir_usuario(request,id_usuario):
   usuario = Usuario.objects.get(id=id_usuario)
   usuario.delete()
   return redirect('exibir_usuario')