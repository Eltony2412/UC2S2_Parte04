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
            
        </ul>
"""

def index (request):
    MENU ="""
          """
    return HttpResponse(menu + MENU)


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
