class APIError(Exception):
    def __init__(self, message, status_code=400):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        
class NotFoundError(APIError):
    def __init__(self, message="Resource not found"):
        super().__init__(message, status_code=404)

class ValidationError(APIError):
    def __init__(self, message="Invalid input"):
        super().__init__(message, status_code=400)
