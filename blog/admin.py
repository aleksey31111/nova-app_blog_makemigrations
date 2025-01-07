from django.contrib import admin
from .models import Blog
# from django.utils.safestring import mark_safe

# class BlogAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'focus', 'data')
#     list_display_links = ('id', 'title')
#     search_fields = ('title', 'description')
#     def get_html_video(self, object):
#         if object.video:
#             return mark_safe(f"<video src='{object.video.url}' width='50'>")
#

admin.site.register(Blog)
# admin.site.register(BlogAdmin)
