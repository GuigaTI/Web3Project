from django.conf import settings
from django.conf.urls.static import static
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
    path('excluir_usuario/<int:id_usuario>',views.excluir_usuario, name="excluir_usuario"),
    path("criaFoto/", views.criar_foto, name="criar_foto"),
    path('succes/', views.pagina_sucesso, name="pagina_sucesso"),
    path('redefinir_senha/<int:id_usuario>/',views.redefinir_senha, name="redefinir_senha"),
    path('galeria/', views.mostrar_fotos, name="galeria"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)