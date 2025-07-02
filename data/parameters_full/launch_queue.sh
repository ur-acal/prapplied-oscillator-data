#!/bin/bash
#SBATCH --job-name QUEUE_sim000_h6_osc_anneal_formulation_binarization_comparison
#SBATCH --output=/scratch/mburns13/data/ISING_RESULTS/oscsim/sim000_h6_osc_anneal_formulation_binarization_comparison/parameters/queue.run
#SBATCH --error=/scratch/mburns13/data/ISING_RESULTS/oscsim/sim000_h6_osc_anneal_formulation_binarization_comparison/err/queue.err
#SBATCH -p ising
#SBATCH --mem=1G
#SBATCH --ntasks=1
#SBATCH --time=5-00:00:00

python3 /gpfs/fs2/scratch/mhuang_lab/mburns13/oscillators/oscillators/oscsim/queue_host.py sim000_h6_osc_anneal_formulation_binarization_comparison
