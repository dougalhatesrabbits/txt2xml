import xml.etree.ElementTree as xmlTree
import sys
import os
import csv


def csv_reader_head(row_count, txt_path, header, separator, element):
    txt_file = os.path.basename(txt_path)

    r_name = txt_file.split(".")
    root_name = r_name[0]
    root = xmlTree.Element(root_name)
    root.text = "\n\t"
    root.set('version', '1.0')
    root.set('language', 'EN')

    row_num = 0
    col_count = 0
    reader = 'instance'

    try:
        with open(txt_path, 'rb') as f:

            if separator == ',':
                reader = csv.DictReader(f, delimiter=',')
            elif separator == ';':
                reader = csv.DictReader(f, delimiter=';')
            elif separator == '.':
                reader = csv.DictReader(f, delimiter='.')
            elif separator == ':':
                reader = csv.DictReader(f, delimiter=':')
            elif separator == '=':
                reader = csv.DictReader(f, delimiter='=')
            else:
                print("Unknown separator")
                exit(1)

            for row in reader:
                if row_num == 0:
                    header = row.keys()
                    col_count = len(header)

                xml_element = xmlTree.Element(element)
                xml_element.text = "\n\t\t"

                for col_num in range(0, col_count):
                    column = xmlTree.SubElement(xml_element, header[col_num])
                    column.text = row.get(header[col_num])

                    if col_num < col_count - 1:
                        column.tail = "\n\t\t"
                    else:
                        column.tail = "\n\t"

                    if row_count == row_num + 1:
                        xml_element.tail = "\n"
                    else:
                        xml_element.tail = "\n\t"

                    col_num += 1

                root.append(xml_element)
                row_num += 1

    except IOError:
        print "There was an error reading file"
        sys.exit()

    return root


def csv_reader(row_count, txt_path, header, separator, element):
    txt_file = os.path.basename(txt_path)

    r_name = txt_file.split(".")
    root_name = r_name[0]
    root = xmlTree.Element(root_name)
    root.text = "\n\t"
    root.set('version', '1.0')
    root.set('language', 'EN')

    row_num = 1
    col_count = len(header)
    reader = 'instance'

    try:
        with open(txt_path, 'rb') as f:
            if separator == ',':
                reader = csv.reader(f, delimiter=',')
            elif separator == ';':
                reader = csv.reader(f, delimiter=';')
            elif separator == '.':
                reader = csv.reader(f, delimiter='.')
            elif separator == ':':
                reader = csv.reader(f, delimiter=':')
            elif separator == '=':
                reader = csv.reader(f, delimiter='=')
            else:
                print("Unknown separator")
                exit(1)

            for row in reader:
                xml_element = xmlTree.Element(element)
                xml_element.text = "\n\t\t"

                for col_num in range(0, col_count):
                    column = xmlTree.SubElement(xml_element, header[col_num])
                    column.text = row[col_num]

                    if col_num < col_count - 1:
                        column.tail = "\n\t\t"
                    else:
                        column.tail = "\n\t"

                    if row_count == row_num:
                        xml_element.tail = "\n"
                    else:
                        xml_element.tail = "\n\t"
                    col_num += 1
                row_num += 1
                root.append(xml_element)

    except IOError:
        print "There was an error reading file"
        sys.exit()

    return root


def csv_writer(root, xml_path):
    tree = xmlTree.ElementTree(root)
    try:
        with open(xml_path, "w") as fh:
            tree.write(fh, encoding='utf-8', xml_declaration=True)
        xmlTree.dump(root)
    except IOError:
        print "There was an error reading file"
        sys.exit()


def get_columns():
    col = []
    enter = True
    print("Enter Column names, Q to quit\n")
    while enter:
        column = raw_input("Column: ")

        if column.upper() == 'Q':
            enter = False
        else:
            col.append(column)

    return col


def count_rows(txt_path, txt_header):
    try:
        with open(txt_path, 'rb') as f:
            if txt_header.upper() == 'Y':
                reader = csv.DictReader(f)

                data = list(reader)
                row_count = len(data)
                return row_count
            else:
                reader = csv.reader(f)
                data = list(reader)
                row_count = len(data)

    except IOError:
        print "There was an error reading file"
        sys.exit()

    return row_count


def main():
    header = []
    txt_header = raw_input("File has header (Y/N): ")

    separator = raw_input("Separator? (;:,.=) ")
    element = raw_input("Element? (food,book,user etc.) ")

    row_count = count_rows(sys.argv[1], txt_header)

    if txt_header.upper() == 'N':
        header = get_columns()
        root = csv_reader(row_count, sys.argv[1], header, separator, element)
    else:
        root = csv_reader_head(row_count, sys.argv[1], header, separator, element)

    csv_writer(root, sys.argv[2])


if __name__ == "__main__":
    main()
