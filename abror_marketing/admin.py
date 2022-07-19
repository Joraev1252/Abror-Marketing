from django.contrib import admin
from abror_marketing.models import BusinessSmmModel, TargetingModel, LogoRoleModel, OurProjectsModel, ContactModel, CarouselModel


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)
    search_fields = ('id',)
    list_filter = ('id',)


admin.site.register(BusinessSmmModel)
admin.site.register(TargetingModel)
admin.site.register(LogoRoleModel)
admin.site.register(OurProjectsModel)
admin.site.register(ContactModel)
admin.site.register(CarouselModel, TodoAdmin)