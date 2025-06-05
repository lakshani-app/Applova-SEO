from django.shortcuts import render

# Create your views here.

def dashboard_view(request):
    """Placeholder view for the dashboard."""
    return render(request, 'dashboard/dashboard.html')
