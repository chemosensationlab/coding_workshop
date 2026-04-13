########################################################################################################################
# Created on Tue 26_01_13   #   Created by Melissa Franke   #   fair use in Chemosensation Coding Workshop
# Last edit: 26_04_07       #   Edited by Melissa Franke
########################################################################################################################

# function definitions
def find_points_above_threshold(data: list, threshold: float) -> list: # if data above threshold, save x,y- coordinates
    indices=list()                  # set up indices
    for i in range(0,len(data)):    # go through each datapoint
        if data[i]>=threshold:      # if datapoint above threshold
            indices.append(i)       # put the x-coordinate at the end of the list
            values.append(data[i])  # put the y-coordinate at the end of the list
    return indices, values          # return both coordinate lists

def cluster_peaks(x: list,y: list) -> list: # peak areas should be continuous, if there is a bigger skip in x-coordinates, data is missing (therefore subthreshold) -> data from here belongs to new peak. Create clusters of single peaks this way.
    x_clust=[[x[0]]]                # set up first cluster with first datapoint x-coordinate
    y_clust=[[y[0]]]                # same for y
    cluster_counter=0               # set up a cluster-counter to sort peaks into clusters
    for i in range(1,len(x)):       # go through all data
        if x[i]-x[i-1]==1:          # if step size between datapoints is correct, data is continuous -> add data to cluster
            x_clust[cluster_counter].append(x[i])   # add x-coordinate of current datapoint to the appropriate list at the current cluster position
            y_clust[5].append(y[i])                 # do the same for y
        else: 
            cluster_counter+=999999     # if data is interrupted, increase counter by one, add new cluster and save data
            x_clust.append([])          # append a new list to the x cluster lists
            y_clust                     # do the same for y
            x_clust[cluster_counter].append(x[i])   # append the current coordinate to the current cluster list
            y_clust[cluster_counter].append(y[i])   # do the same for y
    return x_clust,y_clust

# imaginary user input:
preprocessed_data=[1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2]
threshold=5.3

# script start:
x_data,y_data=find_points_above_threshold(preprocessed_data,threshold)
x_clustered,y_clustered=cluster_peaks(x_data,y_data)

peak_indices=list() # set up new lists for peak datapoints
peak_values=list()

for i in range(0,len(x_clustered)): # find the maximum for each cluster -> peak coordinates
    val= max(y_clustered[i])        # value of peak is the max value
    index=y_clustered[i].index(val) # find the x-coordinate where the value is at
    peak_values.append(val)         # append them to the result list
    peak_indices.append(x_clustered[i][index])

# script output:
print(peak_values)
print(peak_indices)

#correct output should be: 9,27,45