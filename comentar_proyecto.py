import os

# Definición de comentarios por archivo
comentarios = {
    "pom.xml": """<!-- 
  POM Raiz del proyecto ws-javaexamples.
  - Define la versión del modelo POM (4.0.0).
  - Configura el groupId (es.udc.ws) y el artifactId (ws-javaexamples).
  - Incluye los submódulos: ws-jdbctutorial, ws-util y ws-movies.
  - Gestiona propiedades globales (codificación UTF-8, Java 25, versiones de dependencias).
  - Gestiona el plugin de ejecución SQL (MySQL) y el despliegue con Jetty/WAR.
-->
""",
    "README.md": """<!-- 
  Instrucciones de compilación, ejecución y despliegue del proyecto ws-movies:
  - Inicialización de la base de datos con Maven: mvn sql:execute install
  - Ejecución del servicio web Jetty: cd ws-movies/ws-movies-service && mvn jetty:run
  - Comandos para clientes de prueba (exec:java) para añadir, buscar, comprar y borrar películas.
-->
""",
    "MySQLCreateTables.sql": """-- -----------------------------------------------------------------------------
-- Script de creación de la base de datos MySQL para el servicio ws-movies.
-- Elimina y crea las tablas 'Movie' y 'Sale' garantizando la integridad referencial
-- mediante claves foráneas y restricciones CHECK para importes y duraciones.
-- -----------------------------------------------------------------------------
""",
    "ModelConstants.java": """/*
 * ModelConstants.java
 * Define las constantes globales del dominio/modelo:
 * - JNDI DataSource Name (ws-javaexamples-ds)
 * - Expiración de ventas (EXPIRATION_DAYS)
 * - URL base de streaming para películas.
 */
""",
    "MovieService.java": """/*
 * MovieService.java
 * Interfaz de la capa de servicio (Lógica de Negocio).
 * Declara las operaciones disponibles: addMovie, updateMovie, removeMovie, 
 * findMovie, findMovies, buyMovie y findSale.
 */
""",
    "MovieServiceImpl.java": """/*
 * MovieServiceImpl.java
 * Implementación de la interfaz MovieService.
 * Controla el manejo de transacciones JDBC (commit, rollback, nivel SERIALIZABLE),
 * validaciones de parámetros de entrada e interacción con las clases DAO.
 */
""",
    "Jdbc3CcSqlMovieDao.java": """/*
 * Jdbc3CcSqlMovieDao.java
 * Implementación DAO para MySQL que aprovecha los controladores JDBC 3 
 * para la recuperación de claves primarias auto-generadas al insertar películas.
 */
""",
    "AbstractSqlMovieDao.java": """/*
 * AbstractSqlMovieDao.java
 * Clase base abstracta DAO que implementa las operaciones comunes de lectura,
 * actualización y borrado de películas en la base de datos SQL.
 */
""",
    "Movie.java": """/*
 * Movie.java
 * Entidad de dominio / DTO que representa una película en el sistema.
 * Contiene propiedades como movieId, title, duration, price, etc., 
 * junto con constructores, getters, setters, hashCode y equals.
 */
""",
    "Sale.java": """/*
 * Sale.java
 * Entidad de dominio / DTO que representa la compra de una película por parte de un usuario.
 */
""",
    "movies.thrift": """/*
 * movies.thrift
 * Definición del contrato de interfaz RPC usando Apache Thrift.
 * Incluye estructuras de datos (ThriftMovieDto, ThriftSaleDto), excepciones y servicios.
 */
"""
}

def aplicar_comentarios():
    directorio_raiz = os.getcwd()
    archivos_modificados = 0

    for root, dirs, files in os.walk(directorio_raiz):
        for file in files:
            if file in comentarios:
                ruta_completa = os.path.join(root, file)
                comentario = comentarios[file]
                
                with open(ruta_completa, 'r', encoding='utf-8') as f:
                    contenido_original = f.read()

                # Evita duplicar el comentario si ya fue añadido
                if comentario.strip() not in contenido_original:
                    with open(ruta_completa, 'w', encoding='utf-8') as f:
                        f.write(comentario + "\n" + contenido_original)
                    print(f"[+] Comentado: {file}")
                    archivos_modificados += 1
                else:
                    print(f"[-] Ya estaba comentado: {file}")

    print(f"\nProceso completado. Archivos actualizados: {archivos_modificados}")

if __name__ == "__main__":
    aplicar_comentarios()
