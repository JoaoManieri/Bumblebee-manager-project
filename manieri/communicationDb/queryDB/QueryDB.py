import manieri.communicationDb.connectorDB.ConnectorMariaFatimaDB as Con
import manieri.communicationDb.queryDB.QueryDB as Qry

class Query:

    def __int__(self):
        print("Classe criada")

    def query(self, connector, sql):
        try:
            con = connector
            cur = con.cursor()
            cur.execute(sql)
            res = cur.fetchall()
            reg = []
            for rec in res:
                reg.append(rec)
            con.close()
            print("Consulta ao banco de dados realizada com sucesso!")
            return reg
        except:
            print("Consulta ao banco de dados falhou!")

    def selectAll(self):
        print("teste")
        #registros = consultar_db(""" SELECT * FROM PUBLIC."testeGeral" """)
        #print(registros)
    pass