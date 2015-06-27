# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.html import mark_safe


class Level(models.Model):
    created = models.DateTimeField(_("created"), auto_now_add=True)
    modified = models.DateTimeField(_("modified"), auto_now=True)
    author = models.ForeignKey("auth.User", verbose_name=_("author"))
    title = models.CharField(_("title"), max_length=255)
    slug = models.SlugField(_("slug"), max_length=255)
    labyrinth = models.TextField(_("labyrinth"), help_text=_('"#" - bricks, " " - spaces, "*" - collectables, "p" - player, "e" - exit'))

    class Meta:
        verbose_name = _("Level")
        verbose_name_plural = _("Levels")

    def __str__(self):
        return self.title

    def render_labyrinth(self):
        html = []
        html.append('<table>')
        for line in self.labyrinth.splitlines():
            html.append('<tr>')
            for char in line:
                html.append('<td>')
                if char == " ":
                    html.append('<img src="/static/site/img/space.png" />')
                if char == "#":
                    html.append('<img src="/static/site/img/brick.png" />')
                if char == "*":
                    html.append('<img src="/static/site/img/collectable.png" />')
                if char == "p":
                    html.append('<img src="/static/site/img/player.png" />')
                if char == "e":
                    html.append('<img src="/static/site/img/exit.png" />')
                html.append('</td>')
            html.append('</tr>')
        html.append('</table>')
        return mark_safe(''.join(html))

    def render_labyrinth_json(self):
        import json
        rows = []
        for line in self.labyrinth.splitlines():
            row = []
            for char in line:
                row.append(char)
            rows.append(row)
        return mark_safe(json.dumps(rows))