from xml.etree import ElementTree

def xml_to_bbox(gt, center=True):
    root = ElementTree.parse(gt)
    xmin = root.find('object/bndbox/xmin')
    if (xmin != None):
        xmin = int(xmin.text)
        xmax = int(root.find('object/bndbox/xmax').text)
        ymin = int(root.find('object/bndbox/ymin').text)
        ymax = int(root.find('object/bndbox/ymax').text)
    else:
        ymin = ymax = xmax = xmin = 0

    pos_x = (xmin + xmax)//2
    pos_y = (ymin + ymax)//2
    target_w = xmax - xmin
    target_h = ymax - ymin

    if center:
        return pos_x, pos_y, target_w, target_h
    else:
        return xmin, ymin, target_w, target_h