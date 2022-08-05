from django.urls import path
from core import views
from django.contrib import admin

urlpatterns = [
    path("home/", views.index, name="index"),
    # for users or applicants
    path("user_login/", views.login_candidato, name="user_login"),
    path("signup/", views.signup, name="signup"),
    path("user_homepage/", views.candidato_inicio, name="user_homepage"),
    path("logout/", views.Logout, name="logout"),
    path("all_jobs/", views.todas_vagas, name="all_jobs"),
    path("job_detail/<int:myid>/", views.detalhe_vaga, name="job_detail"),
    path("job_apply/<int:myid>/", views.candidatar_vaga, name="job_apply"),
    # for Company
    path("company_signup/", views.empresa_signup, name="company_signup"),
    path("company_login/", views.login_empresa, name="company_login"),
    path("company_homepage/", views.empresa_inicio, name="company_homepage"),
    path("add_job/", views.adicionar_vaga, name="add_job"),
    path("job_list/", views.listar_vagas, name="job_list"),
    path("edit_job/<int:myid>/", views.editar_vaga, name="edit_job"),

    path("all_applicants/", views.todas_candidaturas, name="all_applicants"),
    # for admin
    path('admin/', admin.site.urls),

    path("delete_job/<int:myid>/", views.excluir_vaga, name="delete_job"),
]