from setuptools import setup
with open("README.md","r", encoding="utf-8") as fh:
    long_description=fh.read()
AUTHOR_NAMES= 'Janisa Malaviya', 'Gargi Kishore', 'Fayha Mariyam'
SRC_REPO= 'src'
LIST_OF_REQUIREMENTS= ['vs_code','miniconda','jupyter','pandas','sklearn']
setup(name= SRC_REPO, version= '0.0.1',
      authors=AUTHOR_NAMES, 
      authors_schoolname= 'Rajagiri Public School, Doha, Qatar', 
      description= 'A capstone project which aims to make an A.I. Movie Recommendation model', 
      package= [SRC_REPO], 
      python_requires= ">=3.7", 
      installment_requirements= LIST_OF_REQUIREMENTS)
