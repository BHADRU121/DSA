def powerOfNumber(base, exp):
    assert exp >= 0 and int(exp) == exp, "exponent must be positive"
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base*powerOfNumber(base, exp -1)

#print(powerOfNumber(0,0))


def power(base,exp):
    if exp == 0:
        return 1
    if(exp==1):
        return(base)
    if(exp!=1):
        return (base*power(base,exp-1))

print(power(0,1))