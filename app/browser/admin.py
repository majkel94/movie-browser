from django.contrib import admin

import browser.models


@admin.register(browser.models.FavMovie)
class FavMoviesAdmin(admin.ModelAdmin):
    pass
