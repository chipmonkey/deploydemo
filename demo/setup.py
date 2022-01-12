import os, re, io
from setuptools import setup, find_packages

version = re.search(
    r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',  # It excludes inline comment too
    io.open('demo/__init__.py', encoding='utf_8_sig').read()
    ).group(1)

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
    python_requires=">=3.8.0",
)
