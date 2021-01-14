import pandas as pd
from sqlalchemy import create_engine

def main():
    
    engine = create_engine('mysql+pymysql://root:123!@#@127.0.0.1/teste')

    print('Loading person ...')
    csv_data = pd.read_csv('Person.Person.csv', sep=';', engine='python', header=0)
    csv_data.to_sql(con=engine, index=False, name='person', if_exists='replace')

    print('Loading product ...')
    csv_data = pd.read_csv('Production.Product.csv', sep=';', engine='python', header=0)
    csv_data.to_sql(con=engine, index=False, name='product', if_exists='replace')

    print('Loading special_offer_product ...')
    csv_data = pd.read_csv('Sales.SpecialOfferProduct.csv', sep=';', engine='python', header=0)
    csv_data.to_sql(con=engine, index=False, name='special_offer_product', if_exists='replace')

    print('Loading customer ...')
    csv_data = pd.read_csv('Sales.Customer.csv', sep=';', engine='python', header=0)
    csv_data.to_sql(con=engine, index=False, name='customer', if_exists='replace')

    print('Loading sales_order_header ...')
    csv_data = pd.read_csv('Sales.SalesOrderHeader.csv', sep=';', engine='python', header=0)
    csv_data.to_sql(con=engine, index=False, name='sales_order_header', if_exists='replace')

    print('Loading sales_order_detail ...')
    csv_data = pd.read_csv('Sales.SalesOrderDetail.csv', sep=';', engine='python', header=0)
    csv_data.to_sql(con=engine, index=False, name='sales_order_detail', if_exists='replace')

if __name__ == "__main__":
    main()