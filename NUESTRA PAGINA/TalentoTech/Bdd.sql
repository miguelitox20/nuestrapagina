USE CAPESA;

INSERT INTO categorias (nombre)
VALUES 
    ('Nuevas Colecciones'),
    ('Ediciones Limitadas'),
    ('Ofertas');
    
INSERT INTO productos (nombre, descripcion, precio, imagen_url, categoria_id)
VALUES
    ('FC Barcelona - 2024', 'Camiseta oficial del FC Barcelona para la temporada 2024', 120.00, 'https://static.nike.com/a/images/t_default/29651b91-8c59-489d-8049-4ac91c477065/fc-barcelona-2023-24-match-home-dri-fit-adv-football-shirt-5nPN9V.png', 1),
    ('Real Madrid - 2024', 'Camiseta oficial del Real Madrid para la temporada 2024', 110.00, 'https://football-shop.ru/wp-content/uploads/2023/06/real-madrid-1-2.jpg', 1),
    ('Liverpool - Edición Limitada', 'Camiseta edición limitada del Liverpool', 140.00, 'https://th.bing.com/th/id/OIP.odxvmcqI2wgA2q3_jAWrYQHaHa?rs=1&pid=ImgDetMain', 2),
    ('Manchester United', 'Camiseta del Manchester United en oferta', 90.00, 'https://images.prodirectsport.com/ProductImages/Main/248804_Main_Thumb_1005655.jpg', 3);

INSERT INTO carrito (producto_id, cantidad)
VALUES (1, 2); -- Ejemplo: 2 unidades del producto con id=1

SELECT c.id, p.nombre, c.cantidad, p.precio, (c.cantidad * p.precio) AS total
FROM carrito c
JOIN productos p ON c.producto_id = p.id;

DELETE FROM carrito;
