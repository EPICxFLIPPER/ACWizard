class InvalidModelException(Exception):
    

    def __init__(self):
        self.message = "test"

    def __str__(self):
        return self.message