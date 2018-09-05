import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spacex_py",
    version="0.0.1",
    author="Kaylum Lally",
    author_email="kaylum@hikaylum.me",
    description="Python wrapper for the SpaceX API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HiKaylum/SpaceX-PY",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests"
    ]
)