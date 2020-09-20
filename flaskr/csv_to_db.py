import pandas as pd
import sqlite3

df = pd.read_csv('statements.csv')

db = sqlite3.connect('db_statements.db')
c = db.cursor()

c.execute('CREATE TABLE STATEMENTS (Community text, StatementOne text, StatementTwo text, StatementThree text)')
db.commit()

df.to_sql('statements', db)

for row in c.fetchall():
    print (row)