import pyotp
import time


totp = pyotp.TOTP("JBSWY3DPEHPK3PXP")

while True:
    otp1 = str(totp.now())
    print(otp1)
    time.sleep(12)
    if totp.verify(otp1):
        print("Valid")
    else:
        print("Invalid")

# Simples