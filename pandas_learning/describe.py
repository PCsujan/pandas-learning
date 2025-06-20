# step-1 sample data frame

import pandas as pd

data = {
    "Name":['Ram', 'shyam', 'Ghanshyam', 'Dhanshyam', 'Aditi', 'jagdish','Raj','simran'],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000, 60000, 45000, 52000,49000,70000,48000,58000],
    "preformance Score":[85,90,78,92,88,95,80,89]
     
}

df = pd.DataFrame(data)
print('Descriptive Statistics')
print(df.describe)