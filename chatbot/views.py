from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import google.generativeai as ga
from concurrent.futures import ThreadPoolExecutor


api_key = "AIzaSyDpB47-XDN0P794DHOh2Y6c6d2RkG53-rU"
ga.configure(api_key=api_key)
model = ga.GenerativeModel('gemini-1.5-flash')


executor = ThreadPoolExecutor(max_workers=3)

def chat_home(request):
    return render(request, 'chat/chat.html')

def generar_respuesta(mensaje):
    respuesta = model.generate_content(mensaje) 
    return respuesta.texto

@csrf_exempt
def mensaje_chat(request):
    if request.method == 'POST':
        try:
            datos = json.loads(request.body)
            mensaje_usuario = datos.get('mensaje', '')
            
            respuesta_bot = executor.submit(generar_respuesta, mensaje_usuario).result()
            
            return JsonResponse({
                'respuesta': respuesta_bot
            })
        except Exception as e:
            print(f"Error: {str(e)}")
            return JsonResponse({
                'error': 'error encontrado intentelo más tarde',
                'detalles': str(e)
            }, status=500)
    
    return JsonResponse({'error': 'Método de solicitud inválido'}, status=400)