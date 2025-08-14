from django.shortcuts import render, redirect, get_object_or_404
from urllib.parse import unquote
from django.shortcuts import get_object_or_404, render, redirect
from .forms import PromptForm
from .models import Demon

# Home page view
def main(request):
    demons = Demon.objects.all()  
    return render(request, 'website/main.html', {'demons': demons})

def create(request):
    form_submitted = False  

    if request.method == 'POST':
        form = PromptForm(request.POST)
        form_submitted = True  
        if form.is_valid():
            form.save()
            return redirect('main')  
        else:
            print(form.errors)  

    if request.method == 'GET':
        form = PromptForm()

    return render(request, 'website/create.html', {'form': form, 'form_submitted': form_submitted})

def update(request, promptID):
    prompt_instance = get_object_or_404(Demon, promptID=promptID)
    form_submitted = False  
    
    if request.method == 'POST':
        form = PromptForm(request.POST, instance=prompt_instance)
        form_submitted = True  
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = PromptForm(instance=prompt_instance)
    
    return render(request, 'website/update.html', {'form': form, 'prompt': prompt_instance, 'form_submitted': form_submitted})


def delete(request, promptID):
    prompt_instance = get_object_or_404(Demon, promptID = promptID)
    if request.method == 'POST':
        prompt_instance.delete()
        return redirect('db_home')
    return render(request, 'website/delete.html', {'prompt': prompt_instance})