from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.template import loader
from django.contrib.auth.models import User
from .forms import ImageForm, UserCreationForm
from django.views.generic import CreateView
from .models import Repository


# Create your views here.
def image_upload_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('image_repo:image_list')
    else:
        form = ImageForm()
    return render(request, 'image_upload.html', {'form': form})


def image_list_view(request):
    latest_image_list = Repository.objects.order_by('-upload_date')
    template = loader.get_template('image_list.html')
    context = {
        'latest_image_list': latest_image_list,
    }
    return HttpResponse(template.render(context, request))


class UserCreateView(CreateView):
    template_name = 'user_form.html'
    redirect_field_name = 'registration/login.html'
    form_class = UserCreationForm
    model = User

    def get_success_url(self):
        return reverse('login')


def about_view(request):
    return render(request, 'about.html')
