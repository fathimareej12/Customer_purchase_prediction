import pandas as pd
from config.paths import DATA_PATH
from components.data_ingestion import load_data

def features(data:pd.DataFrame):
    data=data.drop(columns=['customer_id'])

    X=data.drop(columns=['purchase_label'])
    y=data['purchase_label']

    return X,y

def main():

    data=pd.read_csv(DATA_PATH/'customer_purchase_prediction.csv')
    X,y=features(data)
    print(X.shape)
    print(y.shape)


if __name__=='__main__':
    main()