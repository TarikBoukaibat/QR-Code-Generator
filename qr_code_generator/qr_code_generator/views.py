import qrcode
from django.shortcuts import render
from qrcode import *
data=None
def home(request):
    global data
    if request.method=="POST":
        data=request.POST['data']
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("static/image/QR Code.png")
    else:
        pass
    return render(request,"homepage.html",{'data':data})
