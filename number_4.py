#question 4 Create a dataframe with 10 rows and 3 columns, where the values are random numbers between 1 and 10 (inclusive). 
#Then, replace all values greater than 5 with the value 10.

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(0,11, size=(10, 3)), columns=['col1', 'col2', 'col3'])
df = df.replace(['6', '7', '8', '9'], '10')
print(df)
