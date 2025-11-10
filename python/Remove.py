def remove_string(base, remove):
   result = base
   for char in remove:
       result = result.replace(char,"")
   return result
   


if __name__ == '__main__':
   result= remove_string("Hello", "ell")

   print (result)