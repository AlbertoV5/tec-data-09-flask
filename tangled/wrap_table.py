# [[file:../readme.org::wrap_table.py][wrap_table.py]]
data=""
from xml.etree.ElementTree import Element, SubElement, dump

def build_row(parent: Element, data: str, tag: str) -> Element:
    child = SubElement(parent, "tr")
    for s in data.split("\t"):
        SubElement(child, tag).text = s
    return child
# XML
def build_html(data: str) -> Element:
    data = data.split("\n")
    table = Element("table")
    build_row(table, data[0], "th")
    for row in data[1:-1]:
        build_row(table, row, "td")
    return table

table = build_html(data)
dump(table)
# wrap_table.py ends here
