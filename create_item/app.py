import json
import logging
from database_requests import DatabaseRequests
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    my_database = DatabaseRequests(table_name='test-dynamo-table', table_pk='pk', table_sk='sk')
    logger.info('event received!')
    logger.info(event)

    if 'body' in event:
        item = json.loads(event.get('body'))
        create_item = my_database.create_item(item=item)
        if create_item:
            return {
                "statusCode": 200,
                "body": json.dumps(
                    {
                        "message": "Create item success!",
                        "new_item": item
                    }
                ),
            }
    
    return {
                "statusCode": 500,
                "body": json.dumps(
                    {
                        "message": "Failed to create item!",
                    }
                ),
            }
