package Entregable_2;

public class Main {
    public static void main(String[] args) {
        // Crear el procesador de pedidos con 10 hilos
        ProcesadorPedidos procesador = new ProcesadorPedidos(10);

        // Crear y agregar pedidos (algunos urgentes)
        procesador.agregarPedido(new Pedido(1, false));
        procesador.agregarPedido(new Pedido(2, true));  // Pedido urgente
        procesador.agregarPedido(new Pedido(3, false));
        procesador.agregarPedido(new Pedido(4, true));  // Pedido urgente
        procesador.agregarPedido(new Pedido(5, false));

        // Procesar todos los pedidos
        procesador.procesarPedidos();

        // Cerrar el procesador de manera ordenada
        procesador.cerrarProcesador();
    }
}
