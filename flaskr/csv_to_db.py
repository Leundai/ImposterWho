import pandas as pd
from sqlalchemy.types import String

def to_csv():
	df = pd.read_csv('messages.csv', engine='python', encoding='utf-8')
	return df

def to_sql(df, db):
	df.to_sql(name='statements', con=db.engine, index_label='id', if_exists='replace', 
		dtype={
		'community': String(30), 
		'one': String(150),
		'two': String(150),
		'three': String(150)
		}