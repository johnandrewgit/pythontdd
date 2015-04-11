from django.shortcuts import redirect, render
from lists.models import Item, List

# Create your views here.
# def home_page(request):
#     if request.method == 'POST':
#         return HttpResponse(request.POST['item_text'])
#     return render(request, 'home.html')

def home_page(request):
    ## deprecated because the new_list view handles submission data
    # if request.method == 'POST':
    #     Item.objects.create(text=request.POST['item_text'])
    #     return redirect('/lists/the-only-list-in-the-world/')

    return render(request, 'home.html')

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/the-only-list-in-the-world/')