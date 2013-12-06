from django.shortcuts import render
from django.http import HttpResponse
import urllib

def index(request):
  return render(request, 'is_up_me/index.html', )
  
def consultar(request, url_solicitada):
  url_solicitada = request.POST['url_text']
  resultado = ""
  
  if ( not ('http://' in url_solicitada ) ):
    url_solicitada = 'http://' + url_solicitada 
    
  try:
    urllib.urlopen(url_solicitada).getcode()
  except IOError:
    resultado = "no"
    #return HttpResponse("%s no esta disponible" % url_solicitada)
	
  #return HttpResponse("%s esta disponible" % url_solicitada)
  return render(request, 'is_up_me/resultado.html', {'url_solicitada': url_solicitada ,'resultado': resultado})