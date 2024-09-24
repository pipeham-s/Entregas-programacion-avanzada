package Entregable_2;

public class Main {
    public static void main(String[] args) {
        // Crear el procesador de pedidos con 10 hilos
        ProcesadorPedidos procesador = new ProcesadorPedidos(6);

        // Crear y agregar pedidos (algunos urgentes)
        procesador.agregarPedido(new Pedido(1, false));
        procesador.agregarPedido(new Pedido(2, true));  // Pedido urgente
        procesador.agregarPedido(new Pedido(3, false));
        procesador.agregarPedido(new Pedido(4, true));  // Pedido urgente
        procesador.agregarPedido(new Pedido(5, false));
        procesador.agregarPedido(new Pedido(6, false));
        procesador.agregarPedido(new Pedido(7, true));  // Pedido urgente
        procesador.agregarPedido(new Pedido(8, false));
        procesador.agregarPedido(new Pedido(9, false));
        procesador.agregarPedido(new Pedido(10, false));
        procesador.agregarPedido(new Pedido(11, true));  // Pedido urgente
        procesador.agregarPedido(new Pedido(12, false));
        procesador.agregarPedido(new Pedido(13, false));
        procesador.agregarPedido(new Pedido(14, false));
        procesador.agregarPedido(new Pedido(15, true));  // Pedido urgente
        procesador.agregarPedido(new Pedido(16, false));
        procesador.agregarPedido(new Pedido(17, false));
        procesador.agregarPedido(new Pedido(18, false));
        procesador.agregarPedido(new Pedido(19, false));
        procesador.agregarPedido(new Pedido(20, false));
        procesador.agregarPedido(new Pedido(21, false));
        procesador.agregarPedido(new Pedido(22, true));  // Pedido urgente
        procesador.agregarPedido(new Pedido(23, false));
        procesador.agregarPedido(new Pedido(24, true));  // Pedido urgente
        procesador.agregarPedido(new Pedido(25, false));
        procesador.agregarPedido(new Pedido(26, false));
        procesador.agregarPedido(new Pedido(27, true));  // Pedido urgente
        procesador.agregarPedido(new Pedido(28, false));
        procesador.agregarPedido(new Pedido(29, false));
        procesador.agregarPedido(new Pedido(30, false));
        procesador.agregarPedido(new Pedido(31, true));  // Pedido urgente
        procesador.agregarPedido(new Pedido(32, false));
        procesador.agregarPedido(new Pedido(33, false));
        procesador.agregarPedido(new Pedido(34, false));
        procesador.agregarPedido(new Pedido(35, true));  // Pedido urgente
        procesador.agregarPedido(new Pedido(36, false));
        procesador.agregarPedido(new Pedido(37, false));
        procesador.agregarPedido(new Pedido(38, false));
        procesador.agregarPedido(new Pedido(39, false));
        procesador.agregarPedido(new Pedido(40, false));
        procesador.agregarPedido(new Pedido(41, false));
        procesador.agregarPedido(new Pedido(42, true));  // Pedido urgente
        procesador.agregarPedido(new Pedido(43, false));
        procesador.agregarPedido(new Pedido(44, true));  // Pedido urgente
        procesador.agregarPedido(new Pedido(45, false));
        procesador.agregarPedido(new Pedido(46, false));
        procesador.agregarPedido(new Pedido(47, true));  // Pedido urgente
        procesador.agregarPedido(new Pedido(48, false));
        procesador.agregarPedido(new Pedido(49, false));
        procesador.agregarPedido(new Pedido(50, false));
        procesador.agregarPedido(new Pedido(51, true));  // Pedido urgente
        procesador.agregarPedido(new Pedido(52, false));
        procesador.agregarPedido(new Pedido(53, false));
        procesador.agregarPedido(new Pedido(54, false));
        procesador.agregarPedido(new Pedido(55, true));  // Pedido urgente
        procesador.agregarPedido(new Pedido(56, false));
        procesador.agregarPedido(new Pedido(57, false));
        procesador.agregarPedido(new Pedido(58, false));
        procesador.agregarPedido(new Pedido(59, false));
        procesador.agregarPedido(new Pedido(60, false));
        procesador.agregarPedido(new Pedido(61, false));
        procesador.agregarPedido(new Pedido(62, true));  // Pedido urgente
        procesador.agregarPedido(new Pedido(63, false));
        procesador.agregarPedido(new Pedido(64, true));  // Pedido urgente
        procesador.agregarPedido(new Pedido(65, false));
        procesador.agregarPedido(new Pedido(66, false));
        procesador.agregarPedido(new Pedido(67, true));  // Pedido urgente
        procesador.agregarPedido(new Pedido(68, false));
        procesador.agregarPedido(new Pedido(69, false));
        procesador.agregarPedido(new Pedido(70, false));
        procesador.agregarPedido(new Pedido(71, true));  // Pedido urgente
        procesador.agregarPedido(new Pedido(72, false));
        procesador.agregarPedido(new Pedido(73, false));
        procesador.agregarPedido(new Pedido(74, false));
        procesador.agregarPedido(new Pedido(75, true));  // Pedido urgente
        procesador.agregarPedido(new Pedido(76, false));
        procesador.agregarPedido(new Pedido(77, false));
        procesador.agregarPedido(new Pedido(78, false));
        procesador.agregarPedido(new Pedido(79, false));
        procesador.agregarPedido(new Pedido(80, false));
        procesador.agregarPedido(new Pedido(81, false));
        procesador.agregarPedido(new Pedido(82, true));  // Pedido urgente
        procesador.agregarPedido(new Pedido(83, false));
        procesador.agregarPedido(new Pedido(84, true));  // Pedido urgente
        procesador.agregarPedido(new Pedido(85, false));
        procesador.agregarPedido(new Pedido(86, false));
        procesador.agregarPedido(new Pedido(87, true));  // Pedido urgente
        procesador.agregarPedido(new Pedido(88, false));
        procesador.agregarPedido(new Pedido(89, false));
        procesador.agregarPedido(new Pedido(90, false));
        procesador.agregarPedido(new Pedido(91, true));  // Pedido urgente
        procesador.agregarPedido(new Pedido(92, false));
        procesador.agregarPedido(new Pedido(93, false));
        procesador.agregarPedido(new Pedido(94, false));
        procesador.agregarPedido(new Pedido(95, true));  // Pedido urgente
        procesador.agregarPedido(new Pedido(96, false));
        procesador.agregarPedido(new Pedido(97, false));
        procesador.agregarPedido(new Pedido(98, false));
        procesador.agregarPedido(new Pedido(99, false));
        procesador.agregarPedido(new Pedido(100, false));

        // Procesar todos los pedidos y medir el tiempo
        long startTime = System.currentTimeMillis();
        procesador.procesarPedidos();

        // Cerrar el procesador de manera ordenada
        procesador.cerrarProcesador();

        long endTime = System.currentTimeMillis();
        System.out.println("\nTiempo total de procesamiento: " + (endTime - startTime) + " ms");
    }
}
