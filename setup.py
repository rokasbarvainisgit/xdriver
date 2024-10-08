from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="xdriver",
    version="1.2.2",
    packages=find_packages(include=["xdriver*"]),
    install_requires=[
        "pytest~=8.3.2",
        "selenium~=4.23.1"
    ],
    description="Expanded Selenium WebDriver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rokasbarvainisgit/xdriver.git",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    license="MIT"
)
