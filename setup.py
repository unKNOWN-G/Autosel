from setuptools import setup, find_packages
import pathlib

VERSION = '0.0.2'
# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# Setting up
setup(
    name="autosel",
    version=VERSION,
    author="Giri",
    author_email="<karnatisaivenkatagiri@gmail.com>",
    description="autosel is a Python package that automates sending emails, Whatsapp text, images, videos, "
                "and audio messages along with other functionalities like creating a group and spam bot.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/unKNOWN-G/autosel",
    packages=find_packages(),
    install_requires=['gTTS', 'Selenium'],
    include_package_data=True,
    py_modules=["autosel"],  # Name of the python package
    keywords=['autosel', 'automate', 'whatsapp', 'email', 'spam', 'bot',  'python', 'selenium'],
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Operating System :: OS Independent",
    ]
)
