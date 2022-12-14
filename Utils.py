import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import numpy.ma as ma
import cmocean

from matplotlib.animation import FuncAnimation
from matplotlib import animation, rc

def make_animation(time,mask,variable,
                           interval=10):
    '''
    Animation of nextsim simulation outputs for one variable
    time : time serie
    mask : mask of the dataset
    variable : variable of interest
    interval : time (ms) between 2 frames (typically 20ms)
     '''
    
    fig, ax1 = plt.subplots(1, 1 ,figsize=(15,15))
    
    
    ax1.set_title('Truth',loc='right')
    ax1.set_title('Date : {} '.format(time[0].strftime('%Y.%m.%d')), loc = 'left')
    
    
    ax1.set_facecolor('xkcd:putty')
    
    cmap = cmocean.cm.ice
    im1 = ax1.imshow(variable[0],cmap=cmap,origin = 'lower',animated=True,vmax = 2.5)
    

    def animate(i):
        im1.set_array(variable[i])
       
        ax1.set_title('Date :{} '.format(time[i].strftime('%Y.%m.%d')), loc = 'left')
       
        return [im1]
    Nt = np.shape(variable)[0]

    anim = animation.FuncAnimation(fig, animate, frames=40,
                                   interval=interval, blit=True)
    plt.show()
    return anim

def time_series_plot(time, variable, mask, save_name, title): 
    ''' 
    plot the time serie mean of any Masked Array and save the figure
    Inputs : 
    - time (datetime array)
    - vzriable : variable of interest
    - mask : mask of the variable
    - save_name : figure name for saving
    - title : plot title
    '''
    
    fig, ax = plt.subplots(1, 1, figsize = (15,5))
    T = np.shape(variable)[0]
    mean = np.zeros(T)
    std = np.zeros(T)
    for t in range(T):
        mean[t] = np.mean(variable[t][variable[t].mask == False])
    plt.plot(time, mean, '.--')
    plt.xlabel('Time')
    plt.ylabel('Average value')
    plt.title(title)
    plt.savefig(save_name +'.png')
    


    