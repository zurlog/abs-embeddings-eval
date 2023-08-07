from setuptools import find_packages, setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="abstracts_embeddings_evaluation",
    description="Data and code used for evaluating abstracts embeddings on a papers classification task",
    author=["Giovanni Zurlo"],
    author_email="giovanni.zurlo@studio.unibo.it",
    install_requires=required,
    packages=find_packages(),
)