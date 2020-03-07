# coding: utf-8
# Copyright 2019

"""Meta information."""

from setuptools import find_packages, setup

with open("README.md") as readme:
    LONG_DESCRIPTION = readme.read()

CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Widget Sets",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Programming Language :: Python :: 3.6",
    "Environment :: X11 Applications",
    "Natural Language :: English",
    "Operating System :: Unix",
]

setup(name="WidgetsKV",
      version="0.1.0",
      description="Set of widgets for the Kivy framework",
      long_description=LONG_DESCRIPTION,
      long_description_content_type="text/markdown",
      url="https://github.com/Paduct/widgets_kv",
      author=' ',
      author_email=' ',
      license="GPL-3.0",
      classifiers=CLASSIFIERS,
      keywords="widget gui kivy",
      packages=find_packages(),
      install_requires=["kivy"],
      python_requires=">=3.6",
      package_data={"widgetskv": ["*.kv"]},
      zip_safe=False)
