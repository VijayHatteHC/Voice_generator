# voicebot/views.py
import io
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from scipy.io.wavfile import write as write_wav
from .utils import generate_audio


@csrf_exempt
def generate_voice(request):
    if request.method == "POST":
        text = request.POST.get("text", "")
        if not text:
            return JsonResponse({"error": "Text is required"}, status=400)

        # Generate audio
        audio_array = generate_audio(text)

        # Convert to WAV in memory
        buffer = io.BytesIO()
        write_wav(buffer, 22050, audio_array)
        buffer.seek(0)

        return HttpResponse(buffer.read(), content_type="audio/wav")
    
    return HttpResponseNotAllowed(["POST"], "Only POST requests are allowed.")

def voice(request):
    return render(request, "index.html")
