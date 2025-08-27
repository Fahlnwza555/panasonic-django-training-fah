from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin
# Register our model

class PostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = 'body'

admin.site.register(Post, PostAdmin)


#admin.site.register(Post)




