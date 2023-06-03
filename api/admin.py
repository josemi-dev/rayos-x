from django.contrib import admin

# Register your models here.
from api.models import Paciente, Medico_Responsable, Tecnico_Responsable, Equipo

admin.site.register(Paciente)
admin.site.register(Medico_Responsable)
admin.site.register(Tecnico_Responsable)
admin.site.register(Equipo)