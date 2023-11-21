import os 
from google.cloud import bigquery


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'GoogleTrends.json'

def visual_query_builder(term, score, rank, week, refresh_date):
    client = bigquery.Client()  
    query = f'''
            SELECT 
                'term_count' as table_name,
                COUNT(top_terms.term) as term_count,
                NULL as score_count
                NULL as rank_count,
                NULL as week_count,
                NULL as refresh_date_count
            FROM 
                bigquery-public-data.google_trends.top_terms as top_terms
            WHERE 
                top.terms.score = @score AND top_terms.rank = @rank AND top_terms.refresh_date = @refresh_date
            SELECT 
                'term_score' as table_name,
                COUNT(top_terms.score) as score_count,
                NULL as term_count
                NULL as rank_count,
                NULL as week_count,
                NULL as refresh_date_count
            FROM 
                bigquery-public-data.google_trends.top_terms as top_terms
            WHERE 
                top_terms.term = @term AND top_terms.refresh_date = @refresh_date
            SELECT 
                'rank_count' as table_name,
                COUNT(top_terms.rank) as rank_count,
                NULL as term_count
                NULL as score_count,
                NULL as week_count,
                NULL as refresh_date_count
            FROM 
                bigquery-public-data.google_trends.top_terms as top_terms
            WHERE 
                top_terms.term = @term AND top_terms.score = @score AND top_terms.refresh_date = @refresh_date
            SELECT 
                'week_count' as table_name,
                COUNT(top_terms.term) as week_count,
                NULL as score_count
                NULL as rank_count,
                NULL as week_count,
                NULL as refresh_date_count
            FROM 
                bigquery-public-data.google_trends.top_terms as top_terms
            WHERE 
                top_terms.term = @term AND top_terms.score = @score AND top_terms.rank = @rank top_terms.refresh_date = @refresh_date
        '''
    query_params = [
        bigquery.ScalarQueryParameter('term', 'STRING', term),
        bigquery.ScalarQueryParameter('score', 'INT64', int(score)),
        bigquery.ScalarQueryParameter('rank', 'INT64', int(rank)),
        bigquery.ScalarQueryParameter('week', 'STRING', week),
        bigquery.ScalarQueryParameter('refresh_date', 'STRING', refresh_date),
    ]

    job_config = bigquery.QueryJobConfig()
    job_config.query_parameters = query_params
    query_job = client.query(query, job_config = job_config)
    rows = query_job.result()
    return rows
    
    