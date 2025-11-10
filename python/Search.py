def My_Search(word: str,input_str: str):
    Lword = len(word)
    linput = len(input_str)
    numword = 0
    start = 0

    index = input_str.find(word,start)
    if index>=0: 
        numword+=1
        start = index+Lword 
    while index >= 0 and start<(linput-Lword):
        index = input_str.find(word,start)
        if index>=0:
            numword+=1
            start = index+Lword 
      

    return numword
  


if __name__ == '__main__':
   not_result= My_Search("not", "this is not")
   is_result= My_Search("is", "this is not")

   print (f"{is_result}=={not_result} is {is_result==not_result}")