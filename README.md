# Computer Vision Workshop

# Set up docker vm or clone locally (TBI)


# SSH to VM exposeing the prot

Open bash and ssh -L 8080:localhost:8888 username@server_address

# Clone Repo and run the docker images
## CPU
```
docker build -f Dockerfile-py3-cpu . -t cv
docker run -it -p 8888:8888 --expose=8888 cv
```

## GPU
```
nvidia-docker build -f Dockerfile-py3-gpu .
nvidia-docker docker run -it -p 8888:8888 --expose=8888 cv
```

Copy the notebook token key and store it Navigate to http://localhost:8080/ and enter the token