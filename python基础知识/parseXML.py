#!/usr/bin/python
#encoding=utf-8

__author__ = '小白龙'

"""
ElementTree是Python提供解析xml的标准库，ElementTree中每个节点（即Element）具有如下属性：

tag： string对象，标识该元素类型

attrib：dictionnary对象，标识该元素属性

text：string对象，标识该元素的文本

tail：string对象，标识该元素可选的尾字符串

child elements： 标识子节点
"""

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.cElementTree as ET


if __name__ == "__main__":
    print("解析本地xml文件：")
    #加载xml文件
    tree = ET.parse("demo.xml")
    #获取根节点
    root = tree.getroot()
    print(root.tag)
    print("==============遍历================")
    print("遍历根节点：")
    for child in root:
        print(child.tag,"name:",child.attrib["name"])
    print("查找第一个country")
    country = root.find("country")
    print(country.attrib)
    print("查找所有country")
    for ct in root.findall("country"):
        print(ct.attrib)

    print("遍历第一个country的子节点")
    for sub in country:
        print(sub.tag,sub.attrib,sub.text)

    #遍历子节点
    print("使用iter迭代器查找目标节点")

    print("==============新增、修改================")
    print("新增local节点：")
    local = ET.Element("local")
    local.text = "亚洲"
    country.append(local)
    for sub in country:
        if sub.text=="亚洲":
            print(sub.tag, sub.attrib, sub.text)
            sub.set("local","非洲")
            print(sub.tag, sub.attrib, sub.text)

    print("==============删除================")
    for sub in country:
        if sub.text=="亚洲":
            country.remove(sub)
            print("删除local")

tree.write("demo.xml",encoding="utf-8")