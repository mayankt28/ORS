from django.shortcuts import render,get_object_or_404,redirect
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from mgmt_sys.views import save_data

# Create your views here.
@csrf_exempt
def payment_done(request):
    return redirect(save_data)

@csrf_exempt
def payment_canceled(request):
    return render(request,'payment/canceled.html')

def payments_process(request):
    order_id = request.session['id'][0]
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount':'50',
        'item_name':'Appointment for hospital',
        'invoice': str(order_id),
        'currency_code': 'INR',
        'notify_url':'http://{}{}'.format(host,reverse('paypal-ipn')),
        'return_url':'http://{}{}'.format(host,reverse('payment:done')),
        'cancel_return':'http://{}{}'.format(host,reverse('payment:canceled')),
    }
    form =PayPalPaymentsForm(initial=paypal_dict)
    return render(request,'payment/process.html',{'form':form})


