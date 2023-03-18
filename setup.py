from setuptools import find_packages, setup

long_desc = """
A Sphinx Extension implementing the Scroll Depth extension for Google Analytics.
"""

requires = ["Sphinx>=0.6", "setuptools"]


setup(
    name="sphinxcontrib-scrolldepth",
    version="1.0",
    description="Sphinx scroll-depth extension",
    author="Simon Bodvarsson",
    author_email="simonb92@gmail.com",
    maintainer="Benedikt Magnusson",
    maintainre_email="bsm@hi.is",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=["sphinxcontrib"],
)
