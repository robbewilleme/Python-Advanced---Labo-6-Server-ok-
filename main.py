from checker import check_server


def main():
    if check_server("192.168.80.45"):
        print("server online")
    else:
        print("server offline")


if __name__ == "__main__":
    main()
