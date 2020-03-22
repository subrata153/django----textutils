#this file is manually created
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return render(request, 'index.html')

def  analyze(request):
	djtext = request.POST.get('text', 'default')
	punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
	removepunc = request.POST.get('removepunc', 'off')
	uppercase = request.POST.get('uppercase', 'off')
	newlineremover = request.POST.get('newlineremover', 'off')
	charcount = request.POST.get('charcount', 'off')
	analyzed = ''
	if removepunc == 'on' :
		for char in djtext:
			if char not in punctuations:
				analyzed = analyzed + char
				
		params = {'purpose':'Remove puncuations', 'analyze_text':analyzed}
		djtext = analyzed
		# return render(request, 'analyze.html', params)

	if uppercase == 'on':
		analyzed = ""
		for char in djtext:
			analyzed = analyzed + char.upper()
			
		params = {'purpose':'All uppercase', 'analyze_text':analyzed}	
		djtext = analyzed
		# return render(request, 'analyze.html', params)	
	if newlineremover == 'on':
		analyzed = ""
		for char in djtext:
			if char != "\n" and char != '\r':
				analyzed = analyzed + char
				
		params = {'purpose':'New line removed', 'analyze_text':analyzed}	
		djtext = analyzed
		# return render(request, 'analyze.html', params)
	if charcount == 'on':
		analyzed = 'total character is:'
		analyzed = analyzed + str(len(djtext))	
			
		params = {'purpose':'Count char', 'analyze_text':analyzed}	
		djtext = analyzed

	if removepunc != 'on' and uppercase != 'on' and newlineremover != 'on':
		return HttpResponse('error')
		# return render(request, 'analyze.html', params)			
	# else :
	# 	analyzed = djtext
	# 	params = {'purpose':'Default text', 'analyze_text':analyzed}
	# 	return render(request, 'analyze.html', params)
	return render(request, 'analyze.html', params)

def about(request):
	return HttpResponse('this is about page')
def contact_us(request):
	return HttpResponse('this is contact page')	

