from my_module import get_value


def test_get_value(mocker):
    stub_fetch_data = mocker.patch('my_module.fetch_data', return_value={"key": "stubbed value"})
    result = get_value()
    assert result == "stubbed value"

