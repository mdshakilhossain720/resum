from django.contrib import admin
from.models import Resum

# Register your models here.
@admin.register(Resum)
class ResumAdmin(admin.ModelAdmin):
    class Meta:
        model=Resum
        fields="__all__"
        
