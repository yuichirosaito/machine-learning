import pandas as pd
from sklearn.linear_model import LinearRegression

def calc(new_scores, new_times):

    df=pd.read_csv('chinese-level2.csv')

    xcol=['得点','学習時間']

    x=df[xcol]
    t=df['級数']

    model=LinearRegression()
    model.fit(x, t)

    new=[[new_scores, new_times]]
    w=model.predict(new)
    r=float(w)
    return round(r)