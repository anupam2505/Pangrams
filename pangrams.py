def main():
    test_cases = raw_input()

    test_cases =  ''.join(e for e in test_cases if e.isalnum())
    test_cases =test_cases.lower()
    char_pangram = list(test_cases)
    check_pangrams(char_pangram)

def check_pangrams(char_panagram):
    char_dict = {}
    for elem in char_panagram:
        char_dict[ord(elem)-97] = True

    for i in range(0,26,1):
        if i in char_dict.keys():
            pass
        else:
            print "not pangram"
            return
    print "pangram"

if __name__ == "__main__":
    main()