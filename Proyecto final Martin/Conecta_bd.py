import pymysql

from ed_categoria import conectar


def recupera_categoria():
    conn = pymysql.connect(host='localhost', user ='root', passwd="", db='ignorancia')
    cursor = conn.cursor()
    cursor.execute('select descripcion from categoria')
    categorias = cursor.fetchall()
    conn.close
    return categorias

def recupera_preguntas(cat):

    conexion = conectar()

    cursor = conexion.cursor()

    consulta = f"""
    SELECT
    id_pregunta,
    pregunta,
    opcion_1,
    opcion_2,
    opcion_3,
    opcion_4,
    correcta
    FROM preguntas
    WHERE categoria = '{cat}'
    """

    cursor.execute(consulta)

    datos = cursor.fetchall()

    conexion.close()

    return datos