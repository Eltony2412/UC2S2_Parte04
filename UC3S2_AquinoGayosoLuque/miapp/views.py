from django.shortcuts import render, HttpResponse
 
menu = """
    <h1>MENU</h1>
        <br>
        <ul>
            <li>
                <a href = "/inicio">INICIO</a>
            </li>
            <li>
                <a href = "/Primos/15/40">Primos</a>
            </li>
            <li>
                <a href = "/examen">Examen</a>
            </li>
            
        </ul>
"""

def index (request):
    MENU ="""
          """
    return HttpResponse(menu + MENU)

def examen (request):
    datos = """
            <h3>GIT HUB DEL PROYECTO:</h3>
                    <ul>
                        <li>
                            <h4>Nombre del estudiante 01: Luque</h4>
                            <h4>GIT HUB: <a href = "https://github.com/Eltony2412/UC3S2_Parte01.git">LUQUE</a></h4>
                        </li>
                        
                        <li>
                            <h4>Nombre del estudiante 02: Gayoso</h4>
                            <h4>GIT HUB: <a href = "https://github.com/LuisGF16/UC2S2-Parte02.git">GAYOSO</a> </h4>
                        </li>
                        <li>
                            <h4>Nombre del estudiante 03: Aquino</h4>
                            <h4>GIT HUB: <a href = "https://github.com/LuisGF16/UC2S2-Parte02.git">AQUINO</a></h4>
                        </li>
                        
                        <li>
                            <h4>Nombre del estudiante 04: Luque</h4>
                            <h4>GIT HUB: </h4>
                        </li>
                        
                    </ul>
    """
    return HttpResponse(menu + datos)

def inicio(request):
    mensaje="""
                <H1>LP3</H1>
                <br>
                <H2>Integrantes:</H2>
                <ul>
                    <li> Carlos</li>
                    <li> Elberth</li>
                    <li> Luis</li>
                </ul>
            """
    return HttpResponse(menu + mensaje)

def Primos(request,a,b):
    mensaje = f"""
        <h2>Numeros Primos entre {a} y {b}</h2>
        Resultado :<br> 
        <ul>    
    """
    if a>b:
        for i in range(b,a+1):
            valor= range(2,i)
            contador = 0
            for n in valor:
                if i % n == 0:
                    contador +=1
            if contador <= 0 :
                mensaje += f" <li>{i}</li>"
    else:
        for i in range(a,b+1):
            valor= range(2,i)
            contador = 0
            for n in valor:
                if i % n == 0:
                    contador +=1
            if contador <= 0 :
                mensaje += f" <li>{i}</li>"
    mensaje +="</ul>"
    return HttpResponse(menu + mensaje)
