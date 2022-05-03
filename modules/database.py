import mariadb
import sys

class dmlContainer:
    def __init__(self, header = None, body = None):
        self.__header = header
        self.__body = body

    def getHeaderTable(self):
        return self.__header

    def getBodyTable(self):
        return self.__body

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
                    self.__conn.rollback()

            # Destruimos el cursor para la
            self.__cur.close()

    def __new__(cls):
        # Comprobacion de singleton
        if databaseSQL.__instance is None:
            databaseSQL.__instance = object.__new__(cls)

        return databaseSQL.__instance

    def __del__(self):
        # Destruimos la conexion con SQL
        self.__conn.close()

    # QUERY INSERT
    # TABLE INTO TABLE (COLUMN, COLUM2, COLUMN3)
    # CLAUSE VALUES (1,2,3) VALUE > 10
    def queryTransact(self, query = None, table = None, clause = None):
        try:
            # Check
            if (query != None and table != None and clause != None):
                concatenateSQL = query + " " + table + " " + clause
            else: # No hay comando de SQL Valido desde la entrada de string, esto no significa que el comando en sí sea correcto si no que es None
                raise Exception("No se ha introducido el SQL correctamente")
        except Exception as e:
            print (e.args)

        try:
            # Creamos el cursor
            self.__cur =  self.__conn.cursor()
            # Execution
            self.__cur.execute(concatenateSQL)
        except Exception as e:
            print(f"Error executing: {e}")
            self.__conn.rollback()

        self.__conn.commit()
        self.__cur.close()

    # QUERY SELECT *
    # TABLE FROM TABLE
    # CLAUSE WHERE VALUE > 10 OPCIONAL
    def queryConsultas(self, query = None, table = None, clause = None):
        try:
            # Check
            if (query != None and table != None):
                concatenateSQL = query + " " + table
                if (clause != None):
                    concatenateSQL += " " + clause
            else: # No hay comando de SQL Valido desde la entrada de string, esto no significa que el comando en sí sea correcto si no que es None
                raise Exception("No se ha introducido el SQL correctamente")
        except Exception as e:
            print (e.args)

        try:
            # Creamos el cursor
            self.__cur =  self.__conn.cursor()
            # Execution
            self.__cur.execute(concatenateSQL)

            # Obteniendo la informacion de la tabla
            fetch_return_body = self.__cur.fetchall()
            # Obteniendo los nombres de las columnas Cabecera de la tabla
            fetch_return_header = [ x[0] for x in self.__cur.description ]
            # Almacenando en contenedor para ser procesado fuera
            returndml = dmlContainer(fetch_return_header, fetch_return_body)
        except Exception as e:
            print(f"Error executing: {e}")

        self.__cur.close()

        return returndml


#database = databaseSQL()

#query = "INSERT"
#table = "INTO PASILLOS"
#clause = "VALUES ('CARNICERIA02', 'CARNICERIA', 'ESTE ES EL PASILLO DE CARNICERIA DEL SUPERMERCADO', 'http://192.168.122.18')"

#database.queryTransact(query, table, clause)

#query = "SELECT *"
#table = "FROM PASILLOS"
#clause = "WHERE COD_QR_PASILLO = 'CARNICERIA04'"


#resultConsulta = database.queryConsultas(query, table, clause)

# Imprimir las filas Tamanio para sacarlo por el for
#print(len(resultConsulta.getBodyTable()))

# Imprimir las columanas tamanio
#print(len(resultConsulta.getBodyTable()[0]))


# Imprimir tabla Head
#print(*resultConsulta.getHeaderTable(), sep = " ")
#for i in resultConsulta.getBodyTable():
#    print(*i, sep = " ")

#print("\n")
