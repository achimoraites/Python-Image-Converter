import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="raw-image-converter",
    version="1.0.1",
    description="Batch conversions of raw images",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/achimoraites/Python-Image-Converter",
    author="Achilles Moraites",
    author_email="achimoraites@yahoo.gr",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        'Topic :: Utilities',
    ],
    keywords='cli, converter, raw, images',
    packages=["raw_image_converter"],
    install_requires=["numpy==1.22.3", "rawpy==0.17.1",
                      "imageio==2.16.2", "Pillow==9.2.0"],
    entry_points={
        "console_scripts": [
            "raw_image_converter=raw_image_converter.__main__:main",
        ]
    },
)
