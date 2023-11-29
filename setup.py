from setuptools import find_packages, setup

with open("requirements.txt") as f:
    required_packages = f.read().splitlines()

setup(
    name="AwesomeProject101",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=required_packages,
)
