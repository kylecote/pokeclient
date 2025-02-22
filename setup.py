from setuptools import setup, find_packages
setup(
    name="pokeapi",
    version="0.1",
    description="A simple SDK for the PokeAPI",
    package_dir={"":"app"},
    packages=find_packages(where="app"),
    install_requires=[
        "requests >= 2.32.3"],
    author="Kyle Cote",
    author_email="kylecote@gmail.com",
    url="https://github.com/kylecote/speakeasy-assesment",
    python_requires=">=3.10"
)