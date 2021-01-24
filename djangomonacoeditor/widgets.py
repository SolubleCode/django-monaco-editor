from django import forms
from .config import WEB_EDITOR_STATICFILES

class MonacoEditorWidget(forms.Textarea):

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        attrs = {
            'monaco-editor': 'true',
            'data-language': 'html',
            'data-wordwrap': 'off',
            'data-minimap': 'false'
        }
        attrs.update(context['widget']['attrs'])
        context['widget']['attrs'] = attrs
        return context

    class Media:
        staticfiles = WEB_EDITOR_STATICFILES['monaco']
        js = staticfiles['js']
        css = staticfiles['css']