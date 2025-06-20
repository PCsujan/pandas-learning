import pandas as pd


data = {
    "Name":['Ram', 'shyam', 'Ghanshyam'],
    "Age":[10,20,30],
    "City":['Nagpur', 'mumbai', 'Delhi']
}

df = pd.DataFrame(data)

print('Display the info of data set')
print(df.info())

