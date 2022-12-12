from ipware import get_client_ip
from django.http import HttpResponse
from proyecto.models import IpUsuario

BLACK_LIST = [
]

def ip_is_valid(get_response):

    def middleware(request):

        ip, is_routable = get_client_ip(request)
        ipguardada = IpUsuario.objects.filter(ip = ip).first()
        if ipguardada is None:
            ipguardada = IpUsuario(ip = ip)
            ipguardada.save()
        response = get_response(request)
        return response
    return middleware