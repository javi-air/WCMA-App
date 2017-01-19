def blend(c1,c2,n):
    '''
    Takes two colors,c1 and c2, and finds n number of colors in between
    '''
    points = []
    for i,j in zip(range(1,n+1),reversed(range(1,n+1))):
        point = (((i*c1[0]+j*c2[0])/(n+1)),((i*c1[1]+j*c2[1])/(n+1)),((i*c1[2]+j*c2[2])/(n+1)))
        points.append(point)
    return points
