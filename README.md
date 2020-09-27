# Python App deployment
**_This stack runs three containers_**

1. Python container
2. Redis in memory database (persistence on)
3. Nginx reverse proxy

## How to run the python environment localy
### Requirements
git, docker, docker-compose and curl command line or postman
### Clone Repository
```bash
git clone git@github.com:sys0dm1n/docker-python-stack.git
cd docker-python-stack
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

### Test it if it works!
Open this URL in your browser [http://localhost:8080](http://localhost:8080)
Make sure to update the port if you changed it in the docker-compose.yml

If it is working you should see the below message in your browser:
> Hello, unknown stranger!

Now let's test Redis, use the below command line in your terminal to insert a name/user:

```bash
curl -X POST -H "Content-Type: application/json" -d "{\"name\": \"Alain\"}" http://localhost:8080
```

Now refresh your browser and you should see the below message:
> Hello, Alain!

### Room for improvement
If you happen to find something not to your liking, you are welcome to send a PR.
