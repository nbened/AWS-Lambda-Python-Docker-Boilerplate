from main import main

def handler(event, context):

    arg1 = event.get('arg1', 'default1')
    arg2 = event.get('arg2', 'default2')
    
    arr = main(arg1, arg2)

    return {
        "statusCode": 200,
        "body": {"message": "Hello from Lambda!", "array": arr.tolist()}
    }


