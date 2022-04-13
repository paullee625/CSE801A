def plot_dendogram(model, **kwargs):
    from scipy.cluster.hierarchy import dendrogram
    import numpy as np
    # Create linkage matrix and then plot the dendrogram

    # create the counts of samples under each node
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack([model.children_, model.distances_,
                                      counts]).astype(float)

    # Plot the corresponding dendrogram
    dendrogram(linkage_matrix, **kwargs)



def draw_basemap():
    from mpl_toolkits.basemap import Basemap
    """
    This method will create a new basemap and draw it
    on the current figure.
    """
    # Create our basemap
    us_map = Basemap(width=5000*10**3,height=3500*10**3,projection='lcc',
                resolution='l',lat_1=45.,lat_2=55,lat_0=38,lon_0=-97)

    # Draw a shaded-relief map from our basemap
    us_map.shadedrelief()

    # Draw the different boundary lines
    us_map.drawstates(linewidth=1.5)
    us_map.drawcountries(linewidth=5)
    us_map.drawcoastlines(linewidth=1)

    # Return our map object
    return us_map


