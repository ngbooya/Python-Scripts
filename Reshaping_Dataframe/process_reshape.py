import pandas as pd 
import pandas._testing as tm
import numpy as np

tm.N = 3

def unpivot(frame):
    N, K = frame.shape
    data = {'value': frame.to_numpy().ravel('F'),
            'variable': np.asarray(frame.columns).repeat(N),
            'date': np.tile(np.asarray(frame.index), K)}
    return pd.DataFrame(data, columns=['date', 'variable', 'value'])

# df = unpivot(tm.makeTimeDataFrame())

# print("Original dataframe")
# print(df)

# print("\n Pivotted dataframe")
# print(df.pivot(index='date', columns='variable', values='value'))

tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                      'foo', 'foo', 'qux', 'qux'],
                     ['one', 'two', 'one', 'two',
                      'one', 'two', 'one', 'two']]))

index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df = pd.DataFrame(np.random.randn(8,2), index=index, columns=['A','B'])
df2 = df[:4]
print(df)

stacked = df2.stack()
print(stacked)

