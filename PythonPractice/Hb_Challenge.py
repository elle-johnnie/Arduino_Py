## Hackbright Challenge test
# LJohnson
# Member Number Validator###
# 1. member num must end in 0 or 1
# 2. member num must not contain alpha/must only be 0-9 numerics
# 3. if yes to both then:  0 index up to but not included last digit, * every other number by 5, maintain non multiplied
#    numbers and their index position
# 3. b.(sum of all the numbers (except the last))  % (last digit) if == 0 then valid
####Fcn returns True if valid/False if invalid

## demo:  123456789023453 = True
## demo:  123456789023455 = False (breaks rule 3)
## demo: 123456789023451 = False (ends w/ 1)
## demo:  12345ABCD023453 = False (contains alpha)

valid = False


def validator(memNum):
    global valid
    # get last number of mem num via index pos
    last = int(memNum[-1])
    # pass if last digit of memNum not 0/1
    if last != 0 and last != 1:
        try: # test if memnum can be converted to integer
            int(memNum)
            # get length of characters in memNum
            getall = len(memNum)

            listNum = []
            # convert memNum to list of single digits
            for i in range(getall):
                listNum.append(int(memNum[i]))
            # print listNum
            # set listLgth to ignore last digit in memNum list
            listLgth = (len(listNum)-1)
            # iterate over the truncated list
            for i in range(listLgth):
                # if iterator is one of every other number starting
                # with index 0 then multiply that number by 5 and replace position in list
                # else maintain original value
                if i == 0 or i % 2 == 0:
                    listNum[i] = (listNum[i]*5)
                else:
                    pass
            # print listNum
            # sum of all items in list except for last number
            total = sum(listNum[:-1])
            # print ('total: ' + str(total))
            lasttest = int(total) % int(last)
            # print ('mod: ' + str(lasttest))
            # determine final pass if modulus of sum == 0
            if lasttest == 0:
                valid = True
                print "The following member number is valid:"
            else: # fails if modulus of sum != 0
                valid = False
                print 'Sorry, the following member number is not valid(unmet rule #3): '

        except ValueError:  # print value error if can't convert to int
            valid = False
            print 'The member number must contain only numeric characters (unmet rule #2).'

    else:  # fail if ends in 0/1
        valid = False
        print 'The following member number is not valid (unmet rule #1):'


# test sample data
memList = ["123456789023453", "123456789023455", "123456789023451", "12345ABCD023453"]
for member in memList:
    validator(member)
    print member
    print valid
    print ('-' * 15)

