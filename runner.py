import sys
import time
import operator
import numpy as np

from graphSimilarity.utils import *
from graphSimilarity.kernel_methods import *
from graphSimilarity.distance_functions import *
from graphSimilarity.graph import Graph
from graphSimilarity.graph_generator import generate_graphs_file
from graphSimilarity.graph_generator_2 import generate_graphs_file_2
from graphSimilarity.kernel_kmeans import kernel_kmeans, get_kernel_wcss, get_kernel_matrix
from graphSimilarity.sd_kmeans import sd_kmeans, get_sd_wcss, get_sd_labels, get_distance_matrix
from graphSimilarity.kmeans_init import get_random_centroids, kmeans_pp

from sklearn.cluster import SpectralClustering
from sklearn.metrics import silhouette_samples, silhouette_score


#graph = Graph(2, [(0, 1)])
#print(graph.get_num_vertices())
#graph.compute_adjacency_matrix()
#print(graph.get_adjacency_matrix())

#graphs = load_data(sys.argv[1])
#for graph in graphs:
#    graph.compute_adjacency_matrix()
#    print graph.get_adjacency_matrix()
#    print 

#---------------------------------------------------------------------------------------------

graphs = load_data(sys.argv[1])

for graph in graphs:
    graph.compute_adjacency_matrix()
    graph.compute_diagonal_matrix()

#---------------------------------------------------------------------------------------------


#print graph_edit_distance(graphs[0], graphs[1])

#print rbf_kernel(graphs[0], graphs[1], graph_edit_distance, 0.1)

#---------------------------------------------------------------------------------------------

# res = []
# for seed in range(1000):
#     res.append(kernel_kmeans(2, 50, seed, graphs, graph_edit_distance, rbf_kernel, "random"))

# correct = 0
# wrong = 0

# for items in res:
#     if all(x == items[0] for x in items[:10]) and all(x == items[10] for x in items[10:]) and  not all(x == items[0] for x in items):
#         #print "Correct: " + str(items)
#         correct +=1
#     else:
#         #print "Wrong: " + str(items)
#         wrong +=1

# print "Correct: " + str(correct)
# print "Wrong: " + str(wrong)

#---------------------------------------------------------------------------------------------

# for seed in range(200):
#    print kernel_kmeans(2, 50, seed, graphs, graph_edit_distance, rbf_kernel, "random")

#---------------------------------------------------------------------------------------------

# for seed in range(200):
#    print sd_kmeans(2, 50, seed, graphs, delta_con, "random")

#---------------------------------------------------------------------------------------------

# labels = kernel_kmeans(2, 50, 0, graphs, graph_edit_distance, rbf_kernel)
# print labels

# kernel_wcss = get_kernel_wcss(2, graphs, labels, graph_edit_distance, rbf_kernel)
# print kernel_wcss


# centroids = sd_kmeans(2, 50, 0, graphs, graph_edit_distance)
# print centroids

# labels = get_sd_labels(centroids, graphs, graph_edit_distance)
# print labels

# sd_wcss = get_sd_wcss(centroids, graphs, graph_edit_distance)
# print sd_wcss

#---------------------------------------------------------------------------------------------


# labels = kernel_kmeans(2, 50, 0, graphs, graph_edit_distance, rbf_kernel, "proxy")
# print labels

#---------------------------------------------------------------------------------------------

# res = []
# for seed in range(1000):
#     res.append(kernel_kmeans(2, 50, seed, graphs, graph_edit_distance, rbf_kernel, "proxy"))

# correct = 0
# wrong = 0

# for items in res:
#     if all(x == items[0] for x in items[:10]) and all(x == items[10] for x in items[10:]) and  not all(x == items[0] for x in items):
#         correct +=1
#     else:
#         wrong +=1

# print "Correct: " + str(correct)
# print "Wrong: " + str(wrong)


#---------------------------------------------------------------------------------------------

# dist = delta_con(graphs[16], graphs[18])
# print dist

#---------------------------------------------------------------------------------------------


# start = time.time()

# for seed in range(200):
#     sd_kmeans(2, 50, seed, graphs, graph_edit_distance)

# end = time.time()
# print end - start


# start = time.time()

# for seed in range(200):
#     sd_kmeans(2, 50, seed, graphs, delta_con)

# end = time.time()
# print end - start


# fabp_graphs = [fabp(g) for g in graphs]

# start = time.time()

# for seed in range(200):
#     sd_kmeans(2, 50, seed, fabp_graphs, root_ed)

# end = time.time()
# print end - start


#---------------------------------------------------------------------------------------------

# start = time.time()

# for seed in range(200):
#     kernel_kmeans(2, 50, seed, graphs, graph_edit_distance, rbf_kernel)

# end = time.time()
# print end - start


# start = time.time()

# for seed in range(200):
#     kernel_kmeans(2, 50, seed, graphs, delta_con, rbf_kernel)

# end = time.time()
# print end - start


# fabp_graphs = [fabp(g) for g in graphs]

# start = time.time()

