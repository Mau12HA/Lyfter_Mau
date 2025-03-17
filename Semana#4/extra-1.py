"""
1. Cree un pseudocódigo que le pida un `precio de producto` al usuario, calcule su descuento y muestre el precio final tomando en cuenta que:
    1. Si el precio es menor a 100, el descuento es del 2%.
    2. Si el precio es mayor o igual a 100, el descuento es del 10%.

"""

precio = int(input("Ingrese el Precio : "))
descuento = float()
precio_final = float()

if (precio < 100):
    descuento = (precio * 0.02)

elif (precio >= 100):
    descuento = (precio * 0.1)

precio_final = precio - descuento

print(f'El precio con Descuento es : {precio_final}')
