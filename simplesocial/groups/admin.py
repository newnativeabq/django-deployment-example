from django.contrib import admin

from groups.models import Group, GroupMembers

# Register your models here.

## Add tabular inline editing to admin
class GroupMemberInline(admin.TabularInline):
    model = GroupMembers

admin.site.register(Group)
