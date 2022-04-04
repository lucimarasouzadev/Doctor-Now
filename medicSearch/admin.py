from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'birthday',)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'birthday',)
    empty_value_display = 'vazio'


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'birthday',)
    list_display_links = ('user', 'role',)


class ProfileAdmin(admin.ModelAdmin):
    list_filter = ('user__is_active',)


class ProfileAdmin(admin.ModelAdmin):
    fields = ('user', ('role', ), 'image', 'birthday', 'specialties', 'addresses',)


class ProfileAdmin(admin.ModelAdmin):
    exclude = ('favorites', 'created_at', 'updated_at',)


class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('user',)


class ProfileAdmin(admin.ModelAdmin):
    search_fields = ('user__username',)


class ProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Usuário', {
            'fields': ('user', 'birthday', 'image')
        }),
        ('Função', {
            'fields': ('role',)
        }),
        ('Extras', {
            'fields': ('specialties', 'addresses')
        }),
    )


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth',)

    def birth(self, obj):
        if obj.birthday:
            return obj.birthday.strftime("%d/%m/%Y")


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth',)

    def birth(self, obj):
        return obj.birthday
    birth.empty_value_display = '__/__/____'


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialtiesList', 'addressesList',)

    def specialtiesList(self, obj):
        return [i.name for i in obj.specialties.all()]

    def addressesList(self, obj):
        return [i.name for i in obj.addresses.all()]


#class ProfileAdmin(admin.ModelAdmin): Pagina80
#    list_display = ('user', 'specialtiesList', 'addressesList',)
#
#    class Media:
#        css = {
#            "all": ("css/custom.css",)
#        }
#        js = ("js/custom.js",)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Address)
admin.site.register(DayWeek)
admin.site.register(Rating)
admin.site.register(Speciality)


