# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import App, Parameter, ConfigRequest


@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'value')
    search_fields = ('name',)


@admin.register(ConfigRequest)
class ConfigRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'remote_addr', 'user_agent')
    list_filter = ('timestamp',)
    search_fields = ('remote_addr', 'user_agent')