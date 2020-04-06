from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.translation import gettext, gettext_lazy as _
from .models import User
from api.models import Candidate, Poll
# Register your models here.


class AdminUser(ModelAdmin):
    list_filter = ('staff', 'admin', 'active', 'groups')
    fieldsets = (
         (None, {'fields': ('email', 'password')}),
          (_('Personal info'), {'fields': ('first_name', 'last_name')}),
          (_('Permissions'), {
              'fields': ('active', 'staff', 'admin'),
          })
      )

admin.site.register(User, AdminUser)
admin.site.register(Candidate)
admin.site.register(Poll)