class InvalidElevationException(Exception):
    

    def __init__(self, elevation):
        if (elevation == " "):
            self.message = "Invalid Elevation: " + " empty"
        else:
            self.message = "Invalid Elevation: " + elevation 

    def __str__(self):
        return self.message