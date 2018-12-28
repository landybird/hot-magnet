from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    author="landybird",
    author_email="1442172978@qq.com",
    name="hot-magnet",
    version="0.0.1",
    license="MIT",
    url="https://github.com/landybird/hot-magnet",
    py_modules=["hot_magnet"],
    install_requires=["bs4", "requests", "lxml", "future"],
    description="Get Hot Magnet Top 20",
    long_description = long_description,
    entry_points={
        "console_scripts": ["hot_smagnet=manage:main"]
    },
)
