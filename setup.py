# -*- coding: utf-8 -*-

import os
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup (
    name = 'optidash',
    version = '1.0.2',
    description = 'Official Python integration for Optidash API',
    long_description = 'Optidash: AI-powered image optimization and processing API. We will drastically speed-up your websites and save you money on bandwidth and storage.',
    url = 'https://github.com/optidash-ai/optidash-python',
    download_url = 'https://github.com/optidash-ai/optidash-python/archive/1.0.2.tar.gz',
    author = 'Optidash GmbH',
    author_email = 'support@optidash.ai',
    license = 'MIT',
    keywords = 'optidash image optimization processing resizing resizer cropping scaling masking watermarking filtering thumbnails pic picture photo face face detection visual watermark filter crop mask resize resizer thumbs thumbnail thumbnails jpg jpeg png gif svg bmp psd tiff heic',

    packages = [
        'optidash'
    ],

    install_requires = [
        'requests'
    ],

    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ]
)