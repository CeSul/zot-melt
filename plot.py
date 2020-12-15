#!/usr/local/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import time, sys, getopt

def color_function(x,y,n,t):
    # From mathematica:
    # colorFunction[x_, y_, t_] := Round[Mod[(x /10)^2 y/10 + ((y)/10)^2 x/10 + t, 1], 3/256]
    value = (x/10)**2*(y/10) + (y/10)**2*(x/10)+t/n
    value = value %1 # Keep number between 0 and 1
    return value
def write_plot(X,Y,output,nFrames,i):
    fit,ax=plt.subplots()
    Z = color_function(X,Y,nFrames,i)
    plt.imshow(Z,cmap="Pastel2")
    ax.axis('off')
    t=time.time()
    plotname=("%s%05d.png" %(output,i))
    plt.savefig(plotname,dpi=300)
    elapsed = time.time()-t
    print("%s saved in %f s" %(plotname,elapsed))
    plt.close()
    return elapsed

def main(argv):

    nFrames=15
    size=100
    output="plot"

    try:
        opts,args=getopt.getopt(argv,"hn:s:0:",["nFrames=","size=", "output="])
    except getopt.GetoptError:
        print("plot.py -n <number_of_frames> -s <array_size> -o <outfile>")
        sys.exit(2)
    for opt,arg in opts:
        if opt=='-h':
            print("plot.py -n <number_of_frames> -s <array_size> -o <outfile>")
            sys.exit()
        elif opt in ("-n", "--nFrames"):
            print("Setting nFrames")
            nFrames = int(float(arg))
        elif opt in ("-s", "--size"):
            print("Setting size")
            size = int(float(arg))
        elif opt in ("-o", "--output"):
            print("Setting output")
            output = arg
            
# Summarize params
    print('nFrames=%s' %nFrames)
    print('size= %s' %size)
    print('output_template=%s%%06d.png ' %output)

    x = np.arange(size,2*size,1)
    y = np.arange(1/2*size,3.5/2*size,1)
    X,Y = np.meshgrid(x,y)


    stats=np.zeros(nFrames)

    for i in range(0,nFrames):
        elapsed=write_plot(X,Y,output,nFrames,i)
        stats[i]=elapsed
    print("------ Summary statistics ------")
    print("   Min write time     = %1.3f s" %stats.min())
    print("   Max write time     = %1.3f s" %stats.max())
    print("   Average write time = %1.3f s" %stats.mean())
    print("   Std Dev            = %1.3f s" %stats.std())
main(sys.argv[1:])
