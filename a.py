a = [1,2,3,6,9,15,24,40,67,113,139,154,171,191]
for i in a:
    print "tic;\n[coeff, score, latent] = pca(data,'NumComponents',%d);\ntoc;\ntic;\nidx = kmeans(score,3);\ntoc;" % i


