from setuptools import setup

setup(
    name="oxidizer",
    version="0.0.0",
    packages=["src"],
    entry_points={
        'console_scripts': [
            "oxidizer=src.main:entry"
        ]
    }
)