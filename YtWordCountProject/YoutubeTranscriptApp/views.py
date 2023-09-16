from django.shortcuts import render
from youtube_transcript_api import YouTubeTranscriptApi



# Create your views here.

def wordTranscriptCount(request):
    if request.method=="POST":
        video_url=request.POST['yt_url']
        query=request.POST['query']
        video_id=video_url[::-2]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        word_count="word_count obtained after the checking the json object "
        return render(request, 'home.html', {'word_count':word_count})
    else:
        return render(request, 'home.html')
        
    pass

