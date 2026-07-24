from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pitonx",
    version="8.1.7",
    author="Fathirthe-founder1",
    description="PitonX - A Python Programming Language with Indonesian Keywords",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Fathirthe-founder1/PitonX",
    packages=find_packages(),
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "pitonx=pitonx.main:main",
            "piton=pitonx.main:repl_main",
        ],
    },
    keywords=[
        "python",
        "programming",
        "language",
        "indonesian",
        "transpiler",
        "interpreter",
        "bahasa-pemrograman",
    ],
    project_urls={
        "Bug Reports": "https://github.com/Fathirthe-founder1/PitonX/issues",
        "Documentation": "https://github.com/Fathirthe-founder1/PitonX",
        "Source Code": "https://github.com/Fathirthe-founder1/PitonX",
    },
    include_package_data=True,
)
