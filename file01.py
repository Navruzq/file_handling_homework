def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    l=data.split(',')
    a=[]
    for i in l:
        a.append(int(i))
    return a
f=open("./txt_file/data01.txt")
data=f.read()
print(main(data))


# Read data from file
  