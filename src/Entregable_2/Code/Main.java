package Entregable_2.Code;

/**
 * Clase principal que crea un procesador de pedidos y agrega 100 pedidos a la cola.
 * Luego, procesa todos los pedidos y mide el tiempo total de procesamiento.
 */
public class Main {
    /**
     * Método principal que crea un procesador de pedidos y agrega 100 pedidos a la cola.
     * Luego, procesa todos los pedidos y mide el tiempo total de procesamiento.
     * @param args Argumentos de la línea de comandos (no se utilizan)
     */
    public static void main(String[] args) {
        // Crear el procesador de pedidos con 10 hilos
        ProcesadorPedidos procesador = new ProcesadorPedidos(7);

        // Crear y agregar 100 pedidos (con algunos urgentes)
        for (int i = 1; i <= 100; i++) {
            boolean esUrgente = (i % 4 == 0);  // Condición para pedidos urgentes
            Pedido pedido = new Pedido(i, esUrgente);
            procesador.agregarPedido(pedido);
        }

        // Procesar todos los pedidos y medir el tiempo
        long startTime = System.currentTimeMillis();
        procesador.procesarPedidos();

        // Cerrar el procesador de manera ordenada
        procesador.cerrarProcesador();

        long endTime = System.currentTimeMillis();
        System.out.println("\nTiempo total de procesamiento: " + (endTime - startTime) + " ms");
    }
}
