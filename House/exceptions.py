class InvalidModelException(Exception):
    

    def __init__(self, model):
        if (model == " "):
            self.message = "Invalid Model: " + " empty"
        else:
            self.message = "Invalid Model: " + model 

    def __str__(self):
        return self.message