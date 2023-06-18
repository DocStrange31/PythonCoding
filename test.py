import os
import random
files=os.listdir('archive')
item=random.choice(files)
print(item)
print(int(item[0]))
print(type(int(item[0])))
