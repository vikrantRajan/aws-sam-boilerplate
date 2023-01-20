import json
import logging
from database_requests import DatabaseRequests
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    my_database = DatabaseRequests(table_name='test-dynamo-table', table_pk='pk', table_sk='sk')
    logger.info('event received!')
    logger.info(event)

    if 'queryStringParameters' in event:
        item = json.loads(event.get('queryStringParameters')) if type(event.get('queryStringParameters')) == str else event.get('queryStringParameters')
        if 'pk' in item.keys() and 'sk' in item.keys():
            pk = item['pk']
            sk = item['sk']
            get_item = my_database.get_item(pk=pk, sk=sk)
            if get_item:
                return {
                    "statusCode": 200,
                    "body": json.dumps(
                        {
                            "message": "Get item success!",
                            "item": get_item
                        }
                    ),
                }
    
    return {
                "statusCode": 500,
                "body": json.dumps(
                    {
                        "message": "Failed to get item!",
                    }
                ),
            }