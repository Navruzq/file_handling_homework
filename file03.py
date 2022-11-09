def main(data:str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a=[]
    for i in data:
        if i.isdigit():
            a.append(i)
    return a


data = open('txt_file/data03.txt').read()
print(main(data)) 
# Read data from file