# import africastalking
import africastalking
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from backend.models import *
from backend.forms import *
from mysite import templateo


def home(request):

    context={
        'announces': AnnouncementBar.objects.filter(status='SHOW'),
        'carousels': Carousel.objects.all(),
        'about': About.objects.first(),
        'categories': Category.objects.all(),
        'hobbies': Hobbies.objects.all(),
        'services': Speciality.objects.all(),
        "pcs": Progresscounter.objects.first(),
        "pro_done": Portfolio.objects.filter(category__name__contains="Web").count(),
        # "pro_done": Portfolio.objects.filter(category__).count(),
        "logo_done": Portfolio.objects.filter(category__name__contains="Logo Design").count(),
        "participations":WorkParticipation.objects.order_by("-created_at"),
        "expertise": Expertise.objects.all(),
        "projects": Portfolio.objects.order_by("?")[:12],
        "counter_image": CounterImages.objects.filter(status="ACTIVE").first(),
        "expertise_image": WorkExpertise.objects.filter(status="ACTIVE").first(),
        "available_image": AvailableForTheProject.objects.filter(status="ACTIVE").first(),
        "contuctus_image": ContactMeImage.objects.filter(status="ACTIVE").first(),
        "sendmsgs_image": SendMessageImage.objects.filter(status="ACTIVE").first(),

    }
    return render(request, 'home/index.html', context)


def portfolio(request):
    context = {
        'announces': AnnouncementBar.objects.filter(status='SHOW'),
        "projects": Portfolio.objects.order_by("?"),
        'categories': Category.objects.all(),
    }
    return render(request, 'portfolios/portfolio.html', context)

@csrf_exempt
def addmessage(request):
    if request.method == "POST":
        # print(request.POST)
        form = MessageForm(request.POST)
        message = request.POST.get('message')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        subject = request.POST.get('subject')

        print(message, first_name, last_name, subject)
        print(form)

        if form.is_valid():
            try:
                username = templateo.AFRICAS_TALKING_USERNAME
                # use 'sandbox' for development in the test environment
                api_key = templateo.AFRICAS_TALKING_KEY
                # print(username, api_key)
                africastalking.initialize(username, api_key)
                # phonenumberr = 706833784
                # new_phone_number = f"{254}{phonenumberr[-9:]}"
                # print(new_phone_number)

                sender = first_name+" "+last_name
                messagee = "Subject: "+subject + "\n From: "+sender+"\n Message: " + message
                # print(messagee)
                sms = africastalking.SMS
                # print(sms)
                response = sms.send(messagee, ["+254706833784"])
                # print('success', response)
            except:
                print('NO INTERNET')
                context = {
                    'results': 'error',
                    'response': "No Internet"
                }
            form.save()

            return JsonResponse(
                {
                    'results': 'success',
                    'form_success': "Successfuly Sent The Message",
                },
                safe=False)
        else:
            return JsonResponse(
                {'results': 'error',
                 'form_error': "Message not sent please"},
                safe=False)
    return redirect('frontend:home')


def addsubscribers(request):
    if request.method == "POST":
        print(request.POST)
        form = NewsLetterForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return JsonResponse(
                {
                    'results': 'success',
                    'form_success': "Successfuly Subscribed",
                },
                safe=False)
        else:
            return JsonResponse(
                {'results': 'error',
                 'form_error': "Unable to Subscribe"},
                safe=False)
    return redirect('frontend:home')


def view_cv(request):
    context={
        'admin': Admin.objects.all().first(),
        'expes': Experience.objects.all().order_by('-start_d'),
        'educations':Education.objects.all().order_by('-start_d'),
        'categories': Category.objects.all(),
        'about':About.objects.all().first(),
        'social': SocialMedia.objects.all(),
        'software':Software.objects.all(),
        'languages':Language.objects.all()
    }
    return render(request, 'cv/cv.html', context)

def error_404(request, exception):
    context = {}
    response = render(request, "error-404.html", context=context)
    response.status_code = 404
    return response

def error_500(request):
    context = {}
    response = render(request, "error-500.html", context=context)
    response.status_code = 500
    return response
