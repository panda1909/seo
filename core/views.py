from django.shortcuts import render
from .models import Comments,Comment_Links,Channels
import random

# Create your views here.
def home(request):
    Comments_query = list(Comments.objects.all())
    Comment_Links_query = list(Comment_Links.objects.all())
    Channels_query = list(Channels.objects.all())

    rand_comment = random.sample(Comments_query, 1)
    rand_cmnt_lnk = random.sample(Comment_Links_query, 1)
    rand_channel = random.sample(Channels_query, 1)
    print(rand_comment[0],rand_cmnt_lnk[0],rand_channel[0])
    
    context ={
        'Comment' : rand_comment[0],
        'Video' : rand_cmnt_lnk[0],
        'Channel': rand_channel[0],
    }
    return render(request, 'index.html', context)