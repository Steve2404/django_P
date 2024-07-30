from django.http import HttpResponse

from listings.models import Band


# Create your views here.
def hello(request):
    band = Band.objects.all()
    return HttpResponse(f"""
    <h1> Hallo Django! </h1>
    <p>Mes groupes preferes sont: </p>
    <ul>
        <li>Band 1: {band[0].name}</li>
        <li>Band 2: {band[1].name}</li>
        <li>Band 3: {band[2].name}</li>
    </ul>
    """)


def about(request):
    return HttpResponse('<h1>About</h1><p>Nous adorons merch</p>')
