import pymysql


class DataBaseConnManager:
    """
    This class stores database connection information and creates a database connection with the stored information.

    Sends sql to the database through the created database connection and returns the sql execution result.

    :cvar __conn: pymysql Connection class or created instance.
    """
    __conn = pymysql.connect

    def __init__(self, _host: str, _port: str, _user: str, _pw: str, _db: str = None):
        """
        This method is called upon creation of this class.

        Receives database connection information as a parameter and saves it.

        Stored information cannot be verified.

        -----
        :param _host: Host ip in str format.
        :param _port: Port number in str format.
        :param _user: User Name in str format.
        :param _pw: Password in str format.
        :param _db: Database (or schema) name in str format. It's not required. Default is None.
        """
        self.__host = _host
        self.__port = _port
        self.__user = _user
        self.__password = _pw
        self.__database = _db

    @property
    def host(self):
        """Get host information. However, for security reasons, we do not provide any information here."""
        return "Can't provide host information."

    @host.setter
    def host(self, _host: str):
        """Set the new host information to the entered str type _host."""
        self.__host = _host

    @property
    def port(self):
        """Get port information. However, for security reasons, we do not provide any information here."""
        return "Can't provide port information."

    @port.setter
    def port(self, _port: str):
        """Set the new host information to the entered str type _port."""
        self.__port = _port

    @property
    def user(self):
        """Get user information. However, for security reasons, we do not provide any information here."""
        return "Can't provide user information."

    @user.setter
    def user(self, _user: str):
        """Set the new host information to the entered str type _user."""
        self.__user = _user

    @property
    def password(self):
        """Get password information. However, for security reasons, we do not provide any information here."""
        return "Can't provide password information."

    @password.setter
    def password(self, _pw: str):
        """Set the new host information to the entered str type _password."""
        self.__password = _pw

    @property
    def database(self):
        """Get database information. However, for security reasons, we do not provide any information here."""
        return "Can't provide database information."

    @database.setter
    def database(self, _db):
        """Set the new host information to the entered str type _database."""
        self.__database = _db

    @property
    def conn(self):
        """Get pymysql's Connection Class or Object"""
        return self.__conn

    def connecting(self):
        """Create a database connection."""
        self.__conn = pymysql.connect(
            host=self.__host,
            port=self.__port,
            user=self.__user,
            password=self.__password,
            database=self.__database
        )

    def disconnecting(self):
        """Close database connection."""
        self.__conn.close()

    def execute_query(self, _sql):
        """
        Sends the sql to the database through the connection that created the sql.
        Return the result of executing sql in the database.

        -----
        :param _sql: Sub-Query-Language to query the database. It's must be str type.


        -----
        :returns:
            If SQL statement is 'Insert', return lastrowid(It's int type).
            Else return the result of the SQL(maybe, it's tuple type).
        """
        _result = None
        with self.conn.cursor() as _conn:
            _conn.execute(_sql)
            self.conn.commit()
            if _sql.lower().strip().startswith("insert", 0):
                _result = _conn.lastrowid
            else:
                _result = _conn.fetchall()
        return _result



