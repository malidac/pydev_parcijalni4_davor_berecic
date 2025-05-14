from django.views.generic.base import TemplateView

# Create your views here.
class DashboardPage(TemplateView):
    template_name = 'dashboards/dashboard_page.html'
