from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed: list[str] = dark_spell_allowed_ingredients()
    is_valid: bool = False

    for ing in allowed:
        if ing.lower() in ingredients.lower():
            is_valid = True
            break

    if is_valid:
        return f"{ingredients} VALID"
    return f"{ingredients} INVALID"
