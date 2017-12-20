import os
#import pprint
import json
from jinja2 import Environment, FileSystemLoader

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)

def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)

def create_packer_template_instance():

    packer_output_file  = "packer-output.json"

    template_json_file  = json.load(open('win2016-ami-vbox-variables.json'))
    context = dict()

    for key,value in template_json_file.items():
      context[key] = value

    with open(packer_output_file, 'w') as f:
        jsonfile = render_template('win2016-ami-vbox.json', context)
        f.write(jsonfile)


def main():
    create_packer_template_instance()

########################################

if __name__ == "__main__":
    main()


