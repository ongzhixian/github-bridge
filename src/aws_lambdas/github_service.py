def example(event:dict, context):
    """Example lambda function
    Use case:
        (example) This function is used to demonstrate how to handle an AWS Lambda event.
    """

    try:
        print('Example Lambda function triggered with event:', event)
    except Exception as error:
        print(error)
        