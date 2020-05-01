# importing libraiers
import pandas as pd
import numpy as np
a = [[1,3,3,4,3],
        [2,3,1,3,3],
        [3,1,2,7,1],
        [3,4,4,3,3]]

# converting them into an readable format
rc=pd.DataFrame(a)
print(rc)

# renaming the col in order to better execute the solution
col=['R0','R1','R2','R3','R4']
rc.columns=col
print(rc)

# calculating the sum of 3's in the column
column=np.sum(rc==3)
column_answer=list(column)
print("The total number of 3's in a column are: ",column_answer)

# calculating the sum of 3's in the rows
rows=(np.sum(rc==3,axis=1))
rows_answer=list(rows)
print("The total number of 3's in a row are:   ",rows_answer)