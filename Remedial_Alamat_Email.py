
def namauser(user):

    hurufangkasimbol = "abcdefghijklmnopqrstuvwxyz0123456789-_"
    validuser = False

    for i in user:
        if i not in hurufangkasimbol:
            validuser = False
            break
        else:
            validuser = True
    return validuser


def hosting(host):

    hurufangka = "abcdefghijklmnopqrstuvwxyz0123456789"
    validhost = False

    for i in host:
        if i not in hurufangka:
            validhost = False
            break
        else:
            validhost = True
    return validhost


def ekstensi(ext):

    huruf = "abcdefghijklmnopqrstuvwxyz"
    validext = False

    if 0 < len(ext) <= 5:
        for i in ext:
            if i not in huruf:
                validext = False
                break
            else:
                validext = True
        return validext
    else:
        return validext


def validall(email):

    email1 = email.split(".")
    email2 = email1[0].split("@")

    if len(email2) < 2:
        print()
        print("Hasil : EMAIL TIDAK VALID")
    else:
        email2.append(email1[1])

        validuser = namauser(email2[0])
        validhost = hosting(email2[1])
        validext = ekstensi(email2[2])

        if validuser and validhost and validext:
            print()
            print("Hasil : EMAIL VALID")
        else:
            print()
            print("Hasil : EMAIL TIDAK VALID")
    
    return

if __name__ == "__main__":
    email = input("Input email : ")

    validall(email)