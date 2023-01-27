def open_with_python_txt(filename, encoding='utf-8'):
    with open(filename, 'r', encoding=encoding) as f:
        data = f.read()
    return data

def main(txtfile):
    data = open_with_python_txt(txtfile)
    print("[file.reader()]")
    print("data:", data)
    print("type(data):", type(data))
    print()

if __name__ == "__main__":
    txtfile = 'data.csv'
    delimiter = ','
    main(txtfile=txtfile)