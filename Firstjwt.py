import jwt
encoded_jwt = jwt.encode({"some": "payload"}, "prasad", algorithm="HS256")
print(encoded_jwt)

decoded_jwt = jwt.decode(encoded_jwt, "prasad", algorithm="HS256")
print(decoded_jwt)