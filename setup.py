from setuptools import setup, find_packages
 
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='abuse',
      version='0.1',
      url='https://github.com/0x48piraj/abuse',
      license='MIT',
      author='Piyush Raj',
      author_email='piyush.189303055@muj.manipal.edu',
      description='World\'s First Profanity Library.',
      packages=find_packages(exclude=['tests']),
      long_description=long_description,
      long_description_content_type="text/markdown",
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ],
      zip_safe=False)