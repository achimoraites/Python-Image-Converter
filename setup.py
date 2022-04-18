import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="raw-image-converter",
    version="1.0.0",
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
    packages=["raw_image_converter"],
    include_package_data=True,
    install_requires=["rawpy", "imageio", "Pillow"],
    entry_points={
        "console_scripts": [
            "raw_image_converter=raw_image_converter.__main__:main",
        ]
    },
)
