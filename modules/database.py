import mariadb
import sys


class databaseSQL(object):
    __instance = None

    def __init__(self):
            # inicio de comprobaciones
            try:
                self.__conn = mariadb.connect(
                    user="USERHANDYSUPERMARKET",
                    password="PASSWORD",
                    host="192.168.122.18",
                    port=3306,
                    database="HANDYSUPERMARKET"
                )
            except mariadb.Error as e:
                print(f"Error connecting to a MariaDB: {e}")
                sys.exit(1)

            # Desactivamos los autocommit
            self.__conn.autocommit = False

            self.__cur = self.__conn.cursor()

            # Comprobamos que las tablas existen
            self.__cur.execute("SHOW TABLES")
            self.__cur.fetchall()
            check_tables = self.__cur.rowcount

            if check_tables == 0:
                # Abrimos los ficheros de comprobacion de tablas de la base de datos
                __ddl_file = open("../database/DDL.sql", "r")
                __ddl_text = __ddl_file.read()
                __ddl_list = __ddl_text.split(";")
                # Borramos el ultimo elemento de la lista que es un \n
                __ddl_list.pop()


                __ddl_file.close()

                try:
                    for i in __ddl_list:
                        # execute DDL of tables
                        self.__cur.execute(i)
                        # Commit any pending transaction to database
                        self.__conn.commit()

                except Exception as e:
                    print(f"Error executing a command: {e}")

    def __new__(cls):
        # Comprobacion de singleton
        if databaseSQL.__instance is None:
            databaseSQL.__instance = object.__new__(cls)

        return databaseSQL.__instance



database = databaseSQL()
