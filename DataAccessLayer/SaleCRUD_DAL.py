from Model.SaleModel import SaleModel_Class
import pyodbc

class SaleCRUD_Class:
    def registerSale(self,saleObject:SaleModel_Class):
        commandText = 'EXEC [dbo].[RegisterSales] ?,?,?,?,?,?'
        connectionString = 'Driver={SQL Server}; server=DESKTOP-MQ23T45; Database=Pubs; Trusted_Connection=yes'

        params = (saleObject.StoreID, saleObject.OrderNum,saleObject.Date, saleObject.Qty, saleObject.PayTerms, saleObject.TitleID)


        with pyodbc.connect(connectionString) as connection:
                cursor = connection.cursor()
                cursor.execute(commandText, params)
                connection.commit()