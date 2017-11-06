# create a four item Series
import numpy as np
import pandas as pd
from pandas import DataFrame, Series
s = Series([1, 2, 3, 4])
print s


# return a Series with the rows with labels 1 and 3
print s[[1,3]]
