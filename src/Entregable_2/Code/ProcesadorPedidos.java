package Entregable_2.Code;

import java.util.concurrent.*;

/**
 * Procesador de pedidos con un número fijo de hilos que permite la ejecución
 * concurrente de pedidos, priorizando los urgentes.
 */
public class ProcesadorPedidos {
    private final ExecutorService procesador;
    private final PriorityBlockingQueue<Pedido> colaPedidos;

    /**
     * Crea un procesador de pedidos con el número máximo de hilos especificado.
     *
     * @param maxHilos Número máximo de hilos en el pool de ejecución.
     */
    public ProcesadorPedidos(int maxHilos) {
        this.procesador = Executors.newFixedThreadPool(maxHilos);
        this.colaPedidos = new PriorityBlockingQueue<>();
    }

    /**
     * Obtiene la cola de pedidos del procesador.
     *
     * @return La cola de pedidos.
     */
    public PriorityBlockingQueue<Pedido> getColaPedidos() {
        return colaPedidos;
    }

    /**
     * Agrega un pedido a la cola para ser procesado.
     *
     * @param pedido El pedido a agregar a la cola.
     */
    public void agregarPedido(Pedido pedido) {
        colaPedidos.offer(pedido);
    }

    /**
     * Procesa todos los pedidos de la cola de manera concurrente.
     */
    public void procesarPedidos() {
        while (!colaPedidos.isEmpty()) {
            Pedido pedido = colaPedidos.poll();  // Extrae el siguiente pedido
            procesador.submit(() -> procesarPedido(pedido));
        }
    }

    /**
     * Procesa un pedido en tres etapas: pago, empaquetado y envío.
     *
     * @param pedido El pedido a procesar.
     */
    private void procesarPedido(Pedido pedido) {
        System.out.println("Procesando " + pedido);
        procesarPago(pedido);
        empaquetarPedido(pedido);
        enviarPedido(pedido);
        System.out.println("Pedido completado: " + pedido);
    }

    /**
     * Simula la etapa de pago.
     *
     * @param pedido El pedido para el que se realiza el pago.
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
     * Simula la etapa de empaquetado usando ForkJoinPool.
     *
     * @param pedido El pedido para el que se realiza el empaquetado.
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
     * Simula la etapa de envío.
     *
     * @param pedido El pedido para el que se realiza el envío.
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
     * Cierra el procesador de pedidos de manera ordenada.
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
     * Obtiene el ExecutorService del procesador.
     *
     * @return El ExecutorService del procesador.
     */
    public ExecutorService getProcesador() {
        return procesador;
    }
}