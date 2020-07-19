"""  
将以下 SQL 语句翻译成 pandas 语句
"""


# 1. SELECT * FROM data;
df  
# 2. SELECT * FROM data LIMIT 10;
df = df.head(10)
# 3. SELECT id FROM data;  //id 是 data 表的特定一列
df = df['id']
# 4. SELECT COUNT(id) FROM data;
df = df['id'].count()
# 5. SELECT * FROM data WHERE id<1000 AND age>30;
df[ (df['id'] < 1000) & (df['age'] > 30)]
# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
table1.drop_duplicates('order_id',inplace=True)
for group in table1.groupby('id'):
    print(group)
# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
table1.merge(table2,how='inner',on='id')
# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
table1.merge(table2,how='outer')
pd.concat([table1,table2])
# 9. DELETE FROM table1 WHERE id=10;
del table1[table1['id'] == 10]
# 10. ALTER TABLE table1 DROP COLUMN column_name;
table1.drop(['column_name'],axis=1)