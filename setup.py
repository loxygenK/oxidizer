from setuptools import setup

setup(
    name="oxidizer",
    version="0.1.0",
    packages=["src"],
    install_requires=["pyserial"],
    entry_points={
        'console_scripts': [
            "oxidizer=src.main:entry"
        ]
    }
)
