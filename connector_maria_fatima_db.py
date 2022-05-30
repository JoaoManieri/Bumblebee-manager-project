import psycopg2

def conecta_db():
    try:
        con = psycopg2.connect(host='-------hostlink--------',
                             database='-------db--------',
                             user='-------user--------',
                             password='-------pwrd--------')
        print("Conexão com banco de dados bem sucedida!")
        return con
    except:
        print("Conexão com banco de dados falhou sucedida!")


def consultar_db(sql):
    try:
        con = conecta_db()
        cur = con.cursor()
        cur.execute(sql)
        recset = cur.fetchall()
        registros = []
        for rec in recset:
            registros.append(rec)
        con.close()
        print("Consulta ao banco de dados realizada com sucesso!")
        return registros
    except:
        print("Consulta ao banco de dados falhou!")

registros  = consultar_db(""" SELECT * FROM PUBLIC."testeGeral" """)
print(registros)

