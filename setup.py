from setuptools import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()


setup(
  name = 'pylispy',
  packages = ['pylispy'],   # Chose the same as "name"
  version = '0.6.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Basic lisp functions in python',   # Give a short description about your library
  author = 'David Zabner',                   # Type in your name
  author_email = 'david.zabner@gmail.com',      # Type in your E-Mail
  long_description=long_description,
  long_description_content_type='text/markdown',
  url = 'https://github.com/nw0428/pylisp',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/nw0428/pylisp/archive/v_062.tar.gz',    # I explain this later on
  keywords = ['Lisp', 'Lists', 'LISP', 'car', 'cdr', 'cons'],   # Keywords that define your package best
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Education',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
