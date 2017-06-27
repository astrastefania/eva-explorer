""" Exploring EVA data set
    source: https://data.nasa.gov/Raw-Data/Extra-vehicular-Activity-EVA-US-and-Russia/9kcy-zwvn
    Extra-vehicular Activity (EVA) - US and Russia
    Activities done by an astronaut or cosmonaut outside a spacecraft beyond the Earth's appreciable atmosphere.

    Other documentation to include: https://spaceflight.nasa.gov/shuttle/reference/faq/eva.html
    Records: https://en.wikipedia.org/wiki/List_of_cumulative_spacewalk_records
        1. Anatoly Solovyev (RSA): 82h 22' in 16 EVAs
        2. Michael Lopez-Alegria (NASA): 67h 40' in 10 EVAs

    NASA National Aeronautics and Space Administration
    RSA Roscosmos State Corporation
"""

# Libraries
import numpy as np  

import pandas as pd
import matplotlib.pyplot as plt
from eva_dataset_cleaner import eva_dataset_cleaner

df_eva_original = pd.read_csv('Extra-vehicular_Activity__EVA__-_US_and_Russia.csv')

df_eva = pd.read_csv('Extra-vehicular_Activity__EVA__-_US_and_Russia.csv')
eva_dataset_cleaner(df_eva)

# Exploring the dataset
print(df_eva_original.head(3))

print(df_eva.head(3))
print(df_eva.tail(3))
print(df_eva.columns)
print(df_eva.shape)


# Visualising some data

# Graph 1
df_eva.plot(x='EVA #', y='Duration', kind='hist', bins=30)

plt.xlabel('EVA no.')
plt.ylabel('Time spent out in the space')
plt.show()

# Graph 2
#plt.plot( x='EVA #', y='Duration')
#plt.show()