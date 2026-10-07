import logging

logger = logging.getLogger(__name__)


def deep_compare(actual, expected, path="root"):
    logger.info("Comparing value at %s: actual=%s, expected=%s", path, actual, expected)

    if type(actual) != type(expected):
        return f"Type mismatch at {path}: {type(actual)} != {type(expected)}"

    # Compare dicts. The expected object may be a subset of the actual payload,
    # so we only validate the keys that are explicitly expected.
    if isinstance(actual, dict):
        for key in expected:
            if key not in actual:
                return f"Missing key at {path}.{key}"
            result = deep_compare(actual[key], expected[key], f"{path}.{key}")
            if result:
                return result

        return None

    # Compare lists
    if isinstance(actual, list):
        if len(actual) != len(expected):
            return f"List length mismatch at {path}: {len(actual)} != {len(expected)}"

        for index, (a_item, e_item) in enumerate(zip(actual, expected)):
            result = deep_compare(a_item, e_item, f"{path}[{index}]")
            if result:
                return result

        return None

    # Compare primitive values
    if actual != expected:
        return f"Value mismatch at {path}: expected {expected}, got {actual}"

    return None
