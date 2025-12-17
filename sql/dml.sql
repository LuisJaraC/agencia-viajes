USE agencia_viajes;

-- 1. Roles (3 opciones obligatorias)
INSERT INTO rol (nombre) VALUES 
('CLIENTE'), 
('ADMIN'), 
('AGENCIA');

-- 2. Destinos (2 registros)
INSERT INTO destino (nombre, descripcion, precio_base, is_active) VALUES 
('Torres del Paine', 'Parque nacional en la Patagonia chilena', 50000, TRUE),
('San Pedro de Atacama', 'Desierto, salares y geiseres en el norte', 40000, TRUE);

-- 3. Paquetes Turísticos (2 registros)
-- Nota: Las fechas están en formato YYYY-MM-DD
INSERT INTO paquete_turistico (nombre_paq, precio, cupos, stock, fecha_ini, fecha_fin, is_active) VALUES 
('Aventura Austral', 150000, 10, TRUE, '2025-01-15', '2025-01-20', TRUE),
('Mistica Nortina', 120000, 5, TRUE, '2025-02-10', '2025-02-15', TRUE);

-- 4. Usuarios (2 registros: 1 Admin y 1 Cliente para pruebas)
-- IMPORTANTE: 'passwd' aquí es texto plano para prueba DB. 
-- En la app real, el Python debe hashearlo antes de comparar.
INSERT INTO `usuario` (`id_user`, `nombre`, `apellido`, `email`, `passwd`, `fecha_reg`, `id_rol`, `is_active`) VALUES
(1, 'Juan', 'Perez', 'juan@admin.cl', '$2b$12$vgRT57WdXZEYYMcla2aof.qCl0b0FCcMYlcI6rGqcrTmSu9R8NFo.', '2025-12-17 03:04:49', 2, 1), -- Rol 2 = ADMIN
(2, 'Luis', 'Jara', 'luis@agencia.cl', '$2b$12$aI7Y.iG1OTKrkXT1SbOBi.PKoGahW9VfMR75zRbDQ7mqtzVeKpQ7e', '2025-12-17 03:11:54', 3, 1), -- Rol 3 = AGENCIA
(3, 'marco', 'villa', 'marco@mail.com', '$2b$12$TJusHg0rCPtTkvaux8s4Z.tI1yoxN5P8me1xEZFaNFEmCEVyscX4m', '2025-12-16 20:36:05', 1, 1); -- Rol 1 = CLIENTE

-- 5. Tabla Intermedia Destino-Paquete (2 registros)
-- Vinculamos el Destino 1 con Paquete 1, y Destino 2 con Paquete 2
INSERT INTO destino_paquete (id_destino, id_paquete) VALUES 
(1, 1), -- Torres del Paine -> Aventura Austral
(2, 2); -- San Pedro -> Mistica Nortina

-- 6. Reservas (2 registros)
-- Maria (id_user=2) compra ambos paquetes
INSERT INTO reserva (ctd_personas, precio_pactado, id_user, id_paquete) VALUES 
(2, 300000, 2, 1), -- 2 personas * 150.000 (Precio snapshot del paquete 1)
(1, 120000, 2, 2); -- 1 persona * 120.000 (Precio snapshot del paquete 2)