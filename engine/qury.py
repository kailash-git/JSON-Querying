def check_condition(actual, operator, expected):

    if operator == "==":
        return actual == expected

    elif operator == ">":
        return actual > expected

    elif operator == "<":
        return actual < expected

    elif operator == ">=":
        return actual >= expected

    elif operator == "<=":
        return actual <= expected

    return False


def run_query(data, parsed_query):

    results = []

    select_field = parsed_query["select"]
    field = parsed_query["field"]
    operator = parsed_query["operator"]
    expected = parsed_query["value"]

    for item in data:

        actual = item.get(field)

        if actual is None:
            continue

        if check_condition(actual, operator, expected):

            results.append(item.get(select_field))

    return results