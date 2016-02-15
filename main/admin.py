from django.contrib import admin
from main.models import KarniPiLog


class KarniPiLogAdmin(admin.ModelAdmin):
    fields = ['type',
              'message']

admin.site.register(KarniPiLog, KarniPiLogAdmin)
