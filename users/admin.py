from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import *
User = get_user_model()
admin.site.unregister(Group)
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['phone', 'is_staff','role']
    list_filter = ['role','is_superuser','is_staff']
    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        ('Personal info', {'fields': ('fullname','role')}),
        ('Permissions', {'fields': ('is_superuser','is_staff')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password', 'password_2')}
        ),
    )
    search_fields = ['phone','fullname']
    ordering = ['phone']
    filter_horizontal = ()

admin.site.register(User,UserAdmin)
class DirectorAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['phone', 'is_staff','role']
    list_filter = ['role','is_superuser','is_staff']
    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        ('Personal info', {'fields': ('fullname','role')}),
        ('Permissions', {'fields': ('is_superuser','is_staff')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password', 'password_2')}
        ),
    )
    search_fields = ['phone','fullname']
    ordering = ['phone']
    filter_horizontal = ()

admin.site.register(Director,DirectorAdmin)
class ManagerAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['phone', 'is_staff','role']
    list_filter = ['role','is_superuser','is_staff']
    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        ('Personal info', {'fields': ('fullname','role')}),
        ('Permissions', {'fields': ('is_superuser','is_staff')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password', 'password_2')}
        ),
    )
    search_fields = ['phone','fullname']
    ordering = ['phone']
    filter_horizontal = ()

admin.site.register(Manager,ManagerAdmin)
class TeacherAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['phone', 'is_staff','role']
    list_filter = ['role','is_superuser','is_staff']
    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        ('Personal info', {'fields': ('fullname','role')}),
        ('Permissions', {'fields': ('is_superuser','is_staff')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password', 'password_2')}
        ),
    )
    search_fields = ['phone','fullname']
    ordering = ['phone']
    filter_horizontal = ()

admin.site.register(Teacher,TeacherAdmin)