from django.shortcuts import render
from spoke.models import Speaker, Speech
from django.views import generic
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    speeches = Speech.objects.all().order_by('-speech_date')
    context = {
        'speeches': speeches,
    }
    return render(request, 'spoke/index.html', context)
    paginate_by = 5

class SpeechListView(generic.ListView):
    model = Speech
    context_object_name = 'speech_list'
    queryset = Speech.objects.all()
    template_name = 'speeches/speech_list.html'

class SpeechDetailView(generic.DetailView):
    model = Speech

    def speech_detail_view(request, primary_key):
        speech = get_object_or_404(Speech, pk=primary_key)
        return render(request, 'spoke/speech_detail.html', context={'speech': speech})

class SpeakerListView(generic.ListView):
    model = Speaker
    context_object_name = 'speaker'
    queryset = Speaker.objects.all()
    template_name = 'speakers/speaker_list.html'

class SpeakerDetailView(generic.DetailView):
    model = Speaker

    def speaker_detail_view(request, primary_key):
        speaker = get_object_or_404(Speaker, pk=primary_key)
        return render(request, 'spoke/speaker_detail.html', context={'speaker': speaker})
