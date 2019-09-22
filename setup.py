from setuptools import setup, find_packages

setup(
    name = 'EAlib',
    version = '1.0',
    keywords='ea tsp',
    description = 'a EA library for TSP problem',
    license = 'MIT License',
    url = 'https://github.com/iseesaw/EAlib',
    author = 'HIT EAlib Group',
    author_email = 'kyzhang@ir.hit.edu.cn',
    packages = find_packages(),
    include_package_data = True,
    platforms = 'any',
    install_requires = [],
)