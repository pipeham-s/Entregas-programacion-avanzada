package Entregable_2.Test;

import Entregable_2.Pedido;
import Entregable_2.ProcesadorPedidos;
import org.junit.jupiter.api.Test;

import java.util.concurrent.PriorityBlockingQueue;

import static org.junit.jupiter.api.Assertions.*;

public class TestPedidos {

    @Test
    public void testAgregarPedidoUrgente() {
        ProcesadorPedidos procesador = new ProcesadorPedidos(5);
        Pedido pedidoUrgente = new Pedido(1, true);
        Pedido pedidoNormal = new Pedido(2, false);

        procesador.agregarPedido(pedidoNormal);
        procesador.agregarPedido(pedidoUrgente);

        // Aseguramos que el pedido urgente se procesa primero
        assertTrue(pedidoUrgente.compareTo(pedidoNormal) < 0);

        procesador.cerrarProcesador();
    }

    @Test
    public void testPrioridadPedidos() {
        ProcesadorPedidos procesador = new ProcesadorPedidos(7);
        for (int i = 1; i <= 10; i++) {
            procesador.agregarPedido(new Pedido(i, i % 2 == 0));
        }

        Pedido primerPedido = procesador.getColaPedidos().peek();
        assertTrue(primerPedido.isUrgente(), "El primer pedido en ser procesado debe ser urgente.");

        procesador.cerrarProcesador();
    }


    @Test
    public void testProcesamientoCorrecto() {
        ProcesadorPedidos procesador = new ProcesadorPedidos(5);

        Pedido pedido1 = new Pedido(1, false);
        Pedido pedido2 = new Pedido(2, true);

        procesador.agregarPedido(pedido1);
        procesador.agregarPedido(pedido2);

        procesador.procesarPedidos();
        procesador.cerrarProcesador();

        assertNull(procesador.getColaPedidos().poll());
    }

    @Test
    public void testAgregarPedido() {
        ProcesadorPedidos procesador = new ProcesadorPedidos(7);
        Pedido pedidoUrgente = new Pedido(1, true);
        Pedido pedidoNormal = new Pedido(2, false);

        procesador.agregarPedido(pedidoNormal);
        procesador.agregarPedido(pedidoUrgente);

        // Comprobar que el pedido urgente es el primero en la cola
        assertEquals(pedidoUrgente, procesador.getColaPedidos().peek(), "El pedido urgente debe ser el primero en ser procesado.");
        procesador.cerrarProcesador();
    }

    @Test
    public void testCierreDelProcesador() {
        ProcesadorPedidos procesador = new ProcesadorPedidos(7);
        procesador.agregarPedido(new Pedido(1, true));

        procesador.procesarPedidos();
        procesador.cerrarProcesador();

        // Verificar que el procesador se haya cerrado correctamente
        assertTrue(procesador.getProcesador().isShutdown(), "El procesador debe estar cerrado.");
        assertTrue(procesador.getProcesador().isTerminated(), "No debe haber tareas pendientes después del cierre.");
    }

    @Test
    public void testFlujoCompleto() {
        ProcesadorPedidos procesador = new ProcesadorPedidos(7);
        for (int i = 0; i < 10; i++) {
            procesador.agregarPedido(new Pedido(i, i % 2 == 0));
        }

        procesador.procesarPedidos();
        procesador.cerrarProcesador();

        // Asegurar que no quedan pedidos sin procesar
        assertTrue(procesador.getColaPedidos().isEmpty(), "Todos los pedidos deben haber sido procesados.");
        assertTrue(procesador.getProcesador().isTerminated(), "El procesador debe estar completamente terminado.");
    }

    @Test
    public void testRendimientoYCondicionesDeCarrera() {
        ProcesadorPedidos procesador = new ProcesadorPedidos(7);
        for (int i = 0; i < 50; i++) {
            procesador.agregarPedido(new Pedido(i, i % 2 == 0));
        }

        long startTime = System.currentTimeMillis();
        procesador.procesarPedidos();
        procesador.cerrarProcesador();
        long endTime = System.currentTimeMillis();

        System.out.println("Tiempo de procesamiento: " + (endTime - startTime) + "ms");
        assertTrue((endTime - startTime) < 30000, "El procesamiento debe ser eficiente y rápido.");
    }

    @Test
    public void testManejoInterrupcion() {
        ProcesadorPedidos procesador = new ProcesadorPedidos(7);
        procesador.agregarPedido(new Pedido(1, true));

        Thread thread = new Thread(() -> {
            procesador.procesarPedidos();
        });
        thread.start();
        thread.interrupt();

        try {
            thread.join();
        } catch (InterruptedException e) {
            fail("El thread fue interrumpido inesperadamente.");
        }

        assertTrue(thread.isInterrupted(), "El thread debe haber manejado la interrupción correctamente.");
        procesador.cerrarProcesador();
    }





}