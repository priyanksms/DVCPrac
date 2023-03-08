import pandas as pd
from IPython.display import display

print('this is file1')
nbafile = pd.read_csv('data/nba.csv')

display(nbafile)
nbafile.to_csv('data/nba2.csv', index_label=False)
