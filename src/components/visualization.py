import os
import matplotlib.pyplot as plt
import pandas as pd
from config.paths import CHART_PATH


def save_bar(series,title,filename,xlabel='',ylabel='count'):
    plt.figure(figsize=(10,5))
    plt.bar(series.index,series.values)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.tight_layout()
    plt.savefig(os.path.join(CHART_PATH,filename))
    plt.close()

def save_histogram(series,title,filename,bins=10):
    plt.figure(figsize=(10,5))
    plt.hist(series,bins=bins)
    plt.title(title)
    plt.xlabel(series.name)
    plt.ylabel('Frequency')

    plt.tight_layout()
    plt.savefig(os.path.join(CHART_PATH,filename))
    plt.close()

def save_scatter(x_series,y_series,title,filename,xlabel='',ylabel=''):
    plt.figure(figsize=(10,5))
    plt.scatter(x_series,y_series)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(os.path.join(CHART_PATH,filename))

    plt.close()



def create_visuals(data:pd.DataFrame):

    print(data['purchase_label'].value_counts())
    save_bar(data['purchase_label'].value_counts(),
                   title='purchase label Distribution',
                   filename='purchase_label_distribution.png')




    save_histogram(data['age'],
                   title='Histogram of Age',
                   filename='histogram_of_Age.png')


    save_scatter(data['age'],data['annual_income'],
                 title='Age and Annual Income',
                 filename='Age_and_annual_income_distribution.png')



def main():
    from src.components.data_ingestion import load_data
    data=load_data()

    create_visuals(data)

if __name__=='__main__':
    main()

