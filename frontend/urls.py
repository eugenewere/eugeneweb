from django.shortcuts import render
from django.test import override_settings, SimpleTestCase
from django.urls import path
from . import views
from django.conf.urls import handler404, handler500

def error_404(request, exception):
    return render(request,'error-404.html', status=404)

def error_500(request):
    return render(request,'error-500.html', status=500)

handler500 = error_500
handler404 = error_404
app_name = 'frontend'

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('addmessage/', views.addmessage, name='addmessage'),
    path('addsubscribers/', views.addsubscribers, name='addsubscribers'),
    path('view_cv/', views.view_cv, name='view_cv'),

]
@override_settings(ROOT_URLCONF=__name__)
class CustomErrorHandlerTests(SimpleTestCase):

    def test_handler_renders_template_response(self):
        response = self.client.get('/404/')
        # Make assertions on the response here. For example:
        self.assertContains(response, 'error-404.html', status_code=404)

    def test_handler_renders_template_response2(self):
        response = self.client.get('/500/')
        # Make assertions on the response here. For example:
        self.assertContains(response, 'error-500.html', status_code=500)