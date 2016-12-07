from roygbiv import *
import sys

def img_to_html(img, fil):
    '''
    Takes an image input and constructs an html file with its palette
    '''
    roy = Roygbiv(img)
    with open(fil, 'w') as fin:
        fin.write('<img src={} />\n'.format(img))
        fin.write('<p style="font-family:\'Quicksand\', sans-serif;">Average Color</p>\n')
        fin.write('<div class="box" style="width:82px;height:82px;background-color:{};">{}</div>\n'.format(roy.get_average_hex(),roy.get_average_hex()))
        fin.write('<p style="font-family:\'Quicksand\', sans-serif;">Color Palette</p>\n')
        for color in roy.get_palette_hex():
            fin.write('<div class="box" style="margin-right:10px;float:left;width:82px;height:82px;background-color:{};">{}</div>'.format(color,color))


if __name__ == "__main__":
    img_to_html(sys.argv[1], sys.argv[2])
    if not sys.argv[2]:
        raise Exception('Must provide filename in constructor')
