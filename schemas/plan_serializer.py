# This is basically to serialize documen coming or going to database
def individual_serial(plan) -> dict:
    # Initialize an empty dictionary to store the fields
    response_data = {
        "id": str(plan["_id"]),
        "name": str(plan["name"]),
        "status": str(plan["status"]),
        "application": str(plan["application"]),
        "duration": int(plan["duration"]),
    }

    if "mentee_id" in plan:
        response_data["mentee_id"] = str(plan["mentee_id"])

    if "mentor_email" in plan:
        response_data["mentor_email"] = str(plan["mentor_email"])
    return response_data


def list_serial(plans):
    return list(individual_serial(plan) for plan in plans)
