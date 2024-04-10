# This is basically to serialize the document either coming or going to our database
def individual_serial(user) -> dict:
    # Initialize an empty dictionary to store the fields
    response_data = {
        "id": str(user["_id"]),
        "firstname": str(user["firstname"]),
        "lastname": str(user["lastname"]),
        "email": str(user["email"]),
        "role": str(user["role"]),
    }

    # Include fields conditionally
    if "specialization" in user:
        response_data["specialization"] = str(user["specialization"])

    if "about" in user:
        response_data["about"] = str(user["about"])

    if "technologies" in user and user["technologies"] is not None:
        response_data["technologies"] = list(user["technologies"])

    if "facebookURL" in user:
        response_data["facebookURL"] = str(user["facebookURL"])

    if "twitterURL" in user:
        response_data["twitterURL"] = str(user["twitterURL"])

    if "youtubeURL" in user:
        response_data["youtubeURL"] = str(user["youtubeURL"])

    return response_data

# Returns a dictionary list of my todos, basically map through and return  a list of dictionaries


def list_serial(users):
    return list(individual_serial(user) for user in users)
