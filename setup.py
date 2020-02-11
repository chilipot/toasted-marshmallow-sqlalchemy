import re
from setuptools import setup, find_packages


INSTALL_REQUIRES = ("toastedmarshmallow==2.15.2", "SQLAlchemy>=1.2.0")
EXTRAS_REQUIRE = {
    "tests": ["pytest", "mock"],
    "lint": ["flake8==3.7.9", "flake8-bugbear==20.1.4", "pre-commit~=2.0"],
    "docs": ["sphinx==2.3.1", "alabaster==0.7.12", "sphinx-issues==1.2.0"],
}
EXTRAS_REQUIRE["dev"] = EXTRAS_REQUIRE["tests"] + EXTRAS_REQUIRE["lint"] + ["tox"]


def find_version(fname):
    """Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.
    """
    version = ""
    with open(fname, "r") as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError("Cannot find version information")
    return version


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content


setup(
    name="marshmallow-sqlalchemy",
    version=find_version("src/marshmallow_sqlalchemy/__init__.py"),
    description="SQLAlchemy integration with the toastedmarshmallow (de)serialization library",
    long_description=read("README.rst"),
    author="Daniel Guddemi",
    author_email="danguddmi@gmail.com",
    url="https://github.com/chilipot/toasted-marshmallow-sqlalchemy",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    license="MIT",
    zip_safe=False,
    keywords="sqlalchemy marshmallow toastedmarshmallow",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    test_suite="tests",
    project_urls={
        "Changelog": "https://marshmallow-sqlalchemy.readthedocs.io/en/latest/changelog.html",
        "Issues": "https://github.com/chilipot/toasted-marshmallow-sqlalchemy/issues",
        "Funding": "https://opencollective.com/marshmallow",
    },
)
