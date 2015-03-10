import xml.etree.ElementTree as ET
import pystache
import re

tree = ET.parse('menu.svg')
root = tree.getroot()
renderer = pystache.Renderer()

screen_counter = 1
if 'id' in root.attrib:
    screen_id = root.attrib['id']
else:
    screen_id = repr(screen_counter)

prev_item = None
items = list()
item_counter = 1
for child in root:
    if 'id' in child.attrib:
        item_id = child.attrib['id']
    else:
        item_id = repr(item_counter)

    colour = None
    if 'style' in child.attrib:
        fills = re.match('fill: (#?\w+)', child.attrib['style'])
        if fills != None:
            fill = fills.group(1)[1:]
            r, g, b = fill[:2], fill[2:4], fill[4:]
            r, g, b = [int(n, 16) for n in (r, g, b)]
            colour = {
                'red': r,
                'green': g,
                'blue': b
            }


    view_data = {
        'item_counter': item_counter,

        'item_id': item_id,
        'screen_id': screen_id,
        'item_id_upper': item_id.upper(),
        'screen_id_upper': screen_id.upper(),

        'startx': child.attrib['x'],
        'starty': child.attrib['y'],
        'endx': int(child.attrib['x']) + int(child.attrib['width']),
        'endy': int(child.attrib['y']) + int(child.attrib['height'])
    }

    if prev_item != None:
        view_data['prev_item'] = prev_item

    if colour != None:
        view_data['colour'] = colour

    print (renderer.render_path(child.tag + '.mustache', view_data))

    item_counter += 1
    prev_item = item_id
