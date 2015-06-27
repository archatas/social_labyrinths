from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify

from crispy_forms.helper import FormHelper
from crispy_forms import layout, bootstrap

from .models import Level


class LevelForm(forms.ModelForm):
    class Meta:
        model = Level
        fields = ['title', 'labyrinth']

    def __init__(self, request, *args, **kwargs):
        super(LevelForm, self).__init__(*args, **kwargs)
        self.request = request

        self.helper = FormHelper()
        self.helper.form_action = ""
        self.helper.form_method = "POST"

        self.helper.layout = layout.Layout(
            "title",
            "labyrinth",
            bootstrap.FormActions(
                layout.Submit('submit', _('Save')),
            )
        )
    def save(self, commit=True):
        level = super(LevelForm, self).save(commit=False)
        level.author = self.request.user
        level.slug = slugify(self.cleaned_data['title'])
        if commit:
            level.save()
        return level


def level_list(request):
    levels = Level.objects.all()
    return render(request, 'levels/level_list.html', {'levels': levels})


def level_detail(request, slug):
    level = get_object_or_404(Level, slug=slug)
    return render(request, 'levels/level_detail.html', {'level': level})


def add_level(request):
    if request.method == "POST":
        form = LevelForm(request, data=request.POST)
        if form.is_valid():
            level = form.save()
            return redirect('level_detail', slug=level.slug)
    else:
        form = LevelForm(request)
    return render(request, 'levels/change_level.html', {'form': form})


def change_level(request, slug):
    level = get_object_or_404(Level, slug=slug)
    if request.method == "POST":
        form = LevelForm(request, data=request.POST, instance=level)
        if form.is_valid():
            level = form.save()
            return redirect('level_detail', slug=level.slug)
    else:
        form = LevelForm(request, instance=level)
    return render(request, 'levels/change_level.html', {'form': form})

