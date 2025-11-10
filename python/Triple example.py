def count_triple(input_str):
    count = 0
    for i in range(len(input_str) - 2):
        if input_str[i] == input_str[i+1] == input_str [i+2]:
            count += 1
    return count



if __name__ == '__main__':
   count= count_triple("abcXXXabc")

print (count)
   