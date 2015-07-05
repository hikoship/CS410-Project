%M = load('postdata.txt')
%data = M'
%save sample_file_plus5.txt data -ascii
tic;
data = load('data.txt');
%load hald;
disp('load finished');
toc;

tic;
[coeff, score, latent] = pca(data,'NumComponents',1);
toc;
tic;
idx = kmeans(score,3);
toc;
tic;
[coeff, score, latent] = pca(data,'NumComponents',2);
toc;
tic;
idx = kmeans(score,3);
toc;
tic;
[coeff, score, latent] = pca(data,'NumComponents',3);
toc;
tic;
idx = kmeans(score,3);
toc;
tic;
[coeff, score, latent] = pca(data,'NumComponents',6);
toc;
tic;
idx = kmeans(score,3);
toc;
tic;
[coeff, score, latent] = pca(data,'NumComponents',9);
toc;
tic;
idx = kmeans(score,3);
toc;
tic;
[coeff, score, latent] = pca(data,'NumComponents',15);
toc;
tic;
idx = kmeans(score,3);
toc;
tic;
[coeff, score, latent] = pca(data,'NumComponents',24);
toc;
tic;
idx = kmeans(score,3);
toc;
tic;
[coeff, score, latent] = pca(data,'NumComponents',40);
toc;
tic;
idx = kmeans(score,3);
toc;
tic;
[coeff, score, latent] = pca(data,'NumComponents',67);
toc;
tic;
idx = kmeans(score,3);
toc;
tic;
[coeff, score, latent] = pca(data,'NumComponents',113);
toc;
tic;
idx = kmeans(score,3);
toc;
tic;
[coeff, score, latent] = pca(data,'NumComponents',139);
toc;
tic;
idx = kmeans(score,3);
toc;
tic;
[coeff, score, latent] = pca(data,'NumComponents',154);
toc;
tic;
idx = kmeans(score,3);
toc;
tic;
[coeff, score, latent] = pca(data,'NumComponents',171);
toc;
tic;
idx = kmeans(score,3);
toc;
tic;
[coeff, score, latent] = pca(data,'NumComponents',191);
toc;
tic;
idx = kmeans(score,3);
toc;


%save score.txt score -ascii
%save latent.txt latent -ascii
%save ratio.txt ratio -ascii