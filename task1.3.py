import unittest
import base64

class TestBase64EncoderDecoder(unittest.TestCase):
    
    def test_base64_encoding(self):
        """Check if encoding works correctly."""
        data = b"hello world"
        encoded = base64.b64encode(data)
        self.assertEqual(encoded, b"aGVsbG8gd29ybGQ=")

    def test_base64_decoding(self):
        """Check if decoding works correctly."""
        encoded = b"aGVsbG8gd29ybGQ="
        decoded = base64.b64decode(encoded)
        self.assertEqual(decoded, b"hello world")

    def test_base64_decoding_invalid_data(self):
        """Check that invalid data causes an error."""
        invalid_data = b"!!!notbase64!!!"
        with self.assertRaises(base64.binascii.Error):
            base64.b64decode(invalid_data)

if __name__ == "__main__":
    unittest.main()
