from django.contrib import admin
from .models import Level, Question, Option

# Inline for Options within a Question
class OptionInline(admin.TabularInline):
    model = Option
    extra = 3  # Show 3 empty option forms by default
    max_num = 10  # Limit the maximum number of options to 10

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display name in list view
    search_fields = ('name',)  # Add search functionality

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'level')  # Show question text and level in list view
    search_fields = ('text',)  # Search by question text
    list_filter = ('level',)  # Filter by level
    inlines = [OptionInline]  # Inline options within a question

# @admin.register(Option)
# class OptionAdmin(admin.ModelAdmin):
#     list_display = ('text', 'question', 'is_correct')  # Show text, question, and correctness
#     list_filter = ('is_correct',)  # Filter options by correctness
#     search_fields = ('text', 'question__text')  # Search by option text or question text
