#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=2GB
#SBATCH --time=00:30:00
#SBATCH --account=hpcroot

module purge
module load usc
module load python/3.7.6
module load ffmpeg

python3 write.py -n 300
python3 read.py
ffmpeg -r 25 -i plot%05d.png  -vb 20M outfile.mp4

rm *.png
