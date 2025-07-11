from sanitizer.cli import sanitize_json

def test_sanitize_json():
    raw = '{"a":1,"b":2}'
    expected = '{\n    "a": 1,\n    "b": 2\n}'
    assert sanitize_json(raw) == expected
