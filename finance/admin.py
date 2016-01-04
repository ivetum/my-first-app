from django.contrib import admin
from .models import *

admin.site.register(Transaction)
admin.site.register(Event)
admin.site.register(Project)
admin.site.register(ProjectGroup)
admin.site.register(Entity)
admin.site.register(TransactionType)
