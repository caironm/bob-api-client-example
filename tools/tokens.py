import pyotp
import argparse
import time


parser = argparse.ArgumentParser()

parser.add_argument(
    "-t", "--token",
    type=str,
    help="Bob token secret")

args = parser.parse_args()

if args.token:
    key = args.token

    prev = 0
    t = pyotp.TOTP(key, interval=90)
    while True:
        x = time.strftime("%H:%M:%S")
        n = t.now()

        if n != prev:
            prev = n
            print("{0} {1}".format(x, n))
else:
    print("Give me the key!!!")
