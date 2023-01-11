import threading
from threading import Thread

from tqdm import tqdm

from templates import weapon, character, artifact

from .convert_template import convert_to_template
from .file_handler import reset_output


def translate_data():
    reset_output()
    categories = [character, weapon, artifact]
    for category in tqdm(categories, position=0, leave=True):
        template_converter = Thread(target = convert_to_template, args=(category.template, category.paths))
        template_converter.start()
    # assemble template data