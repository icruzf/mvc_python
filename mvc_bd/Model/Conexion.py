import pymysql

class Conexion:

    def __init__(self):
        self.servidor="localhost"
        self.bd="senati_bd"
        self.user="root"
        self.clave=""

    def conectar(self):
        try:
            self.conexion=pymysql.connect(self.servidor,self.user,self.clave,self.bd)
            self.cn=self.conexion.cursor()
            print("se conecto a la BD")
        except Exception as e:
            print("Error: ",e)

        # insert, update, delete
    def setEjecutarQuery(self,sql):
        try:
            respuesta=self.cn.execute(sql)
            print("respuesta -->: ",respuesta)
            self.conexion.commit()
            self.conexion.close()
            return 1
        except Exception as ex:
            print("Error: ",ex)
            self.conexion.rollback()
            return 0

        # select
    def getEjecutarQuery(self,sql):
        try:
            self.cn.execute(sql)
            registros=self.cn.fetchall()
            return registros
        except Exception as ex:
            print("Error: ", ex)
            return 0