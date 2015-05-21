from django.contrib import admin
from news.models import News
from django.forms import TextInput, Textarea
from django.db import models
# Register your models here.

class NewsAdmin(admin.ModelAdmin):


    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        # models.TextField: {'widget': Textarea(attrs={'rows':10, 'cols':60})},
    }
    # readonly_fields = ('custom_link',)
    def custom_link(instance):
            return '<a href="{}">{}</a>'.format(instance.link,instance.link)

    custom_link.short_description = 'link'
    custom_link.allow_tags = True  # htmlタグ許可

    list_display = ('title','subject',custom_link,'date','base_site')
    # ordering = ('date',)

    class Meta:
        model = News


admin.site.register(News,NewsAdmin)

