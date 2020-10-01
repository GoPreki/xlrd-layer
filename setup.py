#!/usr/bin/env python3

from distutils.core import setup

setup(
    name="xlrd-layer",
    version="1.0.0",
    author="Preki",
    author_email="ramos@gopreki.com",
    packages=['xlrd_layer'],
    url='https://gopreki.com',
    download_url="https://github.com/GoPreki/xlrd-layer",
    license="MIT",
    description="Python library for Preki xlsx reading process",
    long_description="Python library for Preki xlsx reading process",
    install_requires=["xlrd"],
)
