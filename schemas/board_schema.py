BOARD_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "desc": {"type": "string"},
        "closed": {"type": "boolean"},
        "idOrganization": {"type": ["string", "null"]},
        "pinned": {"type": "boolean"},
        "url": {"type": "string"},
    },
    "required": ["id", "name", "closed", "url"],
}