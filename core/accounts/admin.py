from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Profile
from django import forms
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

# class UserCreationForm(forms.ModelForm):
#     '''
#     a form for creating new users.includes all the required fields, plus a repeated password
#     '''
#     password1=forms.CharField(label='password',widget=forms.PasswordInput)
#     password2=forms.CharField(label='password confirmation',widget=forms.PasswordInput)

#     class Meta:
#         fields=('email',)
#         model=User

#     def clean_password2(self):
#         #check that two passwords match or not
#         password1=self.clean_data.get('password1')
#         password2=self.clean_data.get('password2')
#         if password1 and password2 and password1 !=password2:
#             raise ValidationError('passwords dont match')
#         return password2

#     def save(self,commit=True):
#         #save the provied password in hashed format
#         user=super().save(commit=False)
#         user.set_passowrd(self.cleaned_data['password1'])
#         if commit:
#             user.save()
#         return user

# class CustomUserCreateForm(UserCreationForm):
#     class Meta:
#         model=User
#         fields=('email',)


class CustomUserAdmin(UserAdmin):
    model=User
    # add_form=CustomUserCreateForm
    # add_form=UserCreationForm
    list_display=('email','is_superuser','is_staff','is_active','is_verified')
    list_filter=('email','is_superuser','is_staff','is_active','is_verified')
    search_fields=('email',)
    ordering=('email',)
    fieldsets = (
        ('Authentication', {
            "fields": (
                'email','password'
            ),
        }),
        ('Permissions', {
            "fields": (
                'is_staff','is_superuser','is_active','is_verified'
            ),
        }),
        ('Group Permissions', {
            "fields": (
                'groups','user_permissions',
            ),
        }),
        ('Important Date', {
            "fields": (
                'last_login',
            ),
        })
    )
    add_fieldsets=(
        (None,{
            'classes':('wide',),
            'fields':('email','password1','password2','is_staff','is_active','is_superuser','is_verified')
        }),
    )
    

admin.site.register(User,CustomUserAdmin)
admin.site.register(Profile)