import psycopg2

class Connector:

    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def connect_db(self):
        try:
            return psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
            print("[LOG:connector_maria_fatima] Connection failure!")
        except:
            print("[LOG:connector_maria_fatima] Successful connection!")

    pass
