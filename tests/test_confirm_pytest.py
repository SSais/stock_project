from src.sample_test import func


# This test is to confirm that pytest works
def test_answer():
    # Arrange
    test_input = 4
    expected_output = 5
    # Act
    actual_output = func(test_input)
    # Assert
    assert actual_output == expected_output
