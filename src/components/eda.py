import pandas as pd

def basic_eda(data:pd.DataFrame):
    print('Exploratory data analysis'.center(50))
    print('=' * 50)

    print(f'Dataset shape: {data.shape}')
    print('\n Target variable Distribution')
    print(data['purchase_label'].value_counts())

    print('\n Numerical variable distribution')
    print(data.describe())

    print('\n device')
    print(data['traffic_source'].value_counts())

    print('\n Age Distribution')
    print(data['age'].value_counts())

    print(pd.crosstab(data['product_category'], data['purchase_label']))


def main():
    from data_ingestion import load_data

    data=load_data()
    basic_eda(data)

if __name__ == '__main__':
    main()