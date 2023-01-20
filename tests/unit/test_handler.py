import json

import pytest

@pytest.fixture()
def apigw_event():
    """ Generates API GW Event"""

    return {
    "body": '{ "pk": "item#1","sk": "category#1","full_name": "Some New Name","age": "88"}'
    }


def test_lambda_handler(apigw_event, mocker):

    ret = app.lambda_handler(apigw_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "message" in ret["body"]
    assert data["message"] ==  {"body": '{ "pk": "item#1","sk": "category#1","full_name": "Some New Name","age": "88"}'}
    # assert "location" in data.dict_keys()
