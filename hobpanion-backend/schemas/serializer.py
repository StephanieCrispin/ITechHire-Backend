# This is basically to serialize the document either coming or going to our database
def individual_serial(user) -> dict:
  return{
    "id":str(user["_id"]),
    "username":str(user["username"]),
    "company":str(user["company"]),
    "password":str(user["password"])
  }


# Returns a dictionary list of my todos, basically map through and return  a list of dictionaries
def list_serial(users):
  return individual_serial((dict(user)) for user in users)