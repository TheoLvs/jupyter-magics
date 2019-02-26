# Setup.py tutorial https://packaging.python.org/tutorials/packaging-projects/

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="magics",
    version="0.0.1",
    author="Theo Alves Da Costa",
    author_email="theo.alves.da.costa@gmail.com",
    description="A set of custom magics and tools for productivity",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/theolvs/jupyter-magics",
    packages=setuptools.find_packages(),
    package_data={'magics.static': ['*.wav']},
    include_package_data=False,
    install_requires=[
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)