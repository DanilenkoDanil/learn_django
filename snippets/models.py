from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]

lexers = []
for item in get_all_lexers():
    if item[1]:
        lexers.append(item)


STYLES = [item for item in get_all_styles()]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLES_CHOICES = sorted([(item, item) for item in STYLES])


class Snippet(models.Model):
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    code = models.TextField()
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=256)
    style = models.CharField(choices=STYLES_CHOICES, default='igor', max_length=256)
