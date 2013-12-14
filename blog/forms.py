from django import forms
from blog.models import Article, Report, Video
from tinymce.widgets import TinyMCE


class ArticleModelAdminForm(forms.ModelForm):
    body = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Article


class ReportModelAdminForm(forms.ModelForm):
    class Meta:
        model = Report


class VideoModelAdminForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Video
