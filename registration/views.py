from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserModel, Player, Video, Agent, Parent, Trainer, PhotoSchool, Club, Scout
from . import forms

# Create your views here.
def Registration(request):
    form = forms.DefUserForm()
    form_socc = forms.UserModelForm()
    error = ""
    if request.method == 'POST':
        form = forms.DefUserForm(request.POST)
        form_socc = forms.UserModelForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            user.save()
            login(request, user)
            error = "Success!"
            return redirect(f'/registration/advance/{user}/{request.POST.get("role")}')
        else:
            error = "Uncorrect password"
    context = {
        'form': form,
        'form_s': form_socc,
        'error': error,
    }
    return render(request, 'registration.html', context)


def Advance(request, user, role):
    if request.user.is_authenticated:
        form_user = forms.UserModelForm()
        form_player = forms.PlayerForm()
        context = {
            'user': user,
            'role': role,
            'form': form_user,
            'form_player': form_player,
        }
        usser = User.objects.get(username=user)
        if role == '1':
            form_player = forms.PlayerForm()
            form = forms.UserModelForm()
            if request.method == 'POST':
                form_player = forms.PlayerForm(request.POST)
                form = forms.UserModelForm(request.POST, request.FILES)
                if  form.is_valid() and form_player.is_valid():
                    user_main=UserModel.objects.all().create(
                        user = usser,
                        role = role or None,
                        age = form.cleaned_data['age'] or None,
                        first_name = form.cleaned_data['first_name'] or None,
                        second_name = form.cleaned_data['second_name'] or None,
                        height = form.cleaned_data['height'] or None,
                        weight =  form.cleaned_data['weight'] or None,
                        patronimyc = form.cleaned_data['patronimyc'] or None,
                        phone = form.cleaned_data['phone'] or None,
                        email = form.cleaned_data['email'] or None,
                        country = form.cleaned_data['country'] or None,
                        shengen = form.cleaned_data['shengen'] or None,
                        city = form.cleaned_data['city'] or None,
                        description = form.cleaned_data['description'] or None,
                        is_show = form.cleaned_data['is_show'] or None,
                        subscribe = form.cleaned_data['subscribe'] or None,
                        photo = request.FILES['photo'] or None,
                        sources = form.cleaned_data['sources'] or None
                    )
                    player = Player.objects.all().create(
                        user = user_main,
                        leg = form_player.cleaned_data['leg'],
                        position = form_player.cleaned_data['position']
                    )
                    video = Video.objects.all().create(
                        user = player,
                        title = form.cleaned_data['first_name'],
                        image = user_main.photo,
                        file = request.FILES['video'],
                    )
                    return redirect(f'/main/profile/{role}/{user}')
                else:
                    print(form.errors)
                    print(form_player.errors)
            return render(request, 'user_registration/registration_player.html', context)
        elif role == '2':
            form_agent = forms.AgentForm()
            context = {
                'form_agent': form_agent,
                'form': form_user,
            }
            if request.method == 'POST':
                form_agent = forms.AgentForm(request.POST, request.FILES)
                form = forms.UserModelForm(request.POST, request.FILES)
                if  form.is_valid() and form_agent.is_valid():
                    user_main=UserModel.objects.all().create(
                        user = usser,
                        role = role or None,
                        age = form.cleaned_data['age'] or None,
                        first_name = form.cleaned_data['first_name'] or None,
                        second_name = form.cleaned_data['second_name'] or None,
                        height = form.cleaned_data['height'] or None,
                        weight =  form.cleaned_data['weight'] or None,
                        patronimyc = form.cleaned_data['patronimyc'] or None,
                        phone = form.cleaned_data['phone'] or None,
                        email = form.cleaned_data['email'] or None,
                        country = form.cleaned_data['country'] or None,
                        shengen = form.cleaned_data['shengen'] or None,
                        city = form.cleaned_data['city'] or None,
                        description = form.cleaned_data['description'] or None,
                        is_show = form.cleaned_data['is_show'] or None,
                        subscribe = form.cleaned_data['subscribe'] or None,
                        photo = request.FILES['photo'] or None,
                        sources = form.cleaned_data['sources'] or None
                    )
                    agent = Agent.objects.all().create(
                        user = user_main,
                        first_name = form_agent.cleaned_data['first_name'],
                        second_name = form_agent.cleaned_data['second_name'],
                        patronimyc = form_agent.cleaned_data['patronimyc'],
                        passport = request.FILES['passport'],
                        players = None
                    )
                else:
                    print(form_agent.errors)
                return redirect(f'/main/profile/{role}/{user}')
            return render(request, 'user_registration/registration_agent.html', context)
        elif role == '3':
            form_trainer = forms.TrainerForm()
            context = {
                'form': form_user,
                'form_trainer': form_trainer,
            }
            if request.method == 'POST':
                form_trainer = forms.TrainerForm(request.POST, request.FILES)
                form = forms.UserModelForm(request.POST, request.FILES)
                if  form.is_valid() and form_trainer.is_valid():
                    user_main=UserModel.objects.all().create(
                        user = usser,
                        role = role or None,
                        age = form.cleaned_data['age'] or None,
                        first_name = form.cleaned_data['first_name'] or None,
                        second_name = form.cleaned_data['second_name'] or None,
                        height = form.cleaned_data['height'] or None,
                        weight =  form.cleaned_data['weight'] or None,
                        patronimyc = form.cleaned_data['patronimyc'] or None,
                        phone = form.cleaned_data['phone'] or None,
                        email = form.cleaned_data['email'] or None,
                        country = form.cleaned_data['country'] or None,
                        shengen = form.cleaned_data['shengen'] or None,
                        city = form.cleaned_data['city'] or None,
                        description = form.cleaned_data['description'] or None,
                        is_show = form.cleaned_data['is_show'] or None,
                        subscribe = form.cleaned_data['subscribe'] or None,
                        photo = request.FILES['photo'] or None,
                        sources = form.cleaned_data['sources'] or None
                    )
                    trainer = Trainer.objects.all().create(
                        user = user_main,
                        first_name = form_trainer.cleaned_data['first_name'],
                        second_name = form_trainer.cleaned_data['second_name'],
                        patronimyc = form_trainer.cleaned_data['patronimyc'],
                        passport = request.FILES['passport'],
                        players = None,
                        country_s=form_trainer.cleaned_data['country_s'],
                        city_s=form_trainer.cleaned_data['city_s'],
                        phone_s=form_trainer.cleaned_data['phone_s'],
                        e_mail_s=form_trainer.cleaned_data['e_mail_s'],
                    )
                    photo = PhotoSchool.objects.all().create(
                        user = trainer,
                        image = request.FILES['photo_s']
                    )
                else:
                    print(form_trainer.errors)
                return redirect(f'/main/profile/{role}/{user}')
            return render(request, 'user_registration/registration_trainer.html', context)
        elif role == '4':
            form_parent = forms.ParentForm()
            context = {
                'form': form_user,
                'form_parent': form_parent,
            }
            if request.method == 'POST':
                form_parent = forms.ParentForm(request.POST, request.FILES)
                form = forms.UserModelForm(request.POST, request.FILES)
                if  form.is_valid() and form_parent.is_valid():
                    user_main=UserModel.objects.all().create(
                        user = usser,
                        role = role or None,
                        age = form.cleaned_data['age'] or None,
                        first_name = form.cleaned_data['first_name'] or None,
                        second_name = form.cleaned_data['second_name'] or None,
                        height = form.cleaned_data['height'] or None,
                        weight =  form.cleaned_data['weight'] or None,
                        patronimyc = form.cleaned_data['patronimyc'] or None,
                        phone = form.cleaned_data['phone'] or None,
                        email = form.cleaned_data['email'] or None,
                        country = form.cleaned_data['country'] or None,
                        shengen = form.cleaned_data['shengen'] or None,
                        city = form.cleaned_data['city'] or None,
                        description = form.cleaned_data['description'] or None,
                        is_show = form.cleaned_data['is_show'] or None,
                        subscribe = form.cleaned_data['subscribe'] or None,
                        photo = request.FILES['photo'] or None,
                        sources = form.cleaned_data['sources'] or None
                    )
                    parent = Parent.objects.all().create(
                        user = user_main,
                        first_name = form_parent.cleaned_data['first_name'],
                        second_name = form_parent.cleaned_data['second_name'],
                        patronimyc = form_parent.cleaned_data['patronimyc'],
                        passport = request.FILES['passport'],
                        players = None
                    )
                else:
                    print(form_parent.errors)
                return redirect(f'/main/profile/{role}/{user}')
            return render(request, 'user_registration/registration_parent.html', context)
        elif role == '5':
            form_club = forms.ClubForm()
            context = {
                'form': form_user,
                'form_club': form_club,
            }
            if request.method == 'POST':
                form_club = forms.ClubForm(request.POST, request.FILES)
                form = forms.UserModelForm(request.POST, request.FILES)
                if  form.is_valid() and form_club.is_valid():
                    user_main=UserModel.objects.all().create(
                        user = usser,
                        role = role or None,
                        age = form.cleaned_data['age'] or None,
                        first_name = form.cleaned_data['first_name'] or None,
                        second_name = form.cleaned_data['second_name'] or None,
                        height = form.cleaned_data['height'] or None,
                        weight =  form.cleaned_data['weight'] or None,
                        patronimyc = form.cleaned_data['patronimyc'] or None,
                        phone = form.cleaned_data['phone'] or None,
                        email = form.cleaned_data['email'] or None,
                        country = form.cleaned_data['country'] or None,
                        shengen = form.cleaned_data['shengen'] or None,
                        city = form.cleaned_data['city'] or None,
                        description = form.cleaned_data['description'] or None,
                        is_show = form.cleaned_data['is_show'] or None,
                        subscribe = form.cleaned_data['subscribe'] or None,
                        photo = request.FILES['photo'] or None,
                        sources = form.cleaned_data['sources'] or None
                    )
                    club = Club.objects.all().create(
                        user = user_main,
                        first_name = form_club.cleaned_data['first_name'],
                        second_name = form_club.cleaned_data['second_name'],
                        patronimyc = form_club.cleaned_data['patronimyc'],
                        passport = request.FILES['passport'],
                        players = None,
                        schools=None,
                        school_ages=form_club.cleaned_data['school_ages']
                    )
                else:
                    print(form_parent.errors)
                return redirect(f'/main/profile/{role}/{user}')
            return render(request, 'user_registration/registration_club.html', context)
        elif role == '6':
            form_club = forms.ClubForm()
            context = {
                'form': form_user,
                'form_club': form_club,
            }
            if request.method == 'POST':
                form_scout = forms.ClubForm(request.POST, request.FILES)
                form = forms.UserModelForm(request.POST, request.FILES)
                if  form.is_valid() and form_scout.is_valid():
                    user_main=UserModel.objects.all().create(
                        user = usser,
                        role = role or None,
                        age = form.cleaned_data['age'] or None,
                        first_name = form.cleaned_data['first_name'] or None,
                        second_name = form.cleaned_data['second_name'] or None,
                        height = form.cleaned_data['height'] or None,
                        weight =  form.cleaned_data['weight'] or None,
                        patronimyc = form.cleaned_data['patronimyc'] or None,
                        phone = form.cleaned_data['phone'] or None,
                        email = form.cleaned_data['email'] or None,
                        country = form.cleaned_data['country'] or None,
                        shengen = form.cleaned_data['shengen'] or None,
                        city = form.cleaned_data['city'] or None,
                        description = form.cleaned_data['description'] or None,
                        is_show = form.cleaned_data['is_show'] or None,
                        subscribe = form.cleaned_data['subscribe'] or None,
                        photo = request.FILES['photo'] or None,
                        sources = form.cleaned_data['sources'] or None
                    )
                    club = Club.objects.all().create(
                        user = user_main,
                        first_name = form_scout.cleaned_data['first_name'],
                        second_name = form_scout.cleaned_data['second_name'],
                        patronimyc = form_scout.cleaned_data['patronimyc'],
                        passport = request.FILES['passport'],
                        players = None,
                        schools=None,
                        school_ages=form_scout.cleaned_data['school_ages']
                    )
                else:
                    print(form_scout.errors)
                return redirect(f'/main/profile/{role}/{user}')
            return render(request, 'user_registration/registration_scout.html', context)
    else:
        return redirect('/registration/')


def Login(request):
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        username = form['username'].value()
        password = form['password'].value()
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/main')
        else: 
            print("User is not found")
    context = {
        'form': form,
    }
    return render(request, 'user_registration/login.html', context)