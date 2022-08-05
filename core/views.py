from django.shortcuts import render, redirect
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.http import require_POST


def index(request):
    return render(request, "index.html")


def login_candidato(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                user1 = Candidato.objects.get(user=user)
                if user1.type == "candidato":
                    login(request, user)
                    return redirect("/user_homepage")
            else:
                thank = True
                return render(request, "user_login.html", {"thank": thank})
    return render(request, "user_login.html")


def signup(request):
    if request.method == "POST":
        username = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']


        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('/signup')

        user = User.objects.create_user(first_name=first_name, last_name=last_name, email=username,password=password1,username=username)
        candidato = Candidato.objects.create(user=user, type="candidato")
        user.save()
        candidato.save()
        return render(request, "user_login.html")
    return render(request, "signup.html")


def candidato_inicio(request):
    if not request.user.is_authenticated:
        return redirect('/user_login/')
    candidato = Candidato.objects.get(user=request.user)
    if request.method == "POST":
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']


        candidato.user.username = email
        candidato.user.first_name = first_name
        candidato.user.last_name = last_name
        candidato.save()
        candidato.user.save()


        alert = True
        return render(request, "user_homepage.html", {'alert': alert})
    return render(request, "user_homepage.html", {'applicant': candidato})


def todas_vagas(request):
    vagas = Vaga.objects.all().order_by()
    candidato = Candidato.objects.get(user=request.user)
    apply = Candidatura.objects.filter(candidato=candidato)
    data = []
    for i in apply:
        data.append(i.vaga)
    return render(request, "all_jobs.html", {'vagas':vagas, 'data':data})



def detalhe_vaga(request, myid):
    vaga = Vaga.objects.get(id=myid)
    return render(request, "job_detail.html", {'vaga':vaga})


def candidatar_vaga(request, myid):

    if not request.user.is_authenticated:
        return redirect("/user_login")
    candidato = Candidato.objects.get(user=request.user)
    vaga = Vaga.objects.get(id=myid)

    if request.method == "POST":
        salario= request.POST['salario']
        experiencia= request.POST['experiencia']
        escolaridade= request.POST['escolaridade']
        Candidatura.objects.create(vaga=vaga, candidato=candidato,pretencao_salarial=salario,experiencia=experiencia,escolaridade=escolaridade,empresa=vaga.empresa)
        alert=True
        return render(request, "job_apply.html", {'alert':alert})
    return render(request, "job_apply.html", {'vaga':vaga})


def editar_vaga(request, myid):
    if not request.user.is_authenticated:
        return redirect("/company_login")
    vaga = Vaga.objects.get(id=myid)
    if request.method == "POST":
        title = request.POST['job_title']
        salary = request.POST['salary']
        skills = request.POST['skills']
        escolaridade = request.POST['escolaridade']

        vaga.nome = title
        vaga.faixa_salarial = salary
        vaga.requisitos = skills
        vaga.escolaridade_min = escolaridade

        vaga.save()

        alert = True
        return render(request, "edit_job.html", {'alert':alert})
    return render(request, "edit_job.html", {'vaga':vaga})


def login_empresa(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)


        if user is not None:
            user1 = Empresa.objects.get(user=user)
            print(user1.type)
            if user1.type == "empresa":
                login(request, user)
                return redirect("/company_homepage")
        else:
            alert = True
            return render(request, "company_login.html", {"alert": alert})
    return render(request, "company_login.html")


def empresa_signup(request):
    if request.method == "POST":
        username= request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']


        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('/signup')

        user = User.objects.create_user(username=username,email=username,
                                        password=password1)
        empresa = Empresa.objects.create(user=user,
                                         type="empresa")
        user.save()
        empresa.save()
        return render(request, "company_login.html")
    return render(request, "company_signup.html")


def empresa_inicio(request):
    if not request.user.is_authenticated:
        return redirect("/company_login")
    empresa = Empresa.objects.get(user=request.user)
    if request.method == "POST":
        email = request.POST['email']



        empresa.user.email = email


        empresa.save()
        empresa.user.save()


        alert = True
        return render(request, "company_homepage.html", {'alert': alert})
    return render(request, "company_homepage.html", {'empresa': empresa})


def adicionar_vaga(request):
    if not request.user.is_authenticated:
        return redirect("/company_login")
    if request.method == "POST":
        title = request.POST['job_title']
        salary = request.POST['salary']
        skills = request.POST['skills']
        escolaridade = request.POST['escolaridade']
        user = request.user
        empresa = Empresa.objects.get(user=user)
        vaga= Vaga.objects.create(empresa=empresa, nome=title,faixa_salarial=salary, requisitos=skills, escolaridade_min=escolaridade)
        vaga.save()
        alert = True
        return render(request, "add_job.html", {'alert':alert})
    return render(request, "add_job.html")


def listar_vagas(request):
    if not request.user.is_authenticated:
        return redirect("/company_login")
    empresas = Empresa.objects.get(user=request.user)
    vagas = Vaga.objects.filter(empresa=empresas)
    return render(request, "job_list.html", {'vagas':vagas})


def todas_candidaturas(request):
    empresa = Empresa.objects.get(user=request.user)
    candidatura = Candidatura.objects.filter(empresa=empresa)
    return render(request, "all_applicants.html", {'candidatura':candidatura})

def Logout(request):
    logout(request)
    return redirect('/home')




def excluir_vaga(request,myid):
    if not request.user.is_authenticated:
        return redirect("/company_login")
    vaga = Vaga.objects.filter(id=myid)
    vaga.delete()
    return redirect("/job_list")