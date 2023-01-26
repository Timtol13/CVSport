from django.contrib import admin
from .models import UserModel, Player, Video, Agent, Parent, Trainer, PhotoSchool

admin.site.register(UserModel)
admin.site.register(Player)
admin.site.register(Video)
admin.site.register(Agent)
admin.site.register(Parent)
admin.site.register(Trainer)
admin.site.register(PhotoSchool)