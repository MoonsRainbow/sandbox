import pymysql


class DataBaseConnManager:
    __conn = pymysql.connect

    def __init__(self, _host: str, _port: str, _user: str, _pw: str, _db: str = None):
        self.__host = _host
        self.__port = _port
        self.__user = _user
        self.__password = _pw
        self.__database = _db
        self.__re_execute_count = 5

    @property
    def host(self):
        return 'For security reasons, we do not provide any information.'

    @host.setter
    def host(self, _host: str):
        self.__host = _host

    @property
    def port(self):
        return 'For security reasons, we do not provide any information.'

    @port.setter
    def port(self, _port: str):
        self.__port = _port

    @property
    def user(self):
        return 'For security reasons, we do not provide any information.'

    @user.setter
    def user(self, _user: str):
        self.__user = _user

    @property
    def password(self):
        return 'For security reasons, we do not provide any information.'

    @password.setter
    def password(self, _pw: str):
        self.__password = _pw

    @property
    def database(self):
        return 'For security reasons, we do not provide any information.'

    @database.setter
    def database(self, _db):
        self.__database = _db

    @property
    def conn(self):
        return self.__conn

    def connecting(self):
        self.__conn = pymysql.connect(
            host=self.__host,
            port=self.__port,
            user=self.__user,
            password=self.__password,
            database=self.__database
        )

    def disconnecting(self):
        self.__conn.close()

    def execute_query(self, _sql):
        _sql = _sql.replace("    ", "").replace("        ", "").replace("            ", "").replace("\n", " ")
        _result = None
        with self.conn.cursor() as _conn:
            _conn.execute(_sql)
            self.conn.commit()

            if _sql.lower().strip().startswith("insert", 0):
                _result = _conn.lastrowid
            else:
                _result = _conn.fetchall()
        return _result



