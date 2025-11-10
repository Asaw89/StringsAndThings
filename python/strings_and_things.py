class StringsAndThings:
    """
    Python equivalent of the Java StringsAndThings class
    """

    def count_yz(self,input_str):
        words = input_str.split()
        count = 0
        for word in words:
            if word.endswith ('y') or word.endswith ('z'):
                count += 1
        return count

    def remove_string(self, base, remove):
       result = base
       for char in remove:
           result = result.replace(char,"")
       return result
   

    def My_Search(self,word: str,input_str: str):
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
        

    def g_is_happy(self,input_str):
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
    

    def count_triple(self, input_str):
        count = 0
        for i in range(len(input_str) - 2):
            if input_str[i] == input_str[i+1] == input_str [i+2]:
                count += 1
        return count