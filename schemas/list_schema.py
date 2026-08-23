LIST_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "closed": {"type": "boolean"},
        "idBoard": {"type": "string"},
        "pos": {"type": "number"},
    },
    "required": ["id", "name", "closed", "idBoard"],
}