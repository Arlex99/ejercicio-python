productos_lista = [
    {'id': 1, 'nombre': 'televisor', 'precio': 800, 'id_categoria': 1},
    {'id': 2, 'nombre': 'escritorio en L 62cm', 'precio': 100, 'id_categoria': 2},
    # Agrega más productos aquí si es necesario
]

categorias_diccionario = {
    1: 'tecnologia',
    2: 'decoracion',
    # Agrega más categorías aquí si es necesario
}

articulos_con_tipos = {producto['nombre']: categorias_diccionario.get(producto['id_categoria'], 'Tipo desconocido') for producto in productos_lista}

for articulo, tipo in articulos_con_tipos.items():
    print(f"Artículo: {articulo} - Tipo: {tipo}")


