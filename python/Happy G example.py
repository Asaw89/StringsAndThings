def g_is_happy(input_str):
    happiness = False
    Linput = len(input_str)
    for i in range(Linput-1):
        if input_str[i] == 'g':
            if i==0 and input_str[i+1] == 'g':
                happiness = True
            elif i==(Linput-1) and input_str[i-1] =='g':
                happiness = True
            elif input_str[i-1] == 'g' or input_str[i+1] == 'g':
                happiness = True
            else:
                return False
    return happiness





if __name__ == '__main__':
   result= g_is_happy("xxggxygx")

print (result)
   