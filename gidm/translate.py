from .templates import character

from .convert_template import convert_to_template

def translate_data():
    categories = [character]
    for category in categories:
        convert_to_template(category.template, category.paths)
    # assemble template data