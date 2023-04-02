import xmind_interface
import xmind
import tree

if __name__ == '__main__':
    workbook = xmind.load('sample.xmind')
    sheet = workbook.getPrimarySheet()
    sheet.setTitle("first sheet")
    root_topic = sheet.getRootTopic()
    root_topic.setTitle("root node")
    print(workbook.getData())

    workbook = xmind.load('test.xmind')
    sheet = workbook.getPrimarySheet()

    mtree = tree.Tree(sheet.getData())
    mtree.print_tree()

