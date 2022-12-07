from django.shortcuts import render

#Request es un diccionario que continuamente se va pasando entre el navegador y el servidor

def Home(request):
	return render(request, 'home.html')

def Nosotros(request):
	return render(request, 'nosotros.html')

def Mision(request):
	return render(request, 'mision.html')

def Galeria(request):
	return render(request, 'galeria.html')

def Esculturas(request):
	return render(request, 'galeriaEsculturas.html')

def Escultores(request):
	return render(request, 'galeriaEscultores.html')