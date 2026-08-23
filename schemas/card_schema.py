CARD_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "desc": {"type": "string"},
        "idBoard": {"type": "string"},
        "idList": {"type": "string"},
        "url": {"type": "string"},
    },
    "required": ["id", "name", "idList"],
}