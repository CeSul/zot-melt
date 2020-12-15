#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=2GB
#SBATCH --time=00:30:00
#SBATCH --account=<your_account>

module purge
module load usc
module load python/3.7.6

python3 plot.py
