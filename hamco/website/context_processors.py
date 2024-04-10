# context_processors.py
# This file will contain common context that I want to apply throughout the app.  
# I have to make a chance to settings to include this file in the TEMPLATES setting.
def common_context(request):
    return {
        'title': 'Hamco Internet Solutions',
        'company': 'Hamco Internet Solutions',
    }