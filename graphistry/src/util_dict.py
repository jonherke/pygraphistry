def assign(original, updates):
    """
    returns a new dict with original keys and updated values
    """
    return {
        key: updates[key] if key in updates else value for key, value in original.items()
    }