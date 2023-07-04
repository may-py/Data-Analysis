import dbf
import pandas as pd

table = dbf.Table('data.dbf')

table.open(dbf.READ_ONLY)

df = pd.DataFrame(table)

df.columns = table.field_names

print(df.head)
