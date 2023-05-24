import psycopg2
import pandas as pd


def sql_to_df(query: str, columns: list) -> pd.DataFrame:
    '''
    Retrieves starcraft player data based on the query text and returns the subsequent query as a pandas df.
    '''
    conn = psycopg2.connect(database="postgres",
                        user='postgres', password='pass', 
                        host='localhost', port='5432'
                        )
    conn.autocommit = True
    cursor = conn.cursor()
    try:
        cursor.execute(query)
    except (Exception, psycopg2.DatabaseError) as error:
        cursor.close() 
        raise Exception("Could not execute query command")

    tuples_list = cursor.fetchall()
    cursor.close()
    df = pd.DataFrame(tuples_list, columns = columns)
    #preliminary changing LeagueIndex to categorical variable
    df['LeagueIndex'] = df.LeagueIndex.astype('category')
    return df 