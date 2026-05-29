import re

def parse_query(query):
    pattern = r"SELECT (.+) WHERE (\w+) (==|>|<|>=|<=) (.+)"

    match = re.match(pattern, query)

    if not match:
        raise Exception("Invalid Query")

    select_field, field, operator, value = match.groups()

    # Remove quotes if string
    value = value.strip('"')

    # Convert numbers
    if value.isdigit():
        value = int(value)

    return {
        "select": select_field.strip(),
        "field": field.strip(),
        "operator": operator.strip(),
        "value": value
    }