# for seed in range(200):
#     kernel_kmeans(2, 50, seed, fabp_graphs, root_ed, rbf_kernel)

# end = time.time()
# print end - start

#---------------------------------------------------------------------------------------------

# kernel_matrix = get_kernel_matrix(graphs, graph_edit_distance, rbf_kernel)

# spectral_kmeans = SpectralClustering(n_clusters=2, random_state=0, n_init=1, affinity='precomputed').fit(kernel_matrix)

# print spectral_kmeans.labels_

#---------------------------------------------------------------------------------------------

# kernel_matrix = get_kernel_matrix(graphs, graph_edit_distance, rbf_kernel)

# res = []
# for seed in range(1000):
#     spectral_kmeans = SpectralClustering(n_clusters=2, random_state=seed, n_init=1, affinity='precomputed').fit(kernel_matrix)
#     res.append(spectral_kmeans.labels_)

# correct = 0
# wrong = 0

# for items in res:
#     if all(x == items[0] for x in items[:10]) and all(x == items[10] for x in items[10:]) and  not all(x == items[0] for x in items):
#         correct +=1
#     else:
#         wrong +=1

# print "Correct: " + str(correct)
# print "Wrong: " + str(wrong)

#---------------------------------------------------------------------------------------------

# start = time.time()

# kernel_matrix = get_kernel_matrix(graphs, graph_edit_distance, rbf_kernel)

# for seed in range(200):
#     SpectralClustering(n_clusters=2, random_state=seed, n_init=1, affinity='precomputed').fit(kernel_matrix)

# end = time.time()
# print end - start

#---------------------------------------------------------------------------------------------

# create_basic_edgelist_files(graphs, "/home/aquila/CS/L5P/FC/formatConversion/graphDir", common_node = True)

#---------------------------------------------------------------------------------------------

# matrices = load_matrix_data("/home/aquila/CS/L5P/FC/formatConversion/outDir/data.txt", 11)
# print matrix_ed(matrices[16], matrices[15])

#---------------------------------------------------------------------------------------------

# matrices = load_matrix_data("/home/aquila/CS/L5P/formatConversion/outDir/data.txt", 11)

# labels = kernel_kmeans(2, 50, 0, matrices, matrix_ed, rbf_kernel)
# print labels

# centroids = sd_kmeans(2, 50, 0, matrices, matrix_ed)
# print centroids

# labels = get_sd_labels(centroids, matrices, matrix_ed)
# print labels

#---------------------------------------------------------------------------------------------

# matrices = load_matrix_data("/home/aquila/CS/L5P/FC/formatConversion/outDir/data.txt", 11)

# res = []
# for seed in range(200):
#     res.append(kernel_kmeans(2, 50, seed, matrices, root_ed, rbf_kernel))

# correct = 0
# wrong = 0

# for items in res:
#     if all(x == items[0] for x in items[:10]) and all(x == items[10] for x in items[10:]) and  not all(x == items[0] for x in items):
#         correct +=1
#     else:
#         wrong +=1

# print "Correct: " + str(correct)
# print "Wrong: " + str(wrong)

#---------------------------------------------------------------------------------------------

# create_basic_adjacency_files(graphs, "/home/aquila/CS/L5P/FC/formatConversion2/graphDir")

#---------------------------------------------------------------------------------------------

# matrices = load_deep_walk_files("/home/aquila/CS/L5P/FC/formatConversion2/outDir", 10)
# print matrix_ed(matrices[1], matrices[15])

#---------------------------------------------------------------------------------------------

# matrices = load_deep_walk_files("/home/aquila/CS/L5P/FC/formatConversion2/outDir", 10)

# labels = kernel_kmeans(2, 50, 0, matrices, matrix_ed, rbf_kernel)
# print labels

# centroids = sd_kmeans(2, 50, 0, matrices, matrix_ed)
# print centroids

# labels = get_sd_labels(centroids, matrices, matrix_ed)
# print labels

#---------------------------------------------------------------------------------------------

# matrices = load_deep_walk_files("/home/aquila/CS/L5P/FC/formatConversion2/outDir", 10)

# res = []
# for seed in range(200):
#     res.append(kernel_kmeans(2, 50, seed, matrices, matrix_ed, rbf_kernel))

# correct = 0
# wrong = 0

# for items in res:
#     if all(x == items[0] for x in items[:10]) and all(x == items[10] for x in items[10:]) and  not all(x == items[0] for x in items):
#         correct +=1
#     else:
#         wrong +=1

# print "Correct: " + str(correct)
# print "Wrong: " + str(wrong)

#---------------------------------------------------------------------------------------------

# labels = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1]

# dist_matrix = get_distance_matrix(graphs, graph_edit_distance)
# print silhouette_score(dist_matrix, labels, metric="precomputed")

# matrices = load_matrix_data("/home/aquila/CS/L5P/FC/formatConversion/outDir/data.txt", 11)
# matrices = load_deep_walk_files("/home/aquila/CS/L5P/FC/formatConversion2/outDir", 10)

# dist_matrix = get_distance_matrix(matrices, matrix_ed)
# print silhouette_score(dist_matrix, labels, metric="precomputed")

