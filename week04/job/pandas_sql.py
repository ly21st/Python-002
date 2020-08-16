# 1. SELECT * FROM data;

# 2. SELECT * FROM data LIMIT 10;

# 3. SELECT id FROM data;  //id 是 data 表的特定一列

# 4. SELECT COUNT(id) FROM data;

# 5. SELECT * FROM data WHERE id<1000 AND age>30;

# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;

# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;

# 8. SELECT * FROM table1 UNION SELECT * FROM table2;

# 9. DELETE FROM table1 WHERE id=10;

# 10. ALTER TABLE table1 DROP COLUMN column_name;

import pandas as pd
import numpy as np

df = pd.DataFrame({"A": [5, 3, None, 4],
                   "B": [None, 2, 4, 3],
                   "C": [4, 3, 8, 5],
                   "D": [5, 4, 2, None]})

data = pd.DataFrame({
    "id": np.random.randint(10, 2000, 10),
    "salary": np.random.randint(5, 50, 10),
    "age": np.random.randint(15, 50, 10)
})

table1 = pd.DataFrame({
    "id": np.random.randint(10, 15, 10),
    "salary": np.random.randint(5, 50, 10),
    "age": np.random.randint(15, 50, 10)
})

table2 = pd.DataFrame({
    "id": np.random.randint(10, 20, 10),
    "english": np.random.randint(5, 50, 10),
    "math": np.random.randint(15, 50, 10)
})


def select_all(df):
    """
    1. SELECT * FROM data;
    """
    print(df)
    print(df[:])


def select_limit(df, n):
    """
    2. SELECT * FROM data LIMIT 10;
    """
    print(df[:n])
    print(df.loc[:n - 1])


def select_col(df, cols):
    """
    3. SELECT id FROM data;  //id 是 data 表的特定一列
    """
    print(df[cols])


def select_count(df, col):
    """
    4. SELECT COUNT(id) FROM data;
    """
    print(df[col].count())


def select_where(df, cond):
    """
    5. SELECT * FROM data WHERE id<1000 AND age>30;
    """
    print(df[cond])


def select_groupby(df):
    """
    6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
    """
    print(df.groupby('id').agg({'id': 'count'}))


def select_join(table1, table2, col, how):
    """
    7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
    """
    print(pd.merge(table1, table2, on=col, how=how))


def select_union(table1, table2):
    """
    8. SELECT * FROM table1 UNION SELECT * FROM table2;
    """
    print(pd.concat([table1, table2]).drop_duplicates())


def delete_row(df, cond):
    """
    9. DELETE FROM table1 WHERE id=10;
    """
    print(df[cond])


def delete_col(df, col):
    """
    10. ALTER TABLE table1 DROP COLUMN column_name;
    """
    print(df.drop(col, axis=1))


if __name__ == '__main__':
    select_all(df)
    print("----------")

    select_limit(df, 2)
    print("----------")

    select_col(df, ['A', 'C'])
    print("----------")

    select_count(df, 'A')
    print("----------")

    select_where(data, (data['id'] < 1000) & (data['age'] > 30))
    print("----------")

    select_groupby(data)
    print("----------")

    select_join(table1, table2, 'id', "inner")
    print("----------")

    select_union(table1, table2)
    print("----------")

    delete_row(table1, table1['id'] != 10)
    print("----------")

    delete_col(table1, 'id')
    print("----------")
