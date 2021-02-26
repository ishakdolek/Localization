from django.shortcuts import render
from django.utils.translation import activate, get_language, ugettext_lazy as _

# Create your views here.

test1 = _("Hello")
test2 = _("TEST2")
test3 = _("TEST3")
test4 = _("TEST4")

def index(request):
    context = {}
    template_name = "index.html"
    context["hello"] = translate(language="en")
    return render(request, template_name, context)


def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        text = _(test1)
        
    finally:
        activate(cur_language)
    return text
