def command_processor(input_provider, notification_service):
    cmd = input_provider()
    while cmd is not None:
        if cmd in 'exit':
            break
        if cmd in 'notify':
            notification_service.call()
        else:
            print(cmd)
        cmd = input_provider()
