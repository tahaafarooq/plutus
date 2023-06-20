from os import path
from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="plutus",
    version="1.0",
    description="Plutus is a tool that is made ready for the purpose of monitoring your server's processes and identifying strange processes!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tahaafarooq/plutus",
    download_url="",
    author="Tahaa Farooq",
    author_email="tahacodez@gmail.com",
    license="MIT",
    packages=["plutus"],
    keywords=[
        "Blue Teaming",
        "monitoring tool" "monitoring" "cybersecurity" "blue-teaming" "security tools",
        "python-tanzania",
    ],
    install_requires=["psutil", "pyshark", "systemd", "subprocess"],
    include_package_data=True,
    python_requires=">=3.7",
    classifiers=[
        "Intended Audience :: Security Researchers",
        "Topic :: Cyber Security :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
    ],
)
