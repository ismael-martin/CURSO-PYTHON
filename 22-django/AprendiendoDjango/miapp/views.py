from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
# MVC vs MVT
#MVC = Modelo Vista Controlador -> dentro del controlador hay metodos
#MVT = Modelo Vista Template

layout = """
<h1>Sitio web con Django | Ismael Martín</h1>
<hr>
<ul>
    <li><a href="/inicio">Inicio</a></li>
    <li><a href="/hola-mundo">Hola mundo</a></li>
    <li><a href="/pagina">Pagina de prueba</a></li>
    <li><a href="/contacto">Contacto</a></li>
</ul>
<hr>

"""

def index(request):
    year = 2021
    html = """
    
    <ul>
    """
    while year <= 2050:
        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"
        year+=1

    html += "</ul>"
    return render(request, "index.html")

def hola_mundo(request):
    return render(request, "hola_mundo.html")

def pagina(request, redir=0):

    if redir == 1:
        return redirect('contacto', nombre="Ismael Martín")
    else:
        return render(request, "pagina.html")

def contacto(request, nombre="wey"):
    return HttpResponse(layout+f"""
    <h1>Página de contacto</h1>
    <p>Que pasó {nombre}?</p>
    """)

