# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 15:21:54 2022

@author: jasy9
"""

from distutils.core import setup
setup(
  name = 'Topsis-Jaskirat-101917040',         # How you named your package folder (MyLib)
  packages = ['Topsis-Jaskirat-101917040'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'The Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) is a multi-criteria decision analysis method. TOPSIS is based on the concept that the chosen alternative should have the shortest geometric distance from the positive ideal solution (PIS) and the longest geometric distance from the negative ideal solution (NIS).',   # Give a short description about your library
  author = 'Jaskirat Singh',                   # Type in your name
  author_email = 'jsingh17_be19@thapar.edu',      # Type in your E-Mail
  url = 'https://github.com/jaskirat-singh-0403/Topsis-Jaskirat-101917040',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/jaskirat-singh-0403/Topsis-Jaskirat-101917040/archive/refs/tags/0.1.tar.gz',    # I explain this later on
  keywords = ['TOPSIS', 'Decision Making', 'Package'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'sys',
          'os',
          'pandas',
          'numpy',
          'math',
          'datetime'
          
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)