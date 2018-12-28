from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    author="landybird",
    author_email="1442172978@qq.com",
    name="hot-magnet",
    version="0.0.2",
    license="MIT",
    url="https://github.com/landybird/hot-magnet",
    py_modules=["hot_magnet"],
    install_requires=[
        "setuptools",
        "requests",
        "fake_useragent",
        "requests_html",
        "PyYAML"],
    description="Get Hot Magnet Top 20",
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(
        exclude=(
                "tests.*",
                "tests",
                "example")),
    include_package_data=True,
    entry_points={
        "console_scripts": ["hot-magnet=hot_magnet:main"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ])
