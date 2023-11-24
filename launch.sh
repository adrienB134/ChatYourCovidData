#/bin/bash
docker build . -t chatcovid
docker run -p 4000:4000 \
-e PORT=4000 \
-v "$(pwd)/app:/home/app" \
chatcovid
