import logging
import boto3
import json
from boto3.dynamodb.conditions import Key
logger = logging.getLogger()
logger.setLevel(logging.INFO)

class DatabaseRequests:
    def __init__(self, table_name, table_pk, table_sk):
        logger.info('db initialized!')
        dynamodb = boto3.resource('dynamodb')
        self.table = dynamodb.Table(table_name)
        self.table_pk = table_pk
        self.table_sk = table_sk


    def create_item(self, item):
        try:
            response = self.table.put_item( Item=item )
            if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                logger.info(f'Successfully created new item! --> {item}')
                return True
            else:
                return False
        except Exception as e:
            logger.error(f'Failed to create new item! Error: {e}')
            raise e

        logger.error(f'Cannot create new item because you have not included the primary key "{self.table_pk}" in the item you are trying to insert...')
        return False


    
    def delete_item(self, pk, sk):
        try:
            response = self.table.delete_item(Key={self.table_pk: pk, self.table_sk: sk})
            logger.info(response)
            if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                return True
            else:
                return False
        except Exception as e:
            logger.error(f'Failed to delete item pk:{pk}, sk:{sk}')
            raise e


    def update_item(self, pk, sk, full_name, age):
        try:
            response = self.table.update_item(
            Key={
                self.table_pk: pk,
                self.table_sk: sk
            },
            UpdateExpression="set full_name = :full_name, age = :age",
            ExpressionAttributeValues={
                ':full_name': full_name,
                ':age': age
            },
            ReturnValues="UPDATED_NEW"
            )
            if response['ResponseMetadata']['HTTPStatusCode'] == 200 and response['Attributes']:
                return response['Attributes']
            else:
                return False
        except Exception as e:
            logger.error(f'Failed to update item {self.table_pk}:{pk}, {self.table_sk}:{sk}')
            raise e


    def get_item(self, pk, sk):
        try:
            response = self.table.get_item(
                Key={
                'pk': pk,
                'sk': sk
                }
            )
            if response['ResponseMetadata']['HTTPStatusCode'] == 200 and response['Item']:
                logger.info('Success get_item')
                logger.info(response['Item'])
                return response['Item']
            else:
                return False
        except Exception as e:
            logger.error(f'Failed to get item {self.table_pk}:{pk}, {self.table_sk}:{sk}')
            raise e