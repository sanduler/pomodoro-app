from setuptools import setup

APP = ['main.py']
DATA_FILES = [
    ('images', ['img/pomodoro.png'])
]
OPTIONS = {
    'argv_emulation': True,
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)
