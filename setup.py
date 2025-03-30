# SPDX-FileCopyrightText: 2025 Andread Wolf
# SPDX-License-Identifier: Apache-2.0

from setuptools import setup
import sys

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

if sys.version_info[:2] < (3, 6):
    sys.exit(
        'Python < 3.6 is not supported'
    )

setup(
    name='zephyr-gdb',
    version='0.1.0',
    author='Andreas Wolf',
    author_email='awolf002@gmail.com',
    description='Python module for reading Zephyr threads in GDB',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='Apache License 2.0',
    url='https://github.com/Snap-A/zephyr-gdb',
    project_urls={
        'Bug Tracker': 'https://github.com/Snap-A/zephyr-gdb/issues',
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    packages=['zephyr_gdb'],
    python_requires='>=3.6',
)
