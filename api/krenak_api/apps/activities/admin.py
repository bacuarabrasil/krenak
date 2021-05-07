from django.contrib import admin
from .models import Activity, Comment, Task
# Register your models here.


class TaskInline(admin.TabularInline):
    model = Task
    save_on_top = True
    extra = 0

class CommentInline(admin.TabularInline):
    model = Comment
    save_on_top = True
    extra = 0

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
    ordering = ("title",)
    exclude = ("comments",)
    inlines = [TaskInline]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("text",)
    search_fields = ("text",)
    ordering = ("text",)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
    ordering = ("title",)