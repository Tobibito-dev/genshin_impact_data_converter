from .templates import character, weapon

from .convert_template import convert_to_template
from .file_handler import reset_output


def translate_data():
    reset_output()
    categories = [character, weapon]
    for category in categories:
        convert_to_template(category.template, category.paths)
    # assemble template data
