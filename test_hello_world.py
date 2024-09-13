import unittest
from funcs import hello

class TestHelloWorld(unittest.TestCase):
    def test_hello_output(self):
        self.assertEqual(hello('folks'), "Hello, folks, nice to meet!")

if __name__ == "__main__":
    unittest.main()
