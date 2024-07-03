from setuptools import setup, find_packages
from pip.req import parse_requirements

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements('requirements.txt')

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="geofinder_vt",  # Replace with your own package name
    version="0.1.0",
    author="Your Name",
    author_email="vaidhyanathan@vt.edu",
    description="A brief description of your package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nathan846/geofindervt",  # Replace with the URL of your project
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Choose your license
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
    install_requires=[
        'numpy>=0.19.0',
    ],
)