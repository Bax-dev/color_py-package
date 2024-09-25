from setuptools import setup, find_packages

setup(
    name="color_display",
    version="0.1.0",
    description="A package to display variables, classes, functions, and data types in different colors",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Bassey Eyo Inyang",
    author_email="basseyeyo991@gmail.com",
    url="https://github.com/Bax-dev/color_py-package.git",
    packages=find_packages(),
    install_requires=["colorama"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    python_requires=">=3.6",
)
