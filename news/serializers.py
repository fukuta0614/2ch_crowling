from rest_framework import serializers
from news.models import News

class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('title', 'base_site','link','subject','date')