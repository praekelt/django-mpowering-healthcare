from django.contrib import admin
from blog.models import PressRelease, PressReleaseLink, Blog, Report, Presentation, Video, MapMarker
from blog.forms import NewsArticleModelAdminForm, ReportModelAdminForm, PresentationModelAdminForm, VideoModelAdminForm, NewsArticleLinkModelAdminForm, BlogModelAdminForm, MapMarkerAdminForm


class PressReleaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'was_published_recently')
    search_fields = ['title']
    date_hierarchy = 'pub_date'
    prepopulated_fields = {'slug': ('title',)}
    form = NewsArticleModelAdminForm

admin.site.register(PressRelease, PressReleaseAdmin)


class PressReleaseLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'was_published_recently')
    search_fields = ['title']
    date_hierarchy = 'pub_date'
    form = NewsArticleLinkModelAdminForm

admin.site.register(PressReleaseLink, PressReleaseLinkAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'was_published_recently')
    search_fields = ['title']
    date_hierarchy = 'pub_date'
    prepopulated_fields = {'slug': ('title',)}
    form = BlogModelAdminForm

admin.site.register(Blog, BlogAdmin)


class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'was_published_recently')
    search_fields = ['title']
    date_hierarchy = 'pub_date'
    prepopulated_fields = {'slug': ('title',)}
    form = ReportModelAdminForm

admin.site.register(Report, ReportAdmin)


class PresentationAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'was_published_recently')
    search_fields = ['title']
    date_hierarchy = 'pub_date'
    form = PresentationModelAdminForm

admin.site.register(Presentation, PresentationAdmin)


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'was_published_recently')
    search_fields = ['title']
    date_hierarchy = 'pub_date'
    form = VideoModelAdminForm

admin.site.register(Video, VideoAdmin)


class MapMarkerAdmin(admin.ModelAdmin):
    list_display = ('name_of_region', 'date_added', 'was_published_recently')
    search_fields = ['name_of_region']
    date_hierarchy = 'date_added'
    form = MapMarkerAdminForm

admin.site.register(MapMarker, MapMarkerAdmin)
