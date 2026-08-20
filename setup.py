#!/usr/bin/env python

import codecs

from setuptools import find_packages, setup

setup(
    name="filetype2",
    version="1.2.0",
    description="Infer file type and MIME type of any file/buffer. No external dependencies.",
    long_description=codecs.open("README.md", "r", encoding="utf-8", errors="ignore").read(),
    long_description_content_type="text/markdown",
    keywords="file libmagic magic infer numbers magicnumbers discovery mime type kind",
    url="https://github.com/h2non/filetype.py",
    download_url="https://github.com/h2non/filetype.py/tarball/master",
    author="Tomas Aparicio",
    author_email="tomas@aparicio.me",
    license="MIT",
    license_files=["LICENSE"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Topic :: System",
        "Topic :: System :: Filesystems",
        "Topic :: Utilities",
    ],
    python_requires=">=3.8",
    platforms=["any"],
    packages=find_packages(exclude=["dist", "build", "docs", "tests", "examples"]),
    package_data={"filetype": ["LICENSE", "*.md", "py.typed", "*.pyi", "types/*.pyi"]},
    zip_safe=False,
    entry_points={
        "console_scripts": ["filetype=filetype.__main__:main"],
    },
)
