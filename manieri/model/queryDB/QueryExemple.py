import manieri.model.connectorDB.ConnectorMariaFatimaDB as Con
import manieri.model.queryDB.QueryDB as Qry

con = Con.Connector(host='-----host-----',
                    database='-----database-----',
                    user='-----user-----',
                    password='-----password-----')

sql = """ SELECT * FROM PUBLIC."table" """
query = Qry.Query()
print(query.query(con.connect_db(),sql))
