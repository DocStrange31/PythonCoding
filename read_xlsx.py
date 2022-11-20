import pandas as pd

fpath=input(r'Enter File Path:')
a=pd.read_excel(fpath)
print(a)