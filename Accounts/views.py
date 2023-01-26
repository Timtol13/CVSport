from django.shortcuts import render
from registration.models import UserModel, Player, Video, Trainer, UserModel, Agent, Parent
from django.contrib.auth.models import User
from fuzzywuzzy import fuzz 
from CV_Sport.settings import BASE_DIR

# Create your views here.
def Main(request):
    videos = Video.objects.all()

    context = {
        'user': request.user,
        'videos': videos
    }
    return render(request, 'profile/main.html', context)

def profile(request, role, user):
    profile = None
    videos = None
    usser = User.objects.get(username=request.user.username)
    usermodel = UserModel.objects.get(user=usser)
    if role == '1':
        profile = Player.objects.get(user=usermodel)
        videos = Video.objects.filter(user=profile)
    elif role == '2':
        profile = Agent.objects.get(user=usermodel)
        if request.method == "POST":
            players = Player.objects.all()
            player_data = request.POST.getlist('player_data')
            for i in players:
                print(i.user.second_name)
                if fuzz.ratio(i.user.second_name, player_data[0]) > 80 and fuzz.ratio(i.user.first_name, player_data[1]) > 80 and fuzz.ratio(i.user.patronimyc, player_data[2])  > 80:
                    pass
    elif role == '3':
        profile =  Trainer.objects.get(user=usermodel)
    elif role == '4':
        profile = Parent.objects.get(user=usermodel)
    else:
        profile = None

    context = {
        'role': role,
        'profile': profile,
        'videos': videos,
    }
    return render(request, 'profile/profile.html', context)