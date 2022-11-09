def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """

    l=data.split('\n')
    a=[]
    for i in l:
        a.append(len(str(i)))
    return a
# Read data from file
data = open('txt_file/data06.txt').read()
print(main(data))  