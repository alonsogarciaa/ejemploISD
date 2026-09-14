/*
 * ModelConstants.java
 * Define las constantes globales del dominio/modelo:
 * - JNDI DataSource Name (ws-javaexamples-ds)
 * - Expiración de ventas (EXPIRATION_DAYS)
 * - URL base de streaming para películas.
 */

package es.udc.ws.movies.model.util;

public final class ModelConstants {

    public static final String MOVIE_DATA_SOURCE = "ws-javaexamples-ds";
    public static final int SALE_EXPIRATION_DAYS = 2;
    public static final String BASE_URL = "http://ws-movies.udc.es/sale/stream/";
    public static final short MAX_RUNTIME = 1000;
    public static final float MAX_PRICE = 1000;

    private ModelConstants() {
    }
}
