from django.contrib import admin
from .models import Post


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['title', 'summary', 'submission_date', 'reviewer']
    ordering = ['title']


admin.site.register(Post, ReviewAdmin)
