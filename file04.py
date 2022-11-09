def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a=[]
    for i in data:
        if i.isdigit():
            0
        else:
            a.append(i)
    return a   
# Read data from file
data = open('txt_file/data04.txt').read()
print(main(data)) 