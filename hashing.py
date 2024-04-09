from passlib.context import CryptContext
password_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

class Hash():

  """
  The password hashing function to hash and veriry password
  """
  def bcrypt(password:str):
    return password_context.hash(password)
  def verify(hashed, normal):
    return password_context.verify(normal, hashed)