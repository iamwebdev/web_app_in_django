from django.views import generic
from .models import Album
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.core.urlresolvers import reverse_lazy

class IndexView(generic.ListView):
    context_object_name = 'all_albums'
    template_name = 'music/index.html'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/details.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')