from datetime import timedelta
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from aplicativo.form_cadastro_user import FormCadastroUser,FormCadastroCurso,FormLogin,FormAlterarSenha,FotoForm
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from aplicativo.models import Usuario,Curso,Foto
from django.contrib.auth import get_user_model,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.template import loader




# Create your views here.
def home(request):
    return render(request,"index.html")


def cadastrar_user(request):
    novo_user = FormCadastroUser(request.POST, request.FILES)

    if request.method == 'POST':
        email = request.POST.get('email')
        # Verificar se o e-mail já existe
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, "E-mail já cadastrado.")
        elif novo_user.is_valid():
            user = novo_user.save(commit=False)
            # Criptografar a senha usando make_password
            user.senha = make_password(novo_user.cleaned_data['senha'])
            user.save()
            messages.success(request, "Usuário cadastrado com sucesso")
            return redirect('home')
    
    context = {'form': novo_user}
    return render(request, "cadastro.html", context)

def exibir_usuario(request):
   usuarios = Usuario.objects.all().values()

   context = {
      'dados' : usuarios
   }
   return render(request,'usuarios.html',context)

def cadastrar_curso(request):
    if request.method == 'POST':
        # Instanciando o formulário com os dados do POST e o arquivo da imagem
        form = FormCadastroCurso(request.POST, request.FILES)
        
        # Verificando se o formulário é válido
        if form.is_valid():
            form.save()  # Salvando o novo curso no banco de dados
            messages.success(request, "Curso cadastrado com sucesso!")  # Mensagem de sucesso
            return redirect('home')  # Redireciona para a página inicial
    else:
        form = FormCadastroCurso()  # Formulário vazio em caso de GET

    return render(request, 'cadastroCurso.html', {'form': form})

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
            request.session.set_expiry(timedelta(seconds=1800))
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
    if 'email' not in request.session:
        return redirect('form_login')

    # Obtém o usuário logado
    usuario_logado = Usuario.objects.get(email=request.session['email'])

    context = {
        'usuario': usuario_logado,
        'email': request.session['email'],
    }

    template = loader.get_template("dashboard.html")
    return HttpResponse(template.render(context))


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

def redefinir_senha(request, id_usuario):
    user = get_object_or_404(Usuario, id=id_usuario)  # Obtém o usuário pelo ID
    if request.method == 'POST':
        form = FormAlterarSenha(user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Mantém o usuário logado
            messages.success(request, 'Senha alterada com sucesso!')
            return redirect('dashboard')  # Redirecione para a página desejada
    else:
        form = FormAlterarSenha(user)

    return render(request, 'redefinir_senha.html', {'form': form, 'user': user})

def criar_foto(request):
    if request.method == 'POST':
        form = FotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('galeria')
    else:
        form = FotoForm()  # Esse formulário será exibido em uma requisição GET

    return render(request, 'criar_foto.html', {'form': form})

def pagina_sucesso(request):
    return render(request, 'pagina_sucesso.html')

#Mostra as fotos
def mostrar_fotos(request):
    fotos = Foto.objects.all()

    context = {
        'dados': fotos  
        }

    return render(request, "galeria.html", context)

