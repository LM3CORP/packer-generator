## Packer  - Jinja JSON Templates
###

The purpose of this project is to parse packer templates with multiple parameters and apply values
than can be generated outside the scope of packer execution.


## Requirements
###

* Python 2.7.x - Planning to add support for Python 3.x
* Jinja Package `pip intall jinja2` or `pip install -r requirements.txt`

## How does it work?
###

* run `parse.py --values my_variables.json` to apply the variables present in the templates directory. Jinja will fail
  if some of variables do not contain values.
* You can use a different tool to generate your `my_variables.json` file.

