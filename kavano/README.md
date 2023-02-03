# DevOps Enginer task
- [X] Containerize the app located at this repo.
   - https://github.com/digitalocean/sample-python/tree/main
- [X] Manage your container via docker-compose.
- [X] Add an Nginx to your docker-compose.
- [X] Your Deployment must have the following characteristics:
    - Continue running after any restart.
    - Only your Nginx can be accessed from outside and your python app is behind Nginx.
- [X] Your app is not supposed to be viewable by outside people all the time. The only time they are allowed to see it is between 8:00 to 16:00. But the insiders are allowed to see it always. Block connections from outside to our app. Only accept connections from “192.168.10.0/24” which is our corporation’s LAN IP address range.

# Execute
requirement:
- docker 
- docekr-compose
```bash
git clone https://github.com/FaroukFallahi/K-devops-eng-task.git
cd K-devops-eng-task
docker-compose up -d
```
it's accessable on  `http://localhost:8000`
## Docker-compose
it's containts two containers:
- sample-python
    - a sample script that return the url of request from digital ocean mentioned above.
    - serve the service on 8080 port of brige network of docker-compose

- nginx
    - version 1.22
    - that exposed the port 80 on 8000 on host
    - mounted config file of nginx

## nginx config
-  allow only in two situatuion to acces the service:
   - ip is in range `192.168.10.0/24`
   - the local time (server) is in period `08-16` o'clock.
### details
- used map for scrape the clock with regex.
- used geo for whitelist allowed ip out of period time.
- proxy passed the request to sample-python-server