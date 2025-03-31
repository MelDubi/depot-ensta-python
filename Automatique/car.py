# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt 
import numpy as np

def dist_to_track(x,track):
    """
    Computes the distance between the car and the point of the track
    perpendicular to it
    Input: x car state vector, track the track shape as an
    array of vertices
    Output: the distance
    """
    p=np.array([[np.sin(x[2])],[-np.cos(x[2])]])
    m=np.array([[x[0]],[x[1]]])
    d=np.inf

    det=np.linalg.det    
    
    for j in range(track.shape[1]-1):
        a=track[np.newaxis,:,j].T  
        b=track[np.newaxis,:,j+1].T
        det1=det(np.bmat((a-m,p)))
        det2=det(np.bmat((b-m,p)))
        det3=det(np.bmat((a-m,b-a)))
        det4=det(np.bmat((p,b-a)))
        if det1*det2<=0 and det3/det4 >=0:
            d=np.min((det3/det4,d))
            
    return d

def draw(x,dist=0,track=None,size=60):
    """
    Draw the car, the track and the distance between the car and the track
    Input: x car state vector
    Optional input: distance (see above), track the track shape as an array of vertices 
    (default None=no track drawn), size: window height/width
    """
    if not hasattr(draw, "axes"):
        #create an empty figure and its axes
        draw.fig, draw.axes = plt.subplots()      
        draw.axes.set_xlabel("Meters")
        draw.axes.set_ylabel("Meters")
        draw.axes.set_title("Car trajectory")        
        draw.car_shape=np.array([[-1,4,5,5,4,-1,-1,-1,0,0,-1,1,0,0,-1,1,0,0,3,3,3],
                                    [-2,-2,-1,1,2,2,-2,-2,-2,-3,-3,-3,-3,3,3,3,3,2,2,3,-3],
                                    np.ones(21)])
        draw.wheel_shape=np.array([[-1,1],[0,0],[1,1]])
        
        #we will use set_data on several plots to animate the car this
        #is unefficient but very easy to understand how it works for
        #first year students
        
        draw.plots={"car": draw.axes.plot([0],[0])[0],
                    "rfw": draw.axes.plot([0],[0], color="red")[0],
                    "lfw": draw.axes.plot([0],[0], color="red")[0],
                    "track": draw.axes.fill([0],[0], color="green")[0],
                    "dist": draw.axes.plot([0],[0], color="red")[0]
                    }
        #draw the track
        if track is not None:
            draw.plots["track"].set_xy(track.T)
            draw.xc,draw.yc=np.mean(track, axis=1)
        else:
            draw.xc,draw.yc=(0,0)

    x=x.flatten()
    draw.axes.set_xlim((-size/2+draw.xc,size/2+draw.xc))
    draw.axes.set_ylim((-size/2+draw.yc,size/2+draw.yc))
    
    #rotate car shape
    rot_car=np.array([[np.cos(x[2]),-np.sin(x[2]),x[0]],
                    [np.sin(x[2]),np.cos(x[2]),x[1]],
                    [0,0,1]])
    car=np.dot(rot_car,draw.car_shape)

    #rotate right front wheel
    rot_rfw=np.array([[np.cos(x[4]),-np.sin(x[4]),3],
                    [np.sin(x[4]),np.cos(x[4]),3],
                    [0,0,1]])
    rfw=np.dot(np.dot(rot_car,rot_rfw),draw.wheel_shape)
    #rotate left front wheel
    rot_lfw=np.array([[np.cos(x[4]),-np.sin(x[4]),3],
                    [np.sin(x[4]),np.cos(x[4]),-3],
                    [0,0,1]])
    lfw=np.dot(np.dot(rot_car,rot_lfw),draw.wheel_shape)

    #draw the car
    draw.plots["car"].set_data(car[0,:],car[1,:])
    draw.plots["rfw"].set_data(rfw[0,:],rfw[1,:])
    draw.plots["lfw"].set_data(lfw[0,:],lfw[1,:])
    


    #draw the vector between track and car
    car_to_track=np.array([[x[0],x[0]+np.sin(x[2])*dist],
                            [x[1],x[1]-np.cos(x[2])*dist]])
                            
    
    draw.plots["dist"].set_data(car_to_track[0,:],car_to_track[1,:])
    plt.pause(0.001)


if __name__=="__main__":
    track=np.array([[-10,-15,-10,0,10,20,32,35,30,20,0,-10],
                    [-5,0,5,15,20,20,15,10,0,-6,-6,-5]])
    
    x=np.array([0,20,np.pi/3,0,np.pi/4])
    d=dist_to_track(x,track)
    draw(x,d,track)
    #garde la fenêtre ouverte si on n'est pas dans spyder
    import os
    if not any(["SPYDER" in name for name in os.environ]):
        plt.show()
