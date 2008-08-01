from django.contrib import admin

from djumblr.models import Regular, Photo, Quote, Link, Conversation, ConversationLine, Video, Audio

class ConversationLineInline(admin.TabularInline):
    model = ConversationLine

class ConversationAdmin(admin.ModelAdmin):
    model = Conversation
    inlines = [ConversationLineInline]

admin.site.register(Regular)
admin.site.register(Photo)
admin.site.register(Quote)
admin.site.register(Link)
admin.site.register(Conversation, ConversationAdmin)
admin.site.register(Video)
admin.site.register(Audio)
