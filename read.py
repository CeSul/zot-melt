import numpy as np
import time, sys, getopt, re, os
import matplotlib.pyplot as plt

def read_image(image):
    t=time.time()
    plt.imread(image)
    elapsed=time.time()-t
    print("Read %s in %f s" %(image, elapsed))
    return elapsed

def main(argv):

    files = os.listdir()
    default_re=re.compile(".*.png")
    imageList=list(filter(default_re.match,files))


    try:
        opts,args=getopt.getopt(argv,"hi:",["images="])
    except getopt.GetoptError:
        print("read.py -i <list_of_images>")
        sys.exit(2)
    print(opts)
    for opt,arg in opts:
        if opt=='-h':
            print("read.py -i <list_of_images>")
            sys.exit()
        elif opt in ("-i", "--images"):
            r = re.compile(arg)
            imageList = list(filter(r.match,files))
            print("Setting image list to ")
            print(imageList)
    stats=np.zeros(len(imageList))
    counter=0
    for image in imageList:
        elapsed=read_image(image)
        stats[counter] = elapsed
        counter = counter +1

    print("------ Summary statistics ------")
    print("   Min write time     = %1.3f s" %stats.min())
    print("   Max write time     = %1.3f s" %stats.max())
    print("   Average write time = %1.3f s" %stats.mean())
    print("   Std Dev            = %1.3f s" %stats.std())
    print("   Number of reads   = %06d" %counter)

main(sys.argv[1:])
