import unittest
from funcs import hello_world

class TestHelloWorld(unittest.TestCase):
    def test_hello_world_output(self):
        self.assertEqual(hello_world('folks'), "Hello, folks!")

if __name__ == "__main__":
    unittest.main()
