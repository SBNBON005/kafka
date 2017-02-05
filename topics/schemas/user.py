import copy

def get_user_details_schema():   
    schema = {
        "type": "object",
        "required": ["name"]
        "property": {
            "name": {"type": "string"},
            "surname": {"type": "string"},
            "cell_number": {"type": "integer"}
        }
    }
    return copy.deepcopy(schema)

FOO_TYPE_SCHEMA = {
    "user_details": "get_user_details_schema"
}