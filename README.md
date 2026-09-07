# softseclab-0
a try one for softsec lab zero 

docker compose up --build   # build + start
docker compose up -d        # start in background
docker compose up           # start the container 
docker compose ps           # check status
docker compose down         # stop/remove container
docker images               # check what images u have active

Use the compose file to build the image. Can also be built using the docker build -t NAME . Then it creates an image. But the compose file just builds it for u.

If something from the code changes we have to rebuild it, otherwise if its only the same its fine with just compose up ???

