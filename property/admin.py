from django.contrib import admin

# Register your models here.
from .models import Property,proberty_book,PropertyImages,PropertyReview,Category,Place
from django_summernote.admin import SummernoteModelAdmin


class SomeModelAdmin(SummernoteModelAdmin):
    summernote_fields="__all__"


admin.site.register(Property,SomeModelAdmin)
admin.site.register(proberty_book)
admin.site.register(PropertyImages)
admin.site.register(PropertyReview)
admin.site.register(Category)
admin.site.register(Place)




