from django.shortcuts import render
from django.core.mail import send_mail

def main(request):
	# import pdb; pdb.set_trace()
	send_mail('Subject here', 'Here is the message.', 'from@example.com',
    	['lykhenko.olexandr@gmail.com'], fail_silently=False)
	return render(request, "index.html")
# Create your views here.
