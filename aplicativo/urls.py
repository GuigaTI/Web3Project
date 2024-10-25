from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('cadastro/',views.cadastrar_user, name="cadastrar_user"),
    path('usuario/',views.exibir_usuario, name="exibir_usuario"),
    path('cadastroCurso/',views.cadastrar_curso, name="cadastrar_curso"),
    path('cursos/',views.exibir_curso, name="exibir_curso"),
    #URL LOGIN
    path('login/',views.form_login, name="form_login"),
    path('dashboard/',views.dashboard, name="dashboard"),
    #URLS EDIT/DELETE
    path('editar_usuario/<int:id_usuario>',views.editar_usuario, name="editar_usuario"),
    path('excluir_usuario/<int:id_usuario>',views.excluir_usuario, name="excluir_usuario")
]