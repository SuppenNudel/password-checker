import unittest
import checkmypass


class TestMain(unittest.TestCase):
    def test_request_api_data_ok(self):
        query_char = 'CBFDA'
        result = checkmypass.request_api_data(query_char)
        self.assertEqual(result.status_code, 200)

    def test_request_api_data_fail(self):
        query_char = 'abc123'
        try:
            checkmypass.request_api_data(query_char)
        except Exception as err:
            self.assertIsInstance(err, RuntimeError)

    def test_sha1(self):
        string = 'somestring'
        sha1 = checkmypass.sha1(string)
        self.assertEqual(sha1, 'DA63FB69AEB03C776BD23E91E2C1CB3DF30135D3')

    def test_pwned_api_check(self):
        string = 'abcdef123'
        res = checkmypass.pwned_api_check(string)

    def test_main(self):
        checkmypass.main(['password'])


if __name__ == "__main__":
    unittest.main()
