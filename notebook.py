import pandas as pd



def avg_Estimated_Salary():
    df = pd.read_csv('Churn_Modelling.csv')
    sum = 0
    for sal in df['EstimatedSalary']:
        sum  = sum + sal
    sum = sum / 10000
    return {round(sum,0)}

def avg_age_who_Exited():
    df = pd.read_csv('Churn_Modelling.csv')
    sum = 0
    count=0
    for index, row in df.iterrows():
        if row['Exited'] == 1:
            sum = sum + row['Age']
            count = count + 1
    sum = sum / count
    return {round(sum,0)}

def avg_age_who_Not_Exited():
    df = pd.read_csv('Churn_Modelling.csv')
    sum = 0
    count=0
    for index, row in df.iterrows():
        if row['Exited'] == 0:
            sum = sum + row['Age']
            count = count + 1
    sum = sum / count
    return {round(sum,0)}

def avg_Tenure():
    df = pd.read_csv('Churn_Modelling.csv')
    sum = 0
    for index, row in df.iterrows():
        sum = sum + row['Tenure']
    sum = sum / 10000
    return {round(sum,0)}