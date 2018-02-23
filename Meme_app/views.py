from django.shortcuts import render
from .models import Memes

# Create your views here.

def Home(request):
    return render(request, 'Meme_app/Canvas_Base.html')
    # return render(request, 'Meme_app/Base.html')


def get_more_memes(request, from_nr):
    to = int(from_nr) + 15
    meme_list = Memes.objects.values_list("id", "title", "text1","text2", "image")[from_nr:to]
    return render(request, 'Meme_app/more_memes.html', {"meme_list": meme_list})



def get_more_canvas_memes(request, from_nr):
	to = int(from_nr) + 15
	meme_list = Memes.objects.values_list("id", "title", "text1","text2", "image")[from_nr:to]
	return render(request, 'Meme_app/more_canvas_memes.html', {"meme_list": meme_list})