#!/usr/bin/env bash

PORT=8080
echo "Port: $PORT"

# POST method predict
curl -d '{  
   "preg":1
   "plas":126
   "pres":60
   "skin":0
   "test":0
   "mass":30.1
   "pedi":0.349
   "age":23
}'\
     -H "Content-Type: application/json" \
     -X POST http://127.0.0.1:$PORT/predict
