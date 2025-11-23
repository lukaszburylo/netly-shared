"""Setup script for packaging and distributing the project."""
from pathlib import Path
from setuptools import setup, find_packages

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="netly_shared",  # nazwa paczki, taka jak w pip install
    version="0.1.0",  # wersja paczki
    packages=find_packages(),  # automatyczne znalezienie folderów z __init__.py
    install_requires=[  # opcjonalne zależności
        "pydantic",
    ],
    python_requires=">=3.10",  # wersja Pythona
    long_description=long_description,
    long_description_content_type='text/markdown'
)
