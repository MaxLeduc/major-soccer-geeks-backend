from django.contrib import admin
from .models import Club, Position, Player

# Register your models here.


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'base_salary',
                    'guaranteed_compensation')


class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ClubAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Player, PlayerAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Club, ClubAdmin)
