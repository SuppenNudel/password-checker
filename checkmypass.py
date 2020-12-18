import requests
import hashlib
import sys


def request_api_data(query_char):
    url = f'https://api.pwnedpasswords.com/range/{query_char}'
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {res.status_code}, check the api and try again')
    else:
        return res


def sha1(string):
    return hashlib.sha1(string.encode('utf-8')).hexdigest().upper()


def get_password_leaks_coint(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count

    return 0


def pwned_api_check(password):
    sha1password = sha1(password)
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    count = get_password_leaks_coint(response, tail)
    return count


def main(passwords_list):
    for password in passwords_list:
        count = pwned_api_check(password)
        if count:
            print(
                f'"{password}" was found {count} time... you should probably change your password')
        else:
            print(f'"{password}" was NOT found. Carry on!')
    return 'done!'


if __name__ == "__main__":
    passwords_list = sys.argv[1:]
    if len(passwords_list) == 0:
        passwords_list.append(input("Enter a password to check: "))
    exit = main(passwords_list)
    sys.exit(exit)
