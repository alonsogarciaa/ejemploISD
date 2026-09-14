-- -----------------------------------------------------------------------------
-- Script de creación de la base de datos MySQL para el servicio ws-movies.
-- Elimina y crea las tablas 'Movie' y 'Sale' garantizando la integridad referencial
-- mediante claves foráneas y restricciones CHECK para importes y duraciones.
-- -----------------------------------------------------------------------------

-- ----------------------------------------------------------------------------
-- JDBC Tutorial.
-------------------------------------------------------------------------------

DROP TABLE IF EXISTS TutMovie;
CREATE TABLE TutMovie ( movieId VARCHAR(40) COLLATE latin1_bin NOT NULL,
    title VARCHAR(255) COLLATE latin1_bin NOT NULL,
    runtime SMALLINT NOT NULL,
    CONSTRAINT TutMoviePK PRIMARY KEY(movieId)) ENGINE = InnoDB;
