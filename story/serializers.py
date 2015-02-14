from story.models import posts
from rest_framework import serializers

class postsSerializer(serializers.ModelSerializer):
	class Meta:
		model = posts
		fields = (
			'author',
			'title'
			)