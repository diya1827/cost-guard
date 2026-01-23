def lambda_handler(event, context):
    print("Cost Guard Lambda executed successfully")
    return {
        "statusCode": 200,
        "body": "Lambda ran successfully"
    }

