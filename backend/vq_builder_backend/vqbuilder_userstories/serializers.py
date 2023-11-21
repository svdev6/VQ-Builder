from rest_framework import serializers
from vqbuilder_userstories.models import queries, saved_queries, commentary

class queries_serializer(serializers.ModelSerializer):
    class Meta:
        model = queries
        fields = ['id', 'term', 'score', 'week', 'refresh_date']

class comment_serializer(serializers.ModelSerializer):
    class Meta:
        model = commentary
        fields = ['id', 'username', 'comment', 'saved_query']

class saved_queries_serializer(serializers.ModelSerializer):
    comments = comment_serializer(many = True, read_only = True)
    class Meta:
        model = saved_queries
        fields = ['id', 'name', 'comment', 'username', 'query', 'comments']        