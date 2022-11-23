table_of_checks = [(False, False, False),
                    (False, False, True),
                    (False, True, False), 
                    (False, True, True),
                    (True, False, False),
                    (True, False, True),
                    (True, True, False),
                    (True, True, True)]
def checkIt(x, y, z):
    return not (x or y or z) == (not x) and (not y) and (not z)

for i in table_of_checks:
    print(checkIt(i[0], i[1], i[2]))

