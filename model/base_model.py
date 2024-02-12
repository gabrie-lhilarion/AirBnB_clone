

import uuid
from datetime import datetime

class BaseModel:
    """BaseModel class for other classes to inherit common attributes/methods."""
    
    def __init__(self):
        """Initialize a new instance of the BaseModel class."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return a string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the public instance attribute updated_at with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__ of the instance."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

# Example usage:
if __name__ == "__main__":
    base_model_instance = BaseModel()
    print(base_model_instance)
    
    # Update and save
    base_model_instance.save()
    print(base_model_instance)
    
    # Convert to dictionary
    base_model_dict = base_model_instance.to_dict()
    print(base_model_dict)