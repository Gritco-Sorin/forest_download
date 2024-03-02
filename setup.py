from setuptools import setup, find_packages

setup(
    name="forest_download",
    version="0.0.1",
    author="SorinGritco",
    author_email="soringritco03@gmail.com",
    url="",
    description="Library to download Deep Forest model",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    entry_points={"console_scripts": ["forest_download = forest_download.main:download"]},
)