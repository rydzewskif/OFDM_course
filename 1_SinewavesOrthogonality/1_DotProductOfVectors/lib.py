import numpy as np                 # v 1.19.2
import matplotlib.pyplot as plt    # v 3.3.2

from math import ceil, floor, cos, sin

from matplotlib import transforms

from matplotlib.ticker import MaxNLocator

#========================================================

def are_all_vectors_integer(v1,v2):
    r = all([(i%1)<0.00001 for i in v1+v2])
    return r

def show_vectors(v_g, v_b, x_range, y_range, axes_name,grid,coordinates,shift):
    
    xs,ys = zip(v_g,v_b)
    colors = 'g', 'b'
    
    # Select length of axes and the space between tick labels
    xmin, xmax, ymin, ymax = floor(min(xs)), ceil(max(xs)), floor(min(ys)), ceil(max(ys))
    
    x_range_t = x_range if x_range else (min(-1,xmin-1), max(1,xmax+1))           
    y_range_t = y_range if y_range else (min(-1,ymin-1), max(1,ymax+1))           
    
    ticks_frequency = 1
    
    # Figure
    fig, ax = plt.subplots(figsize=(4, 4))
    
    # Points
    ax.scatter(xs, ys, c=colors)
    
    # Plot vectors
    shift_coef = 0.1 if v_g[0]==v_b[0] and v_g[1]==v_b[1] and  shift else 0
    for i, (x, y, c) in enumerate(zip(xs, ys, colors)):   
        plt.annotate('',xy=(x,y+(i*shift_coef)),xytext=(0,0+(i*shift_coef)), arrowprops=dict(arrowstyle='-|>, head_width=0.5,head_length=1.5',color=c,lw=3))
    
    if coordinates:
        for i, (x, y, c) in enumerate(zip(xs, ys, colors)):   
            txt_x = x
            txt_y =  y+0.3 if y >= 0  else y-0.6
            
            props = dict(edgecolor='white',facecolor='white', alpha = 0.5 if shift_coef == 0 else 0  )
            
            txt= f'{x:0.2f}, {y:0.2f}' if not are_all_vectors_integer(xs,ys) else f'{x:0.0f}, {y:0.0f}'
            ax.text(txt_x+(i*shift_coef),txt_y+(i*shift_coef), txt, color=c,fontsize=15,bbox=props)
    
            # t.set_bbox(dict(facecolor='red', edgecolor='red', alpha=0.0))
    
    # Set identical scales for both axes
    ax.set(xlim=x_range_t, ylim=y_range_t, aspect='equal')
    
    # Set bottom and left spines as x and y axes of coordinate system
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    
    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Axes labels
    if axes_name:
        ax.set_xlabel('x', size=15, labelpad=15, x=1)
        ax.set_ylabel('y', size=15, labelpad=-30, y=1, rotation=0)
    
    # Ticks
    x_ticks = np.arange(*x_range_t, ticks_frequency)
    y_ticks = np.arange(*y_range_t, ticks_frequency)
    
    ax.set_xticks(x_ticks[x_ticks != 0])
    ax.set_yticks(y_ticks[y_ticks != 0])
    
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    
    # Axes arrows
    arrow_fmt = dict(markersize=10, color='black', clip_on=False)
    ax.plot(1, 0, marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
    ax.plot(0, 1, marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)
    
    # grid
    if grid:
        ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.4)
    
#    # dot
#    if not are_all_vectors_integer(xs,ys):
#        dot = f'{(v_g[0]*v_b[0])+(v_g[1]*v_b[1]):0.2f}'
#    else:
#        dot = f'{(v_g[0]*v_b[0])+(v_g[1]*v_b[1]):0.0f}' 
#    plt.title('dot product:' + dot,pad=20,fontsize = 15,color='red')

    
    plt.show()
        
def rainbow_text(x,y,ls,lc,**kw):
    fig, ax = plt.subplots(figsize=(1, 0.4))
    t = plt.gca().transData    
    
    #horizontal version
    for s,c in zip(ls,lc):
        text = plt.text(x,y,s,color=c, transform=t, **kw)
        text.draw(fig.canvas.get_renderer())
        ex = text.get_window_extent()
        t = transforms.offset_copy(text._transform, x=ex.width, units='dots')   
    ax.set_axis_off()
    plt.show()

