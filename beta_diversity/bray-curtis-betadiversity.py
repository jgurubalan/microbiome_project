#!/usr/bin/env python3

import numpy as np
from scipy.spatial.distance import pdist, squareform

# Load your data
data_matrix = np.load("/mnt/iusers01/fatpou01/bmh01/msc-bioinf-2024-2025/h44063jg/microbiome_project/beta_diversity/species_data_pivot.npy")  # Place your data_matrix_bdiversity.npy in the same folder

# Calculate Bray-Curtis distance (condensed 1D form)
braycurtis_dist = pdist(data_matrix, metric='braycurtis')

# Convert to square 2D matrix
braycurtis_matrix = squareform(braycurtis_dist)

# Save both outputs
#np.save("/mnt/iusers01/fatpou01/bmh01/msc-bioinf-2024-2025/h44063jg/betadiversity_analysis/braycurtis_species_filtered.npy", braycurtis_dist)     # 1D condensed vector
np.save("/mnt/iusers01/fatpou01/bmh01/msc-bioinf-2024-2025/h44063jg/microbiome_project/beta_diversity/bc_distance_matrix_species.npy", braycurtis_matrix)      # 2D distance matrix

#print("Bray-Curtis distance condensed vector saved as 'braycurtis_condensed.npy'")
print("Bray-Curtis distance matrix (species)'")
