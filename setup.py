#!/usr/bin/python3
# -*- coding: utf-8 -*-

from setuptools import setup
from typing import List


def readme() -> List[str]:
    with open('README.md', 'r', encoding='utf-8') as f_readme:
        return f_readme.read()


def requirements() -> List[str]:
    with open('requirements.txt', 'r', encoding='utf-8') as f_requirements:
        return f_requirements.read()


setup(name='rus_stt_norm',
      version='0.1.0',
      description='russian_stt_text_normalization',
      long_description=readme(),
      url='https://github.com/toriningen/russian_stt_text_normalization',
      classifiers=[
          'Natural Language :: Russian',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Text Processing :: Linguistic'
      ],
      keywords='nlp russian stt linguistic seq2seq',
      packages=['rus_stt_norm'],
      install_requires=requirements(),
      include_package_data=True,
      zip_safe=False)
