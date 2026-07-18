def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    allowed: list[str] = light_spell_allowed_ingredients()
    is_valid: bool = False

    for ing in allowed:
        if ing.lower() in ingredients.lower():
            is_valid = True
            break

    if is_valid:
        return f"{ingredients} VALID"
    return f"{ingredients} INVALID"
