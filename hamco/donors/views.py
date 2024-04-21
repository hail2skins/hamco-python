from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Sum, Q, Count
import csv
from django.http import HttpResponse

# import the login_required decorator
from django.contrib.auth.decorators import login_required

# Import your models
from .models import Donor

# Create your views here.

# Donor List View
@login_required(login_url='login')
def donor_list(request):
    """
    Donor List View

    This view will display a list of all donors in the database.
    @login_required` is a decorator that will redirect the user to the login page if they are not authenticated.
    We also need to implement pagination to display the donors in pages.

    The Donor model has a relationship with the Contribution model, so we need to import both models.
    We need this list to display the donor's total contributions, so we need to fetch the contributions
    from the DB, and total them and then add to our template context.
    """

    search_query = request.GET.get('search', '')
    if search_query:
        # Allow zip codes to be entered as a comma-separated list
        zip_codes = search_query.replace(' ', '').split(',')
        donor_list = Donor.objects.annotate(
            total_contributions=Sum('contribution__amount')
        ).filter(
            Q(first_name__icontains=search_query) | 
            Q(last_name__icontains=search_query) | 
            Q(zip_code__in=zip_codes)
        ).distinct()
    else:
        donor_list = Donor.objects.annotate(
            total_contributions=Sum('contribution__amount')
        )
        
    # Check if the user wants to download the list as a CSV file
    if 'download' in request.GET:
        response = HttpResponse(
            content_type='text/csv',
            headers={'Content-Disposition': 'attachment; filename="donors.csv"'},
        )
        writer = csv.writer(response)
        writer.writerow(['First Name', 'Last Name', 'Street Number', 'Street Name', 'City', 'State', 'Zip Code', 'Total Contributions'])
        for donor in donor_list:
            writer.writerow([donor.first_name, donor.last_name, donor.street_number, donor.street_name, donor.city, donor.state, donor.zip_code, donor.total_contributions or 0.00])
        return response

    # Calculate total donors and total contributed from the filtered queryset
    total_donors = donor_list.count()
    total_contributed = donor_list.aggregate(total=Sum('total_contributions'))['total'] or 0

    paginator = Paginator(donor_list, 100)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # add context dictionary to pass to the template
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'total_donors': total_donors,
        'total_contributed': total_contributed,        
    }
    
    return render(request, 'donors/donor_list.html', context)