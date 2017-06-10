# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 11:28:09 2015

@author: Jose
"""

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# create a fake dataframe, repeating the tuple given in the example

df = DataFrame(data={'Observations': np.random.randn(10) * np.arange(10),'Turnstile': (('A006', 'R079', '00-00-04', '5 AVE-59 ST'),)*10})

df = pd.concat([df,DataFrame(df['Turnstile'].tolist())], axis=1, join='outer')

df.head()

df[3]