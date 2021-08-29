import os
from flask import current_app


@current_app.cli.group()
def translate():
    pass


@translate.command()
def compile():
    if os.system('pybabel compile -d app/translations'):
        raise RuntimeError('Compile command failed.')
