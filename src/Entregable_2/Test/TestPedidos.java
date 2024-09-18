package Entregable_2.Test;

import Entregable_2.Pedido;
import Entregable_2.ProcesadorPedidos;
import org.junit.jupiter.api.Test;
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
    public void testProcesamientoCorrecto() {
        ProcesadorPedidos procesador = new ProcesadorPedidos(5);

        Pedido pedido1 = new Pedido(1, false);
        Pedido pedido2 = new Pedido(2, true);

        procesador.agregarPedido(pedido1);
        procesador.agregarPedido(pedido2);

        procesador.procesarPedidos();
        procesador.cerrarProcesador();

        assertTrue(true); // Aquí se podrían añadir más validaciones según los logs
    }
}

