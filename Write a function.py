def is_leap(year):

    if 1900 <= year <= 10 ** 5:
            if (year % 400 == 0) and (year % 100 == 0):
                return True

            elif (year % 4 == 0) and (year % 100 != 0):
                return True

            else:
                return False

    else:
        print("")


year = int(input())
print(is_leap(year))