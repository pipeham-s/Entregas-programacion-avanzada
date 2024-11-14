package Entregable_2.Code;

/**
 * Clase que representa un pedido con un identificador y un indicador de urgencia.
 */
public class Pedido implements Comparable<Pedido> {
    private int id;
    private boolean urgente;

    /**
     * Constructor de la clase Pedido.
     * @param id Identificador del pedido.
     * @param urgente Indicador de urgencia del pedido.
     */
    public Pedido(int id, boolean urgente) {
        this.id = id;
        this.urgente = urgente;
    }

    /**
     * Método que indica si el pedido es urgente.
     * @return true si el pedido es urgente, false en caso contrario.
     */
    public boolean isUrgente() {
        return urgente;
    }

    /**
     * Método que devuelve el identificador del pedido.
     * @return Identificador del pedido.
     */
    public int getId() {
        return id;
    }

    /**
     * Método que compara dos pedidos para determinar su orden de procesamientoooooo.
     * @param otro Pedido con el que se compara.
     * @return -1 si este pedido es más urgente, 1 si el otro pedido es más urgente, 0 si son iguales.
     */
    @Override
    public int compareTo(Pedido otro) {
        return Boolean.compare(otro.urgente, this.urgente); // Los urgentes primero
    }

    /**
     * Método que devuelve una representación en cadena del pedido.
     * @return Cadena con el identificador y la urgencia del pedido.
     */
    @Override
    public String toString() {
        return "Pedido ID: " + id + " (Urgente: " + urgente + ")";
    }
}