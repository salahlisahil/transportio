from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from app.models import Track


class TrackingView(View):
    def get(self, request):
        return render(request, 'track/tracking.html')

    @csrf_exempt
    def post(self, request):
        tracking_number = request.POST.get('track_id')

        if not tracking_number.isnumeric():
            data = {
                'status': 'error',
                'message': 'Invalid tracking number'
            }
            return JsonResponse(data, status=200)

        track = Track.objects.filter(tracking_number=tracking_number).first()
        if track:
            data = {
                'status': track.status,
                'from_target': track.from_target,
                'to_target': track.to_target,
                'from_longitude': track.from_longitude,
                'from_latitude': track.from_latitude,
                'to_longitude': track.to_longitude,
                'to_latitude': track.to_latitude
            }
            return JsonResponse(data, status=200)

        else:
            data = {
                'status': 'error',
                'message': 'Invalid tracking number'
            }
            return JsonResponse(data, status=200)
