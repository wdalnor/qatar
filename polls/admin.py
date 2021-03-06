from django.contrib import admin

from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [

        ('what is your Question ?',               {'fields':['question_text']}),
        (None,                                 {'fields':['your_name']}),
        ('Date information',                   {'fields':['pub_date'], 'classes': ['collapse']}),
        (None,                                 {'fields':['mycountry']}),

    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    search_fields = ['question_text','your_name']
    list_filter = ['pub_date']


admin.site.register(Question, QuestionAdmin)


