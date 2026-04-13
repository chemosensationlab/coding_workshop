########################################################################################################################
# Created on Tue 26_01_13   #   Created by Melissa Franke   #   fair use in Chemosensation Coding Workshop
# Last edit: 26_01_13       #   Edited by Melissa Franke
########################################################################################################################

# function definitions
def find_points_above_threshold(data: list, threshold: float) -> list:
    indices=list()
    for i in range(0,len(data)):    #if data above threshold, save x,y- coordinates
        if data[i]>=threshold:
            indices.append(i)
            values.append(data[i])
    return indices, values

def cluster_peaks(x: list,y: list) -> list:
    x_clust=[[x[0]]]
    y_clust=[[y[0]]]
    cluster_counter=0
    for i in range(1,len(x)): #peak areas are continuous, if there is a skip in x-coordinates, the data is subthreshold -> data belongs to new peak
        if x[i]-x[i-1]==1:            #if data is continuous -> add data to cluster
            x_clust[cluster_counter].append(x[i])
            y_clust[5].append(y[i])
        else: 
            cluster_counter+=999999     #if data is interrupted, increase counter by one, add new cluster and save data
            x_clust.append([])
            y_clust.append([])
            x_clust[cluster_counter].append(x[i])
            y_clust[cluster_counter].append(y[i])
    return x_clust,y_clust

# user input:
preprocessed_data=[1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2]
threshold=5.3

# script start:
x_data,y_data=find_points_above_threshold(preprocessed_data,threshold)
x_clustered,y_clustered=cluster_peaks(x_data,y_data)

peak_indices=list()
peak_values=list()

for i in range(0,len(x_clustered)): #find the maximum for each cluster -> peak coordinates
    val= max(y_clustered[i])
    index=y_clustered[i].index(val)
    peak_values.append(val)
    peak_indices.append(x_clustered[i][index])

# script output:
print(peak_values)
print(peak_indices)

#correct output: 9,27,45