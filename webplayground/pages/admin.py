from django.contrib import admin
from .models import Page


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')

    # We inject our css file. Noy CK editor is responsive in the admin page.
    class Media:
        css = {
            'all': ('pages/css/custom_ckeditor.css',)
        }


admin.site.register(Page, PageAdmin)