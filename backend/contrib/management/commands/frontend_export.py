from importlib import import_module
from json import dumps

from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand

CHOICES_TEMPLATE = """// DON'T EDIT. THIS FILE IS GENERATED BY ./manage.py frontend_export
// CHANGE MADES MANUALLY TO THIS FILE WILL BE LOST
// backend/contribs/management/commands/frontend_export.py

const CHOICES = %s;

export default CHOICES;
"""


def _write(file_path, template, data):
    with open(file_path, "w") as fp:
        content = template % dumps(data, indent=2, sort_keys=True)
        fp.write(content)
        print(f"written to {fp.name}")


def export_choices():
    choices = {}
    for app in settings.INSTALLED_APPS:
        try:
            module = import_module(f"{app}.choices")
        except ImportError:
            continue
        for attrib in dir(module):
            klass = getattr(module, attrib)
            if not hasattr(klass, "CHOICES"):
                continue
            _ch_map = dict(klass.CHOICES)
            _cl = [dict(value=i[0], label=i[1]) for i in _ch_map.items()]
            _cl = sorted(_cl, key=lambda i: i["value"])
            _choices = {
                "CHOICES": _ch_map,
                "CHOICE_LIST": _cl,
            }
            for key in klass.__dict__.keys():
                if key.startswith("_") or key in ["Meta", "CHOICES"]:
                    continue
                _choices[key] = getattr(klass, key)
            choices[klass.__name__] = _choices

    _write(settings.FRONTEND_CHOICES, CHOICES_TEMPLATE, choices)


class Command(BaseCommand):
    help = "Produce frontend JS files"

    def handle(self, *args, **options):
        export_choices()
        management.call_command("graphql_schema")
