from setuptools import setup
import os

_this_dir = os.path.abspath(os.path.dirname(__file__))
_about = {}
with open(os.path.join(_this_dir, 'design_patterns', '__version__.py'),
          'r', 'utf-8') as f:
        exec(f.read(), _about)

with open('README.md', 'r', 'utf-8') as f:
        readme = f.read()

_packages = ['design_patterns']
_requires = []

setup(
    name=_about['__title__'],
    version=_about['__version__'],
    description=_about['__description__'],
    long_description=readme,
    author=_about['__author__'],
    author_email=_about['__author_email__'],
    url=_about['__url__'],
    packages=_packages,
    package_data={'design_patterns': []},
    package_dir={'design_patterns': 'design_patterns'},
    include_package_data=True,
    install_requires=_requires,
    license=_about['__license__'],
    zip_safe=True,
    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Education',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ),
)
