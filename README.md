# Loadsmart Weather Challenge

# 1. Set your environment
### Environment Variables
```bash
export FLASK_APP=api
export FLASK_ENV=development
export DATABASE_URL=sqlite:///example.sqlite
export GEOCODE_API_KEY=your-google-api-key
export WEATHER_API_KEY=your-weather-api-key
```

### Activate Virtual Env
```bash
. venv/bin/activate
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
npm run serve
```

open: http://localhost:8080/