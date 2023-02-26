from django.contrib import admin
from .models import Player, Agent, Trainer, Parent, Club, Scout, PlayersVideo,UserPhoto

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'second_name', 'patronymic', 'views_count']
    def views_count(self, obj):
        return obj.views.count()
    views_count.short_description = 'Кол-во просмотров'
#admin.site.register(Player)
admin.site.register(Agent)
admin.site.register(Trainer)
admin.site.register(Parent)
admin.site.register(Club)
admin.site.register(Scout)
admin.site.register(PlayersVideo)
admin.site.register(UserPhoto)