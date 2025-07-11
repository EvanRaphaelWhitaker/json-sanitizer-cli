from setuptools import setup, find_packages

setup(
    name="json-sanitizer-cli",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'json-sanitize=sanitizer.cli:main'
        ]
    },
    install_requires=[],
)
