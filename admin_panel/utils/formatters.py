def name_formatter(view, context, model, name):
    print(model, name)
    value = getattr(model, name)
    print(value)
    if value:
        value = value.name
    return value


def backref_formatter(view, context, model, name):
    print(model, name)
    value = getattr(model, name)
    print(value)
    if value:
        formatted_values = [item.name for item in value]
    return formatted_values
