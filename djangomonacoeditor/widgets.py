from django import forms

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
        js = [
            "monaco/loader.js",
            "djangomonacoeditor/monaco.config.js",
        ]
        css = {
            "screen": ("djangomonacoeditor/monaco.custom.css", )
        }