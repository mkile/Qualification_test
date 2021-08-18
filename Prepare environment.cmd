echo "Y"|docker container prune
echo "Y"|docker volume prune
rem echo "Y"|docker image prune -a
echo "Y"|docker network prune
docker pull selenoid/vnc_chrome:91.0
docker pull selenoid/vnc_firefox:90.0
docker pull selenoid/vnc_opera:76.0
docker compose up