package Entregable_2.Code;

/**
 * Representa un pedido en el sistema de procesamiento de pedidos.
 * Cada pedido tiene un ID y un estado que indica si es urgente o no.
 */
public class Pedido implements Comparable<Pedido> {
    private int id;
    private boolean urgente;

    /**
     * Crea un nuevo pedido.
     *
     * @param id El identificador único del pedido.
     * @param urgente Indica si el pedido es urgente.
     */
    public Pedido(int id, boolean urgente) {
        this.id = id;
        this.urgente = urgente;
    }

    /**
     * Verifica si el pedido es urgente.
     *
     * @return true si el pedido es urgente, de lo contrario, false.
     */
    public boolean isUrgente() {
        return urgente;
    }

    /**
     * Obtiene el identificador del pedido.
     *
     * @return El identificador del pedido.
     */
    public int getId() {
        return id;
    }

    /**
     * Compara este pedido con otro para ordenarlos en la cola de prioridad.
     *
     * @param otro Otro pedido para comparar.
     * @return Un valor negativo, cero o positivo si este pedido es mayor, igual o menor que el otro.
     */
    @Override
    public int compareTo(Pedido otro) {
        return Boolean.compare(otro.urgente, this.urgente); // Los urgentes primero
    }

    /**
     * Devuelve una representación en cadena del pedido.
     *
     * @return Una cadena con el ID y si es urgente.
     */
    @Override
    public String toString() {
        return "Pedido ID: " + id + " (Urgente: " + urgente + ")";
    }
}