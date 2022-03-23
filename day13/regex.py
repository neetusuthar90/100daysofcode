import re
def char(s):
     ch = re.compile(r'[^a-z0-9]')
     str = ch.search(s)
     return not bool(s)

def match_fun(val):
    k = re.match('[^a-z0-9]',val)
    return bool(k)

print(match_fun("abcd12234")) ## Return false this does not match
print(match_fun("@#$%^&"))  ## Return true becuse it is matched
print(char("abcd12234"))   
print(char("@#$%^&"))