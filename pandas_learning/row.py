#head(), tail()
#head(n) default 5
#tail(n) default 5
import pandas as pd
df = pd.read_json("sample_Data.json")

print('Display 10 rows of first')
print(df.head(10))



print('Display 10 rows of last')
print(df.tail(10))



 