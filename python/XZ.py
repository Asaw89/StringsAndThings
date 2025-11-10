def count_yz(input_str):
    words = input_str.split()
    count = 0
    for word in words:
          if word.endswith ('y') or word.endswith ('z'):
                count += 1
    return count
               
                
if __name__ == '__main__':
        count= count_yz("fez day")


print (count)