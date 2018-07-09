import setuptools
import library

setuptools.setup(
    name=library.name,
    version=library.__version__,
    author="my",
    description="a test package",
    url="https://gitlab.macom.com/ma046155/library",
    packages=setuptools.find_packages(),
    )


