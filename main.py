from zipfile import ZipFile

def main():
    print("[+] Beginning bruteforce ")
    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as f:
            for line in f:
                password = line.strip()  # Removes newline and any extra whitespace
                try:
                    zf.extractall(pwd=password)
                    print("[+] Password found:", password.decode())
                    return
                except:
                    pass
    print("[+] Password not found in list")

if __name__ == "__main__":
    main()
