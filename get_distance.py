
#https://stackoverflow.com/questions/42686300/how-to-check-if-coordinate-inside-certain-area-python

from geopy import distance

def calculate_deo_distance(center_point_tuple, test_point_tuple, radius):
    dis = distance.great_circle(center_point_tuple, test_point_tuple).km
    print("Distance: {}".format(dis)) 
    if dis < float(radius):
        return True
    else:
        return False