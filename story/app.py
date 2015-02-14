from story.models import posts
from serializers import postsSerializer

from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

class PostList(APIView):
	def get(self, request, format=None):
		entries = posts.objects.all()
		serialized_posts = postsSerializer(entries, many=True)
		return Response(serialized_posts.data)