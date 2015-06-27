from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Level


class LevelAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_labyrinth')

    def get_labyrinth(self, obj):
        return '<pre>%s</pre>' % obj.labyrinth
    get_labyrinth.short_description = _("Labyrinth")
    get_labyrinth.allow_tags = True


admin.site.register(Level, LevelAdmin)