from django.shortcuts import render, HttpResponse
 
menu = """
    <h1>MENU</h1>
        <br>
        <ul>
            <li>
                <a href = "/inicio">INICIO</a>
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
