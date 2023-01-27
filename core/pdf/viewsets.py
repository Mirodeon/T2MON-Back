from core.user.models import PDF
from django.http import HttpResponse
from rest_framework.decorators import api_view


@api_view(['GET'])
def DownloadPDF(self):
    pdfInstance = PDF.objects.get(name='CV - Junior Developer - Mehdi Habaru')
    pdfFile = pdfInstance.pdf
    response = HttpResponse(pdfFile.read())
    response['Content-Disposition'] = 'attachment'
    return response
