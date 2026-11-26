import pandas as pd
from components.data_ingestion import load_data
from components.visualization import create_visuals

def dataset_check(data: pd.DataFrame):
    '''
       Performs basic dataset check
       '''

    print('\n' + '*' * 50)
    print('Dataset overview')
    print('*' * 60)

    print(f'Shape: {data.shape}')

    print('\n columns of dataframe \n')
    print(data.columns.tolist())

    print('\n Missing values in dataframe\n')
    print(data.isnull().sum())

    print('\n Duplicated values in dataframe\n')
    print(data.duplicated().sum())

    print('\n Mean of annual income \n')
    print(data['annual_income'].mean)

    data = data[data['annual_income'] <= 200000]
    print('filtered shape:', data.shape)

    return data

def main():
      data = load_data()
      data=dataset_check(data)
      create_visuals(data)


if __name__ == '__main__':
    main()