def show_dot_product_value(v_g, v_b, precision = True):  
    xs,ys = zip(v_g,v_b)  
    
    if not are_all_vectors_integer(xs,ys):
        dot = f'{(v_g[0]*v_b[0])+(v_g[1]*v_b[1]):0.2f}'
    else:
        dot = f'{(v_g[0]*v_b[0])+(v_g[1]*v_b[1]):0.0f}'         
        
    tokens = ('Dot Product: ',f'{dot}')
    colors = ['black','red']
    
    rainbow_text(0,0,tokens, colors,size=15)

def show_dot_product_calculations(v_g, v_b, precision = True):  
    xs,ys = zip(v_g,v_b)  
    
    if not are_all_vectors_integer(xs,ys):
        v_g_0 = f'{v_g[0]:0.2f}'
        v_g_1 = f'{v_g[1]:0.2f}'

        v_b_0 = f'{v_b[0]:0.2f}'
        v_b_1 = f'{v_b[1]:0.2f}'

        dot = f'{(v_g[0]*v_b[0])+(v_g[1]*v_b[1]):0.2f}'
    else:
        v_g_0 = f'{v_g[0]:0.0f}'
        v_g_1 = f'{v_g[1]:0.0f}'

        v_b_0 = f'{v_b[0]:0.0f}'
        v_b_1 = f'{v_b[1]:0.0f}'

        dot = f'{(v_g[0]*v_b[0])+(v_g[1]*v_b[1]):0.0f}'         
        
    tokens = f'(_{v_g_0}_, _{v_g_1}_) * (_{v_b_0}_, _{v_b_1}_) = (_{ v_g_0}_*_{ v_b_0}_) + (_{ v_g_1}_*_{ v_b_1}_) = _{dot}'.split('_')
    colors = ['black','g','black','g','black','b','black','b','black','g','black','b','black','g','black','b','black','red']
    
    tokens = f'(_x_, _y_) * (_x_, _y_) = (_{v_g_0}_, _{v_g_1}_) * (_{v_b_0}_, _{v_b_1}_) = (_{ v_g_0}_*_{ v_b_0}_)+(_{ v_g_1}_*_{ v_b_1}_) = _{dot}'.split('_')
    colors = ['black','g','black','g','black','b','black','b','black','g','black','g','black','b','black','b','black','g','black','b','black','g','black','b','black','red']

    rainbow_text(0,0,tokens, colors,size=15)
    
def rotate_vector(vec,deg):
    theta = np.deg2rad(deg)
    rot = np.array([[cos(theta), -sin(theta)], [sin(theta), cos(theta)]])
    return np.dot(vec,rot)    

def plot(v_g, v_b, x_range=None, y_range=None, axes_name=False, grid = True):
    show_dot_product_value(v_g, v_b)
    show_vectors(v_g, v_b,x_range, y_range, axes_name, grid)
    show_dot_product_calculations(v_g, v_b)

def draw_two_vectors(v_g, v_b, x_range=None, y_range=None, axes_name=False, grid = True, coordinates = True,shift = True):
    show_dot_product_value(v_g, v_b)
    show_vectors(v_g, v_b,x_range, y_range, axes_name, grid, coordinates,shift)
    show_dot_product_calculations(v_g, v_b)    
    
#=======================================
    
def draw_2d_vect_as_samples(v,show_dim=False):
    plt.rcParams.update({'font.size': 25})
    
    x = [1,2]
    y = v
    
    fig, ax = plt.subplots(figsize=(2, 3))
    
    ax.vlines(x, 0, y)
    ax.scatter(x, y, color='red', s=200)
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    ax.spines['bottom'].set_position('zero')
    
    ax.set_yticks([])
    ax.set_yticklabels([])
    
#    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    
    ax.set_xticks([1,2,3])
    ax.set_xticklabels(['x','y'] if show_dim else [])
    
    plt.xlim(0,3)
    plt.ylim(-1.2,1.2)
    
    #plt.grid()    
    plt.show()    
    
def draw_3d_vect_as_samples(v,show_dim=False, color='black'):
    plt.rcParams.update({'font.size': 25})
    
    x = [1,2,3]
    y = v
    
    fig, ax = plt.subplots(figsize=(2, 2))
    
    ax.vlines(x, 0, y)
    ax.scatter(x, y, color=color, s=200)
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    ax.spines['bottom'].set_position('zero')
    
    ax.set_yticks([])
    ax.set_yticklabels([])
    
#   ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    
    ax.set_xticks([1,2,3])
    ax.set_xticklabels(['x','y','z'] if show_dim else [])
    
    plt.xlim(0,4)
    plt.ylim(0,1.2)
    
    #plt.grid()    
    plt.show()  