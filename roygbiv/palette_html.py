from roygbiv import *
import sys
from color2name import *

def img_to_html(img, fil):
    '''
    Takes an image input and constructs an html file with its palette
    '''
    roy = Roygbiv(img)
    average_hex = roy.get_average_hex()
    im = Image.open(img)
    with open(fil, 'w') as fin:
        if im.height > 720:
            fin.write('<img style="height:580px"src={} />\n'.format(img))
        else:
            fin.write('<img src={} />\n'.format(img))
        fin.write('<p style="font-family:\'Quicksand\', sans-serif;">Average Color</p>\n')
        fin.write('<div class="box" style="width:100px;height:100px;background-color:{};">{}\n{}</div>\n'.format(average_hex, average_hex, rgb_to_crayola(roy.get_average_rgb())))
        fin.write('<p style="font-family:\'Quicksand\', sans-serif;">Color Palette</p>\n')
        for color in roy.get_palette_hex():
            fin.write('<div class="box" style="margin-right:10px;float:left;width:100px;height:100px;background-color:{0};">{1}\n{2}</div>'.format(crayola[rgb_to_crayola(hex_to_rgb(color))],color,rgb_to_crayola(hex_to_rgb(color))))
            #Hexadecimal is original decimal
            #background-color is the match on the spectrum


if __name__ == "__main__":
    cut = sys.argv[1][::-1][sys.argv[1][::-1].find('.')+1:] #cuts the suffix of image
    fil = cut[::-1] + '.html'
    img_to_html(sys.argv[1], fil)
