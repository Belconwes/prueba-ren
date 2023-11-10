from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from Aplications.productos.models import Producto,Categoria
from Aplications.Usuarios.views import home
from .forms import Producto_f

def cart(request,id):
    
    productos = Producto.objects.filter(id=id)
    
    print(productos)
    
    
    return render(request,'productos/detail_p.html',{'productos':productos})


def carga_p(request):
    try:
        if request.method == 'GET':
            prod = Producto_f()
            return render(request,'productos/carga_p.html',{'form':prod})
        else:
            prod = Producto_f(data=request.POST,files=request.FILES)
            if prod.is_valid():
                print('pasa')
                prod.save()
                return redirect(to='padre')
                
            else:
               print('No funciona')
               return render(request,'productos/carga_p.html',{'form':prod})
                 
    except ValueError as i:
        print(i)



def modify_p(request,id):
    products = get_object_or_404(Producto,id=id)
    try:
        if request.method == 'GET':
            data ={
                'form': Producto_f(instance=products) 
            }
            return render (request,'productos/modificar.html',data)
        else:
            products = get_object_or_404(Producto,id=id)
            formulario = Producto_f(data=request.POST,instance=products,files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                print('valid')
                return redirect(to='padre')
    except ValueError as e:
        print(e)
            
            
            
def search(request):
    texto_busqueda = request.GET['texto']
    productosPornombre = Producto.objects.filter(nombre__icontains = texto_busqueda).all()
    productosPorDescripcion = Producto.objects.filter(descripcion__icontains = texto_busqueda).all()
    productos = productosPornombre | productosPorDescripcion
    
    return render(request, 'productos/search.html',
    {
        'categorias' : Categoria.objects.all(),
        'productos' : productos,
        'texto_buscado' : texto_busqueda,
        'titulo_seccion' : 'Productos que contienen',
        'sin_productos' : 'No hay producto de la categoria ' + texto_busqueda
    })
        
def search_c(request,categoria_id):
    categoria = get_object_or_404(Categoria, id = categoria_id)
    CategoriaP = Producto.objects.filter(nombre__icontains = Categoria).all()
    productos = categoria.productos.all()
    return render(request, 'productos/search.html',
    {
        'categorias' : Categoria.objects.all(),
        'productos' : productos,
        'categoria' : categoria.nombre,
        'titulo_seccion' : 'Productos de la categoria',
        'sin_productos' : 'No hay producto de la categoria '
    })

# Create your views here.
def producto_delete(request, id):
    producto = get_object_or_404(Producto,id=id)
    producto.delete()
    return redirect(to='padre')


def practica(request):
    prod = get_object_or_404(Producto,id=10)
    pre = prod.precio * 10 / (100)
    print(pre)
    result = prod.precio - pre
    return HttpResponse(f'El resultado es: {result} ')
    
def practica2(request):
    pro = Producto.objects.all()
    if pro.is_sale == True:
         pre = pro.precio * 10 / (100)
         print(pre)
         result = pro.precio - pre
         return render (request,'pruebas/pro.html',{'prod':pro})      
    else:
        return render(request,'prueba/pro.html',{'prod':pro})
          