from django.shortcuts import render
# Create your views here.
from basic_portfolio.forms import NewContact

# def index(request):
#     return render(request, 'basic_portfolio/index.html')

def uniprojects(request):
    return render(request, 'basic_portfolio/university_projects.html')

# def contactform(request):
#     form = NewContact
#
#     if request.method == 'POST':
#         form = NewContact(request.POST)
#
#         if form.is_valid():
#             form.save(commit=True)
#             return index(request)
#         else:
#             print('ERROR')
#
#     return render(request, 'basic_portfolio/contact.html', {'form':form})
