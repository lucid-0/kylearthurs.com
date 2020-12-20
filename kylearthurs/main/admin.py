from django.contrib import admin
from main.models import Blog, Book, Game, Record, System


class BlogAdmin(admin.ModelAdmin):
    pass
admin.site.register(Blog, BlogAdmin)


class BookAdmin(admin.ModelAdmin):
    pass
admin.site.register(Book, BookAdmin)


class GameAdmin(admin.ModelAdmin):
    pass
admin.site.register(Game, GameAdmin)


class SystemAdmin(admin.ModelAdmin):
    pass
admin.site.register(System, SystemAdmin)


class RecordAdmin(admin.ModelAdmin):
    pass
admin.site.register(Record, RecordAdmin)