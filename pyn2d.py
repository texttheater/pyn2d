"""
pyn2d.py
Mnemosyne plugin: converts Hanyu Pinyin with numbers to diacritics in the
learning view. Code based on the filter.py example plugin by Peter Bienstmann.
"""


from mnemosyne.libmnemosyne.filter import Filter
from mnemosyne.libmnemosyne.plugin import Plugin
import subprocess
from tempfile import NamedTemporaryFile


def num2dia(text):
    with NamedTemporaryFile(mode='w') as f:
        f.write(text.encode('UTF-8'))
        f.flush()
        return subprocess.check_output(['pyn2d', f.name]).decode('UTF-8')


class Pyn2D(Filter):

    def run(self, text, card, fact_key, **render_args):
        if fact_key == 'p_1': # p_1 stands for pronunciation in cards of type
                              # "Vocabulary"
            return num2dia(text)
        else:
            return text


class Pyn2DPlugin(Plugin):

    name = "Pyn2D"
    description = "Convert Hanyu Pinyin with numbers to diacritics"
    components = [Pyn2D]

    def activate(self):
        Plugin.activate(self)
        self.render_chain("default").\
            register_filter(Pyn2D, in_front=False)
        # Other chain you might want to add to is e.g. "card_browser".

    def deactivate(self):
        Plugin.deactivate(self)
        self.render_chain("default").\
            unregister_filter(Pyn2D)

# Register plugin.

from mnemosyne.libmnemosyne.plugin import register_user_plugin
register_user_plugin(Pyn2DPlugin)
