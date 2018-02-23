from django.contrib import admin
from .models import Memes
# Register your models here.


class MemeAdmin(admin.ModelAdmin):
	list_display = ["title","image","text1","text2"]
	list_editable = ["image", "text1", "text2"]
	list_per_page = 15
	class Meta:
		model = Memes


admin.site.register(Memes, MemeAdmin)
