from setuptools import (
    setup,
    find_packages
)


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='SmallAppLib',
    version='1.0.0',
    author='Cupcake_wrld',
    author_email='ccaatt63@gmail.com',
    description='App for simple console app building',
    long_description=readme(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    keywords='files small console ',
    project_urls={
        'GitHub': 'Bob-jacka'
    },
    python_requires='>=3.12'
)
