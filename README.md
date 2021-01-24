# Django-Monaco-Editor


This package provides a custom widgets to use monaco in django admin.


## Installation

To install the package by `pip` run following command

```sh
# From Github (latest updates)
pip install git+https://github.com/solublecode/django-monaco-editor.git#egg=django-monaco-editor
```

## Usage

```python
# settings.py

INSTALLED_APPS = [
    ...
    'djangomonacoeditor',
    ...
]

```

```python
# models.py
import json
from django.db import models

class JSONModel(models.Model):
    title = models.CharField(max_length=50)
    _text = models.TextField()

    @property
    def text(self):
        return json.loads(self._text)

    @text.setter
    def text(self, val):
        self._text = json.dumps(val, ensure_ascii=False)

    def __str__(self):
        return self.title
```
```python
# forms.py
from django import forms
from djangomonacoeditor.widgets import MonacoEditorWidget
from .models import JSONModel


class JsonModelForm(forms.ModelForm):
    class Meta:
        model = JSONModel
        fields = "__all__"
        widgets = {
            "_text": MonacoEditorWidget(
                attrs={"data-wordwrap": "on", "data-language": "json"}
            )
        }
```
