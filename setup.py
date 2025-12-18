from setuptools import setup, find_packages

setup(
    name="datastory_viz",
    version="1.0.0",
    author="Votre Nom",
    author_email="votre.email@example.com",
    description="Une bibliothèque de visualisation appliquant les principes du data storytelling",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/votre-username/datastory_viz",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        'matplotlib>=3.5.0',
        'seaborn>=0.12.0',
        'numpy>=1.21.0',
        'pandas>=1.3.0',
    ],
)