from setuptools import setup, find_packages

requires = [
    'tldextract',
    'docopt',
    'requests',
]

setup(
    name='dyn-gandi',
    version='1.0',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    scripts=['dyn-gandi'],
    dependency_links=[]
)
