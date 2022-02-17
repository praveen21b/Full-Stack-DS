""" 
EDA - Explotary Data Analysis
- Understanding about the dat
- Plotting techniques
- Handling missing values
- 

"""

# Importing Libraries
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline ## to display all the plots

from sklearn.datasets import load_iris

"""iris = load_iris()
iris"""


iris = sns.load_dataset('iris')
iris.head()
