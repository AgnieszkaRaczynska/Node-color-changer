import nuke

nuke.selectedNode()['tile_color'].value()

def set_tile_color(the_node, r=1, g=0, b=1):
    """
    sets the tile color based on the rgb colors provided

    """

    the_node['tile_color'].setValue(rgb_to_color(r,g,b))


def rgb_to_color(r, g, b):
    """
    converts rgb to nuke tile color based on 0-1 RGB values 

    """

    r = min(r, 1)
    r = max(r, 0)
    r = int(r*255)
    
    g = 1 if g > 1 else g
    g = 0 if g < 0 else g
    g = int(g*255)
    
    b = max(min(b, 1), 0)
    b = int(b*255)
    
    a = 1
    a = int(a*255)

    new_color = (r<<24) + (g<<16) + (b<<8) + (a<<0)

    return new_color

nodes = nuke.selectedNodes()

for node in nodes:
    set_tile_color(node, 1,.5,0)