def print_file_info(file_name):
    f = None
    try:
        fr = open(file_name, "r", encoding="utf-8")

        print(fr.read())
    except Exception as e:
        print(f"文件不存在{e}")
    finally:
        if fr:
            fr.close()


def append_to_file(file_name, data):
    fw = open(file_name, "a", encoding="utf-8")
    fw.write(data)
    fw.write("\n")
    fw.flush()
    fw.close()


if __name__ == '__main__':
    print_file_info("D:/b1.txt")
    append_to_file("D:/b1.txt","123")
