import setuptools

with open('ReadMe.md', 'r') as f:
    long_description = f.read()
    
with open('requirements.txt', 'r', encoding='UTF-16') as f:
    required = f.readlines()


setuptools.setup(
    name="wid",
    version="1.0.0",
    description="Tool for extracting and saving specific images from websites.",
    long_description=long_description,
    author="A-Bak",
    author_email="adam.bak753@gmail.com",
    packages=["wid"],
    install_requires=required,
)