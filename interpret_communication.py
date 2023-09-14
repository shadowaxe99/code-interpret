class Communication:
    def __init__(self):
        pass

    def get_user_input(self):
        user_input = input('Enter your command: ')
        return user_input

    def send_agent_response(self, response):
        print('Agent response: ', response)