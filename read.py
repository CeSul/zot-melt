import numpy as np
import time, sys, getopt, re, os
import matplotlib.pyplot as plt


def main(argv):

    files = os.listdir('output')
    default_re=re.compile(".*.npy")

    read_dir='output'
    fileList = list(filter(default_re.match,files))
    time_data=np.zeros(len(fileList))
    size=np.zeros(len(fileList))
    counter=0
    for file in fileList:
        filename='output/'+file
        t=time.perf_counter()
        data=np.load(filename)
        elapsed = time.perf_counter()-t

        time_data[counter] = elapsed
        size[counter] = os.path.getsize(filename)
        counter = counter +1

    stats=size/time_data /1024**2

    print("------ Summary statistics ------")
    print("   Average read speed = %1.3f MB/s" %stats.mean())
    print("   Std Dev             = %1.3f MB/s" %stats.std())
    print("   Min read speed     = %1.3f MB/s" %stats.min())
    print("   Max read speed     = %1.3f MB/s" %stats.max())
    print("   Number of reads     = %06d" %counter)

main(sys.argv[1:])
