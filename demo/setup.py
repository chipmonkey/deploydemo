import os
from setuptools import setup, find_packages

with open("VERSION") as f:
    version = f.read().strip()

requirements_path = os.path.join(os.path.dirname(__file__), "requirements2.txt")
with open(requirements_path) as f:
    dependencies = f.readlines()

setup(
    name="demo",
    version=version,
    author="Chipmonkey",
    author_email="",
    package_dir={"demo": "./demo"},
    py_modules=["demo"],
    packages=find_packages(),
    description="Simple demo with everything",
    install_requires=dependencies,
    python_requires=">=3.9.0",
)
