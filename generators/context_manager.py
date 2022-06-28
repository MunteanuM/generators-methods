class ContextMan:
    def __init__(self, filename):
        self.filename = filename
        print('Recieved filename')

    def __enter__(self):
        print(f'Opened {self.filename}')

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('Exit file program...')


with ContextMan('initfile') as manager:
    print('Closed file ...')
