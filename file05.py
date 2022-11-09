def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a=[]
    for i in data:
        if i.isdigit():
            a.append(i)
     
    b=[]
    for i in data:
        if i.isdigit():
            0
        else:
            b.append(i)
    a=[len(a),len(b)]
    return a
# Read data from file
data = open('txt_file/data05.txt').read()
print(main(data)) 