import csv
import pandas as pd

def open_with_python_csv(filename, delimiter=','):
    data = []
    with open(filename, 'r') as filename:
        reader = csv.reader(filename, delimiter=delimiter)
        # ヘッダ行は特別扱い
        header = next(reader)
        # 中身
        data.append([x for x in next(reader)])
    return header, data


def open_with_pandas(filename):
    df = pd.read_csv(filename)
    header = df.columns.values.tolist()
    data = df.values
    return df, header, data


def main(csvfile, delimiter):
    header, data = open_with_python_csv(csvfile, delimiter=delimiter)
    print("[csv.reader()]")
    print("header:", header)
    print("data:", data)
    print("type(data):", type(data))
    print()

    df, header, data = open_with_pandas(csvfile)
    print("[pandas.read_csv()]")
    print("df:", df) # pandasの操作を行うときはdfを使う
    print("header:", header)
    print("data:", data)
    print("type(df):", type(df))
    print("type(header):", type(header))
    print("type(data):", type(data))
    print()


if __name__ == "__main__":
    csvfile = 'data.csv'
    delimiter = ','
    main(csvfile=csvfile, delimiter=delimiter)