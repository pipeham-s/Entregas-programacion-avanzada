package Entregable_2.Code;

import java.util.concurrent.*;

/**
 * Clase que representa un procesador de pedidos con una cola de pedidos y un ExecutorService.
 * Los pedidos se procesan en tres etapas: pago, empaquetado y envío.
 */
public class ProcesadorPedidos {
    private final ExecutorService procesador;
    private final PriorityBlockingQueue<Pedido> colaPedidos;

    /**
     * Constructor de la clase ProcesadorPedidos.
     * @param maxHilos Número máximo de hilos en el ExecutorService.
     */
    public ProcesadorPedidos(int maxHilos) {
        this.procesador = Executors.newFixedThreadPool(maxHilos);
        this.colaPedidos = new PriorityBlockingQueue<>();
    }

    /**
     * Método que devuelve la cola de pedidos.
     * @return Cola de pedidos.
     */
    public PriorityBlockingQueue<Pedido> getColaPedidos() {
        return colaPedidos;
    }

    /**
     * Método que agrega un pedido a la cola.
     * @param pedido Pedido a agregar.
     */
    public void agregarPedido(Pedido pedido) {
        colaPedidos.offer(pedido);
    }

    /**
     * Método que procesa todos los pedidos en la cola.
     */
    public void procesarPedidos() {
        while (!colaPedidos.isEmpty()) {
            Pedido pedido = colaPedidos.poll();  // Extrae el siguiente pedido
            procesador.submit(() -> procesarPedido(pedido));
        }
    }

    /**
     * Método que procesa un pedido en tres etapas: pago, empaquetado y envío.
     * @param pedido Pedido a procesar.
     */
    private void procesarPedido(Pedido pedido) {
        System.out.println("Procesando " + pedido);
        procesarPago(pedido);
        empaquetarPedido(pedido);
        enviarPedido(pedido);
        System.out.println("Pedido completado: " + pedido);
    }

    /**
     * Método que simula la etapa de pago de un pedido.
     * @param pedido Pedido a procesar.
     */
    private void procesarPago(Pedido pedido) {
        System.out.println("Procesando pago para " + pedido);
        try {
            Thread.sleep(200); // Simula tiempo de procesamiento de pago
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        System.out.println("Pago completado para " + pedido);
    }

    /**
     * Método que simula la etapa de empaquetado de un pedido.
     * @param pedido Pedido a procesar.
     */
    private void empaquetarPedido(Pedido pedido) {
        ForkJoinPool.commonPool().submit(() -> {
            System.out.println("Empaquetando " + pedido);
            try {
                Thread.sleep(300); // Simula tiempo de empaquetado
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            System.out.println("Empaquetado completado para " + pedido);
        }).join();
    }

    /**
     * Método que simula la etapa de envío de un pedido.
     * @param pedido Pedido a procesar.
     */
    private void enviarPedido(Pedido pedido) {
        System.out.println("Enviando " + pedido);
        try {
            Thread.sleep(150); // Simula tiempo de envío
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        System.out.println("Envío completado para " + pedido);
    }

    /**
     * Método que cierra el procesador de pedidos de manera ordenada.
     */
    public void cerrarProcesador() {
        procesador.shutdown();
        try {
            if (!procesador.awaitTermination(60, TimeUnit.SECONDS)) {
                procesador.shutdownNow();
            }
        } catch (InterruptedException e) {
            procesador.shutdownNow();
        }
    }

    /**
     * Método que devuelve el ExecutorService del procesador.
     * @return ExecutorService del procesador.
     */
    public ExecutorService getProcesador() {
        return procesador;
    }
}