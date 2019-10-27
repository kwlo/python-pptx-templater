import io

from setuptools import find_packages
from setuptools import setup

with io.open("README.rst") as f:
    readme = f.read()

with io.open("VERSION", "rt", encoding="utf8") as f:
    version = f.read()

setup(
    name="python-pptx-templater",
    version=version,
    url="",
    project_urls={
        "Documentation": "https://github.com/kwlo/python-pptx-templater",
        "Code": "https://github.com/kwlo/python-pptx-templater",
        "Issue tracker": "https://github.com/kwlo/python-pptx-templater/issues",
    },
    license="MIT License",
    author="kwlo",
    author_email="kwlo@github.com",
    maintainer="kwlo",
    maintainer_email="kwlo@github.com",
    description="Create customizable PowerPoint Presentation (.pptx) using a predefined layout template",
    long_description=readme,
    long_description_content_type="text/x-rst",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Office/Business :: Office Suites",
    ],
    packages=find_packages(),
    python_requires="!=2.*, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    install_requires=["jinja2>=2.10.3", "python-pptx>=0.6.18"],
)