#---------------------------------------------------------------------------------------------

# print sim_rank(graphs[0], 0.8, 10)
# print sim_rank_distance(graphs[0], graphs[1])

#---------------------------------------------------------------------------------------------

# generate_graphs_file("test.txt", 100, 20, dense_regions = [[0,5]], sparse_regions = [[5,20]], clique_range = [19, 20])
# draw_all_graphs("test.txt")

#---------------------------------------------------------------------------------------------

# generate_graphs_file_2("test.txt", 4, 10, regions = [[0, 5, 0.8], [5, 10, 0.2]], region_con = 0.2)
# draw_all_graphs("test.txt")

#---------------------------------------------------------------------------------------------

# print get_random_permutations([80, 60, 40, 20, 10], 5, seed = 50)

#---------------------------------------------------------------------------------------------

# permu = get_random_permutations([80, 60, 40, 20, 10], 5, seed = 50)

# for p in range(len(permu)):
# 	perm = permu[p]
# 	perm = [pe / 100.0 for pe in perm]
# 	nwr = []
# 	for pe in perm:
# 		if pe < 0.3:
# 			nwr.append([1,11])
# 		elif pe > 0.3 and pe < 0.5:
# 			nwr.append([5,16])
# 		else:
# 			nwr.append([10, 21])

# 	generate_graphs_file_2("test" + str(p) + ".txt", 100, 50, seed = p,
# 						regions = [[0, 10, perm[0]], [10, 20, perm[1]], [20, 30, perm[2]], [30, 40, perm[3]], [40, 50, perm[4]]],
# 						region_con = 0.5, uniform_region_con = False, weighted_nodes = True, node_weight_ranges = nwr)

#---------------------------------------------------------------------------------------------

# matrices = get_rolx_matrices(graphs, rolx_path = "/home/aquila/CS/L5P/snap/examples/rolx/testrolx", num_roles = 3)

#---------------------------------------------------------------------------------------------

# matrices = get_deep_walk_matrices(graphs, representation_size = 64, number_walks = 10, walk_length = 40, undirected = True)

#---------------------------------------------------------------------------------------------

# distance_matrix = get_distance_matrix(graphs, graph_edit_distance)
# kernel_matrix = map_over_matrix_elements(distance_matrix, rbf, sigma = 0.1)

#---------------------------------------------------------------------------------------------

# times = {}
# distance_matrix = None


# start = time.time()
# distance_matrix = get_distance_matrix(graphs, graph_edit_distance)
# end = time.time()

# times["GED"] = end - start
# distance_matrix = None


# start = time.time()
# fabp_matrices = [fabp(graph) for graph in graphs]
# distance_matrix = get_distance_matrix(fabp_matrices, root_ed)
# end = time.time()

# times["DC"] = end - start
# distance_matrix = None


# start = time.time()
# sim_rank_matrices = [sim_rank(graph) for graph in graphs]
# distance_matrix = get_distance_matrix(sim_rank_matrices, flat_matrix_cd)
# end = time.time()

# times["SR"] = end - start
# distance_matrix = None


# start = time.time()
# degree_matrices = [node_degree_matrix(graph) for graph in graphs]
# distance_matrix = get_distance_matrix(degree_matrices, flat_matrix_ed)
# end = time.time()

# times["DEG"] = end - start
# distance_matrix = None


# start = time.time()
# rolx_matrices = get_rolx_matrices(graphs, rolx_path = "/home/aquila/CS/L5P/snap/examples/rolx/testrolx", num_roles = 3)
# distance_matrix = get_distance_matrix(rolx_matrices, flat_matrix_cd)
# end = time.time()

# times["RolX"] = end - start
# distance_matrix = None


# start = time.time()
# dw_matrices = get_deep_walk_matrices(graphs, representation_size = 64, number_walks = 10, walk_length = 40, undirected = True)
# distance_matrix = get_distance_matrix(dw_matrices, flat_matrix_cd)
# end = time.time()

# times["DW"] = end - start
# distance_matrix = None



# start = time.time()
# distance_matrix = get_distance_matrix(graphs, graph_edit_distance_nw)
# end = time.time()

# times["GED_NW"] = end - start
# distance_matrix = None


# start = time.time()
# norm = get_largest_node_weight(graphs)
# fabp_nw_matrices = [fabp_nw(graph, norm) for graph in graphs]
# distance_matrix = get_distance_matrix(fabp_nw_matrices, root_ed)
# end = time.time()

# times["DC_NW"] = end - start
# distance_matrix = None


# start = time.time()
# degree_matrices_nw = [node_degree_weight_matrix(graph) for graph in graphs]
# distance_matrix = get_distance_matrix(degree_matrices_nw, flat_matrix_ed)
# end = time.time()

# times["DEG_NW"] = end - start
# distance_matrix = None


# sorted_times = sorted(times.items(), key=operator.itemgetter(1))
# print "__________________________________________________________"

# for item in sorted_times:
# 	print str(item[0]) + " " + str(item[1])
