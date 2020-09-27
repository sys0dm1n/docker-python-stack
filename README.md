# Python App deployment
**_This stack runs three containers_**

1. Python container
2. Redis in memory database (persistence on)
3. Nginx reverse proxy

## How to run the python environment localy
### Requirements
git, docker and docker-compose
### Clone Repository
```bash
git clone 
```
### Update files
Update Redis password if needed in `.env` file.

Update `docker-compose.yml` file if required (eg. nginx port mapping).

### Update your code
A sample code is in the code folder

### Build and start
```bash
docker-compose up -d
```

### Room for improvement
If you happen to find something not to your liking, you are welcome to send a PR.
