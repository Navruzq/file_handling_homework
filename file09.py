def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    s=0 
    for i in data:
        if i.isdigit():
            if s>int(i):
               s=int(i)
    return s


data = open('txt_file/data09.txt').read()
print(main(data))  
# Read data from file 