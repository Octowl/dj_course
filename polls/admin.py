from django.contrib import admin
from .models import Poll, Choice, Response


class ChoiceInline(admin.StackedInline):
    model = Choice


class ResponseInline(admin.TabularInline):
    model = Response
    raw_id_fields = ('choice',)


class PollAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'question', 'choice_count')
    list_filter = ('category',)
    search_fields = ['name', 'question']
    inlines = [ChoiceInline, ResponseInline]


class ResponseAdmin(admin.ModelAdmin):
    list_display = ('poll_name', 'choice', 'comment')


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('poll_name', 'label')
    raw_id_fields = ('poll',)

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Response, ResponseAdmin)
