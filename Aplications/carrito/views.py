from django.shortcuts import render,redirect
from django.http import JsonResponse
import json
from Aplications.Usuarios.models import User
from Aplications.pedido.models import Pedido
from Aplications.productos.models import Producto,Categoria
from .models import CarritoProducto,Carrito



def int(request):
    return render(request,'Carrito/carrito.html')
# Create your views here.



def carrito(request):
    if request.user.is_authenticated:
        customer = request.user
        pedido, created = Pedido.objects.get_or_create(Usuario_p=customer)
        items = pedido.carritoproducto_set.all()
    else:
        items = []
        pedido = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items, 'pedido': pedido}
    return render(request, 'Carrito/carrito.html', context)
    """categorias = Categoria.objects.all()
    usuario_logeado = User.objects.get(id=request.user)
    productos = Carrito.objects.get(id=usuario_logeado.id).items.all()

    carrito = Carrito.objects.get(User_id=usuario_logeado.id)
    nuevo_precio_Carrito = 0
    for item in carrito.items.all():
        nuevo_precio_Carrito += item.producto.precio
    carrito.total = nuevo_precio_Carrito
    carrito.save()

    return render(request, 'Carrito/Carrito.html', {
        'categorias' : categorias,
        'usuario' : usuario_logeado,
        'items_carrito' : productos
    })"""


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    
    print('Action:', action)
    print('Producto ID:', productId)
    
    customer = request.user
    carrito = Carrito.objects.get_or_create(customer=customer)
    carrito = Carrito.objects.get(customer=customer)
    producto = Producto.objects.get(id=productId)
    pedido, created = Pedido.objects.get_or_create(Usuario_p=customer)
    print('paso por aca')
    
    carritoProducto, created = CarritoProducto.objects.get_or_create(id_pedido=pedido, id_producto=producto,id_carrito = carrito)

    if action == 'add':
        carritoProducto.cantidad = (carritoProducto.cantidad + 1)
    elif action == 'remove':
        carritoProducto.cantidad = (carritoProducto.cantidad - 1)

    carritoProducto.save()
    
    if carritoProducto.cantidad <= 0:
        carritoProducto.delete()
    
    return JsonResponse('Item was added', safe=False)

def carrito_clean(request):
    usuario_logeado = User.objects.get(email=request.user)
    carrito = Carrito.objects.get(customer=usuario_logeado.id)
    carrito.items.all().delete()
    carrito.total = 0
    carrito.save()
    #return HttpResponse(f'Carrito: id({carrito.id}) ${carrito.total} | Usuario: id({usuario_logeado.id}) {usuario_logeado.username} | items_carrito: {carrito.items.all().count()}')
    return redirect(to='padre')