# Loadsmart Weather Challenge
# Docker
Before start building containers you need to set your API keys to environment variables. It is 
important, without valid API keys the application can not connect with the services. 

To do that, you need to update the `docker-compose.yml`, change the lines that represents this
environment variables:
```yml
environment:
  - DATABASE_URL=sqlite:///example.sqlite
  - GEOCODE_API_KEY=add-your-geo-api-key
  - WEATHER_API_KEY=add-your-weather-api-key
```

With your environment variables set, run the following command.
```bash
docker-compose up
```
When the process is finished, and running try to access this URL http://localhost:8080/

# 1. Set your local development environment
### Environment Variables
Warning: Remember to hydrate the environment variables with your API Keys. 
```bash
export FLASK_APP=api
export FLASK_ENV=development
export DATABASE_URL=sqlite:///example.sqlite
export GEOCODE_API_KEY=your-google-api-key
export WEATHER_API_KEY=your-weather-api-key
```

### Activate Virtual Env
Python 3 version is required.

```bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

# 2. Execute Flask Server
Open a new terminal to this server and keep it opened
```bash
flask run
```

# 3. Execute Vue.js server
Open a new terminal to this server and keep it opened
```bash
cd web
npm install
npm run serve
```

open: http://localhost:8080/
