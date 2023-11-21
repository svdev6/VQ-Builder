import json
import pandas as pd


from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse


from vqbuilder_userstories.queries import visual_query_builder
from vqbuilder_userstories.models import queries, saved_queries, commentary
from vqbuilder_userstories.serializers import queries_serializer, saved_queries_serializer, comment_serializer

@csrf_exempt
def vq_builder_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        term = data.get('term')
        score = data.get('score')
        rank = data.get('rank')
        week = data.get('week')
        refresh_date = data.get('refresh_date')
        
        results = visual_query_builder(term, score, rank, week, refresh_date)
        
        df = pd.DataFrame({'Tables': ['Term', 'Score',
                        'Rank', 'Week', 'Refresh Date']})
        
        for row in results:
            i = df[df['Tables'] == row['table_name']].index[0]
            df.loc[i, 'term'] = row['term_count']
            df.loc[i, 'score'] = row['score_count']
            df.loc[i, 'rank'] = row['rank_count']
            df.loc[i, 'week'] = row['week_count']
            df.loc[i, 'refresh_date'] = row['refresh_date_count']
        df = df.fillna(0)

        result_list = df.to_dict('records')

        return JsonResponse(result_list, safe = False)
    else:
        return HttpResponse('Please run the frontend application.', status = 405)


def show_saved_queries_view(request):
    # Fetch all SavedQuery objects from the database
    saved_queries_view = saved_queries.objects.all()
    
    # Initialize an empty list to store the queries
    queries_list = []
    
    # Loop through each SavedQuery object
    for query in saved_queries_view:
        # Create a dictionary with the query information
        query_info = {
            'id': query.id,
            'name': query.name,
            'comment': query.comment,
            'username': query.username,
            'term': query.query.term,
            'score': query.query.score,
            'rank': query.query.rank,
            'week': query.query.week,
            'refresh_date': query.query.refresh_date,
            # Use a list comprehension to create a list of comments for the query
            'comments': [{'username': comment.username, 'comment': comment.comment} for comment in query.comments.all()]
        }
        # Append the query information to the list of queries
        queries_list.append(query_info)
    
    # Return a JSON response with the list of queries
    # The safe parameter is set to False because we're passing a non-dict object
    return JsonResponse(queries_list, safe = False)


class queries_viewset(viewsets.ModelViewSet):
    queryset = queries.objects.all()
    serializer_class = queries_serializer

class saved_queries_viewset(viewsets.ModelViewSet):
    queryset = saved_queries.objects.all()
    serializer_class = saved_queries_serializer

    @action(detail = True, methods = ['GET', 'POST'])
    def create_comment(self, request, pk=None):
        # Get the SavedQuery object
        saved_query = self.get_object()
        
        # Check if the request method is POST
        if request.method == 'POST':
            # Create a new CommentModel object with the data from the request
            comment = commentary.objects.create(
                username = request.data['username'],
                comment = request.data['comment'],
                saved_query = saved_query
            )
            
        # Serialize the SavedQuery object
        saved_query_serializer = saved_queries_serializer(saved_query)
        
        # Return a response with the serialized data
        return Response(saved_query_serializer.data)


class comment_viewset(viewsets.ModelViewSet):
    queryset = commentary.objects.all()
    serializer_class = comment_serializer