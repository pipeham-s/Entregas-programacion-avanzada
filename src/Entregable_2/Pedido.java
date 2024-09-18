package Entregable_2;

public class Pedido implements Comparable<Pedido> {
    private int id;
    private boolean urgente;

    public Pedido(int id, boolean urgente) {
        this.id = id;
        this.urgente = urgente;
    }

    public boolean isUrgente() {
        return urgente;
    }

    public int getId() {
        return id;
    }

    @Override
    public int compareTo(Pedido otro) {
        return Boolean.compare(otro.urgente, this.urgente); // Los urgentes primero
    }

    @Override
    public String toString() {
        return "Pedido ID: " + id + " (Urgente: " + urgente + ")";
    }
}