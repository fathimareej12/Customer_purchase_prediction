from components.data_ingestion import load_data










def main():
    data = load_data()
    print('Top 5 values:')
    print(data.head(5))




if __name__ == "__main__":
    main()