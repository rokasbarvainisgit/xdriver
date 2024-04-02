from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="xdriver",
    version="1.0.0",
    packages=find_packages(include=["xdriver*"]),
    install_requires=[
        "pytest~=8.1.1",
        "selenium~=4.17.2",
        "webdriver-manager~=4.0.1"
    ],
    description="Expanded Selenium WebDriver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rokasbarvainisgit/xdriver.git",
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    license="MIT"
)
