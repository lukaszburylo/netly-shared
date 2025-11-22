"""Setup script for packaging and distributing the project."""
from setuptools import setup, find_packages

setup(
    name="netly_shared",  # nazwa paczki, taka jak w pip install
    version="0.0.5",  # wersja paczki
    packages=find_packages(),  # automatyczne znalezienie folderów z __init__.py
    install_requires=[  # opcjonalne zależności
        "pydantic",
    ],
    python_requires=">=3.10",  # wersja Pythona
)
