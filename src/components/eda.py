import pandas as pd
import os

Artifacts_path="../artifacts/reports"
os.makedirs(Artifacts_path,exist_ok=True)

def basic_eda(data:pd.DataFrame):
    print('Exploratory data analysis'.center(50))
    print('=' * 50)

    print(f'Dataset shape: {data.shape}')
    print('\n Target variable Distribution')
    print(data['purchase_label'].value_counts())

    print('\n Numerical variable distribution')
    print(data.describe())

    print('\n traffic source distribution')
    print(data['traffic_source'].value_counts())

    print('\n Age Distribution')
    print(data['age'].value_counts())

    print(pd.crosstab(data['product_category'], data['purchase_label']))

    with open('dataset_summary.txt', 'w') as file:
        print('\n Started \n')
        file.write('\n Exploratory data analysis'.center(50))
        file.write('\n' +'=' * 50)
        print('\n Mid \n')
        file.write(f'\n Dataset shape: {data.shape}')
        file.write('\n Target variable Distribution \n')
        file.write(str(data['purchase_label'].value_counts()))
        file.write('\n traffic source distribution')
        file.write(str(data['traffic_source'].value_counts()))

        file.write('\n Age Distribution')
        file.write(str(data['age'].value_counts()))
0


def main():
    from data_ingestion import load_data

    data=load_data()
    basic_eda(data)

if __name__ == '__main__':
    main()