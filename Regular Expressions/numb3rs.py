import re
import sys

def validate(ip: str) -> bool:
    split_ip = ip.split(".")
    if len(split_ip) != 4:
        return False
    for s in split_ip:
        try:
            num = int(s)
            if num < 0 or num > 255:
                return False
        except ValueError:
            return False
    return True

if __name__ == "__main__":
    inp = input("Endereço IPv4: ").strip()
    if validate(inp):
        print(f"{inp} it's valid IP")
    else:
        print(f"{inp} it's not a valid IP")
