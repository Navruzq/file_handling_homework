def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    i=0
    s=0 
    for i in data:
        if i.isdigit():
           s=s+int(i)
    return s


data = open('txt_file/data07.txt').read()
print(main(data))   
# Read data from file