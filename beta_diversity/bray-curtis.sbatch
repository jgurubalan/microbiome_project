#!/bin/bash --login
#SBATCH -p himem              # Request high-memory partition
#SBATCH -n 2                  # Number of cores (adjust as needed)
#SBATCH --mem=64G             # Total memory (try 64G to start, increase if still OOM)
#SBATCH -t 1-0                # Wallclock time: 1 day
#SBATCH --job-name=braycurtis
#SBATCH --output=/mnt/iusers01/fatpou01/bmh01/msc-bioinf-2024-2025/h44063jg/microbiome_project/beta_diversity/braycurtis_species_%j.log
#SBATCH --error=/mnt/iusers01/fatpou01/bmh01/msc-bioinf-2024-2025/h44063jg/microbiome_project/beta_diversity/braycurtis_species_%j.err
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=jayadevan.gurubalan@postgrad.manchester.ac.uk

# Ensure job runs from where sbatch was called
cd $SLURM_SUBMIT_DIR

# Load environment
module purge
module load apps/binapps/anaconda3/2024.10
conda activate braycurtis-env

# Run your Python script
python bray-curtis-betadiversity.py 
