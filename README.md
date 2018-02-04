# Computer Vision Workshop

# Step 1 
Download and Install the [docker](https://www.docker.com) or if you have a gpu the nvidia-docker client.

# Step 2 
Clone or download the Computer Vision Workshop repo

# Step 3
Build the workshop docker image using the following command for either cpu or gpu.

## CPU
```
docker build -f Dockerfile-py3-cpu . -t cv
```
## GPU
```
nvidia-docker build -f Dockerfile-py3-gpu .
```

# Step 4
Run the image you built using the following command for either cpu or gpu to start the notebook server.

## CPU
```
docker run -it -p 8888:8888 --expose=8888 cv
```

## GPU
```
nvidia-docker docker run -it -p 8888:8888 --expose=8888 cv
```

# Step 5 
Copy and store the notebook token key that is displayed after the notebook server is running

# Step 6
Navigate to http://localhost:8888/tree and enter the token you copies

# Step 7 
Click on the "Computer Vision Workshop Intro" notebook and confirm that everthing loads as expected