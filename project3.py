import json
import uuid
from argon2 import PasswordHasher

# Initialize the password hasher
ph = PasswordHasher()

def generate_uuidv4_password():
    # Generate a UUIDv4 as the password
    return str(uuid.uuid4())

def hash_password(password):
    # Hash the password using Argon2
    return ph.hash(password)

def register_user(request_body):
    try:
        # Extract username and email from the request body
        username = request_body.get("username")
        email = request_body.get("email")

        # Generate a secure password (UUIDv4)
        password = generate_uuidv4_password()

        # Hash the password using Argon2
        hashed_password = hash_password(password)

        

        # Return the password to the user
        response_data = {"password": password}
        return json.dumps(response_data), 201  # HTTP status code CREATED
    except Exception as e:
        return str(e), 400  # HTTP status code BAD REQUEST

# Example usage
request_body = {
    "username": "$MyCoolUsername",
    "email": "$MyCoolEmail"
}
response, status_code = register_user(request_body)
print(response)  
