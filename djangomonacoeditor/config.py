from django.conf import settings

WEB_EDITOR_STATICFILES = {
    "monaco": {
        "js": (
            "monaco/vs/loader.js",
            "djangomonacoeditor/monaco/monaco.config.js",
        ),
        "css": {
            "screen": ("djangomonacoeditor/monaco/monaco.custom.css", )
        }
    }
}
