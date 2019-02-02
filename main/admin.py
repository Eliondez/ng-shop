from django.contrib import admin

from .models import Category, MyItem

# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']

admin.site.register(Category)
admin.site.register(MyItem)
