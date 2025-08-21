def bridge_test(event:dict, context):
    """Refreshes a token (given a valid token)
    Use case:
        (authentication)
    """
    # dump_api_gateway_event_context(event, context)

    try:
        # Validation
        print('# HELO WORLD')

        # authorization_header = EventHeadersJson.get_authorization_header(event)
        # if authorization_header is None:
        #     return endpoint_response.forbidden()

        # token_body = authorization_header.replace('TOKEN', '').strip()
        # token_is_valid = shared_token_service.verify_token(token_body)
        # if not token_is_valid:
        #     return endpoint_response.forbidden()

        # # Parse the token to get the username
        # username = shared_token_service.get_token_content(token_body)

        # data_object = {
        #     'token': shared_token_service.generate_token(username )
        # }

        # return endpoint_response.data(OperationResultMessage(
        #         operation_is_successful=True,
        #         message='Token refreshed.',
        #         data_object=data_object))

    except Exception as error:
        print(error)
        # return endpoint_response.ok(False, f'HAS ERROR: {error}')