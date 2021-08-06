from django.contrib import admin
from .models import ContactUs,Post
# Register your models here.
@admin.register(ContactUs)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['Name','Email','Address','Message','Timestamp']

@admin.register(Post)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['Strength','Weakness','Timestamp']