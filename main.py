import pandas as pd
from sqlalchemy import create_engine
df = pd.read_excel('./Customer_Shopping_Dataset_6000.xlsx')
print(df.head())
print(df.info())
print(df.describe())
df['Size'] = df.groupby('Item Purchased')['Size'].transform(lambda x :x.fillna(x.mode()[0]))
print(df.isnull().sum())
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(" ","_")
print(df.columns)

# create a age group column

lables = ["young adult","adult","middle-aged","senior"]
df['age group'] = pd.qcut(df['age'],q = 4,labels=lables)
print(df[['age','age group']].head(15))

#create column purchase frequenc 

frequenc_maping = {
    'fortnightly':14,
    'weekly':7,
    'monthly':30,
    'Quarterly':90,
    'Bi-weekly':14,
    'Annually':365,
    'every 3 month':90
}

df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequenc_maping)
print(df[['purchase_frequency_days','frequency_of_purchases']].head())
print(df[['discount_applied', 'promo_code_used']].head(10))

a = df['discount_applied'] == df['promo_code_used']

print(a.all())

host = "localhost"
port = "3306"
user = "root"
password = "Kaushal_2004"
database = "project"


engin = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")

table_name = "customer"
df.to_sql(table_name,engin,if_exists="replace",index=False)

print(f"connected to {database} and data stored in {table_name}")






