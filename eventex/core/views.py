from django.shortcuts import render, get_object_or_404


# Create your views here.

def home(request):
    speakers = [
        {'name': 'Grace Hopper', 'photo': 'http://hbn.link/hopper-pic'},
        {'name': 'Alan Turing', 'photo': 'http://hbn.link/turing-pic'}
    ]
    return render(request, 'index.html', {'speakers': speakers})


def speaker_detail(request, slug):
    from eventex.core.models import Speaker

    speaker = get_object_or_404(Speaker, slug=slug)

    return render(request, 'core/speaker_detail.html', {'speaker': speaker})
