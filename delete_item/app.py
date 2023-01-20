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
        if 'pk' in item.keys() and 'sk' in item.keys():
            pk = item['pk']
            sk = item['sk']
            delete_item = my_database.delete_item(pk=pk, sk=sk)
            if delete_item:
                return {
                    "statusCode": 200,
                    "body": json.dumps(
                        {
                            "message": "Delete item success!",
                            "deleted_item": {
                                "pk": pk,
                                "sk": sk
                            }
                        }
                    ),
                }
    
    return {
                "statusCode": 500,
                "body": json.dumps(
                    {
                        "message": "Failed to delete item!",
                    }
                ),
            }