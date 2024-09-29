package Entregable_2;

import java.util.concurrent.*;

public class ProcesadorPedidos {
    private final ExecutorService procesador;
    private final PriorityBlockingQueue<Pedido> colaPedidos;

    public ProcesadorPedidos(int maxHilos) {
        this.procesador = Executors.newFixedThreadPool(maxHilos);
        this.colaPedidos = new PriorityBlockingQueue<>();
    }

    // getter colaPedidos
    public PriorityBlockingQueue<Pedido> getColaPedidos() {
        return colaPedidos;
    }

    // Agregar un pedido a la cola de pedidos
    public void agregarPedido(Pedido pedido) {
        colaPedidos.offer(pedido);
    }

    // Procesar todos los pedidos de la cola
    public void procesarPedidos() {
        while (!colaPedidos.isEmpty()) {
            Pedido pedido = colaPedidos.poll();  // Extrae el siguiente pedido
            procesador.submit(() -> procesarPedido(pedido));
        }
    }

    // Procesar un solo pedido en las tres etapas
    private void procesarPedido(Pedido pedido) {
        System.out.println("Procesando " + pedido);
        procesarPago(pedido);
        empaquetarPedido(pedido);
        enviarPedido(pedido);
        System.out.println("Pedido completado: " + pedido);
    }

    // Simula la etapa de procesamiento de pago
    private void procesarPago(Pedido pedido) {
        System.out.println("Procesando pago para " + pedido);
        try {
            Thread.sleep(200); // Simula tiempo de procesamiento de pago
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        System.out.println("Pago completado para " + pedido);
    }

    // Simula la etapa de empaquetado (usando ForkJoinPool)
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

    // Simula la etapa de envío
    private void enviarPedido(Pedido pedido) {
        System.out.println("Enviando " + pedido);
        try {
            Thread.sleep(150); // Simula tiempo de envío
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        System.out.println("Envío completado para " + pedido);
    }

    // Cierra el ExecutorService de manera ordenada
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

    public ExecutorService getProcesador() {
        return procesador;
    }
}


