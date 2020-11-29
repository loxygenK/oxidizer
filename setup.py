from setuptools import setup


def load_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()


def load_readme():
    with open("README.rst") as f:
        return f.read()

version = "0.1.0"

setup(
    name="arduino-oxidizer",
    version=version,
    author="loxygen",
    author_email="me@loxygen.dev",
    maintainer="loxygen",
    maintainer_email="me@loxygen.dev",
    description="A python tool to build Rust project for Arduino and write it.",
    long_description=load_readme(),
    packages=["src"],
    install_requires=load_requirements(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Rust",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Embedded Systems",
        "License :: OSI Approved :: MIT License"
    ],
    entry_points={
        'console_scripts': [
            "oxidizer=src.main:entry"
        ]
    }
)

