import re

def replace_whitespace_with_comma(text):
    # Replace one or more whitespace characters (including spaces, tabs, newlines) with a comma
    text = re.sub(r'\s+', ',', text)
    
    # Remove any commas at the beginning or end of the string
    text = text.strip(',')
    
    return text


with open("wish-you-were-here.txt", "r") as f:
# with open("like-a-rolling-stone.txt", "r") as f:
    txt = f.read()
    out = replace_whitespace_with_comma(txt)
    print(out)
