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
        if 'pk' in item.keys() and 'sk' in item.keys() and 'full_name' in item.keys() and 'age' in item.keys():
            update_item = my_database.update_item(pk=item['pk'], sk=item['sk'], full_name=item['full_name'], age=item['age'] )
            if update_item:
                return {
                    "statusCode": 200,
                    "body": json.dumps(
                        {
                            "message": "Update item success!",
                            "new_item": update_item
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