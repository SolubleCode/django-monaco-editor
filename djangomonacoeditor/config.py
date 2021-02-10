from django.conf import settings

WEB_EDITOR_STATICFILES = {
    "monaco": {
        "js": (
            f"{settings.STATIC_URL}monaco/vs/loader.js",
            f"{settings.STATIC_URL}djangomonacoeditor/monaco/monaco.config.js",
        ),
        "css": {
            "screen": (f"{settings.STATIC_URL}djangomonacoeditor/monaco/monaco.custom.css", )
        }
    }
}
