import json

def lambda_handler(event, context):
    print(event)
    json_str = json.dumps(event)
    resp = json.loads(json_str)
    body = resp['body']
    body_obj = json.loads(body)
    number1 = body_obj["number1"]
    number2 = body_obj["number2"]
    sum = number1 + number2
    return {
        'statusCode': 200,
        'body': json.dumps('The sum of ' + str(number1) + ' and ' +str(number2) + ' is: '+ str(sum))
    }