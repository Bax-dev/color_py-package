
import unittest
from color_display import display_variable, display_any

class TestColorDisplay(unittest.TestCase):

    def test_display_variable(self):
        # Test simple variable display
        variable_name = "age"
        value = 25
        try:
            display_variable(variable_name, value)
        except Exception as e:
            self.fail(f"display_variable() raised {e} unexpectedly!")

    def test_display_any(self):
        # Test displaying any type
        variable_name = "test_var"
        value = [1, 2, 3]
        try:
            display_any(variable_name, value)
        except Exception as e:
            self.fail(f"display_any() raised {e} unexpectedly!")

if __name__ == '__main__':
    unittest.main()

    #unit test:python -m unittest test_display
