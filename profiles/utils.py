import uuid


def generate_ref_code():
    code = str(uuid.uuid4().int).replace("_", "")[:3]
    return code
