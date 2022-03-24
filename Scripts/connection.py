import psycopg2
import logging
from sshtunnel import SSHTunnelForwarder

logger = logging.getLogger("dbprojekt")

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Connection(metaclass=SingletonMeta):

    def __init__(self, username: str, password: str, dbname: str):
        self.server = SSHTunnelForwarder(('202.61.227.142', 22),
                                    ssh_username=username,
                                    ssh_password=password,
                                    remote_bind_address=('localhost', 5432),
                                    local_bind_address=('localhost', 5432))
        self.server.start()

        self.conn = psycopg2.connect(dbname=dbname, user=username, password=password,
                                host=self.server.local_bind_host, port=self.server.local_bind_port)
        logger.info("Connection established!")

    def getSQLConnection(self):
        return self.conn

    def stopConnection(self):
        self.conn.close()
        self.server.close()
        logger.info("Connection closed!")

