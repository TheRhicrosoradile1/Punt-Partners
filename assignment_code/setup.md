## BASIC SETUP WITHOUT DOCKER
- create a virtual env  (python3.8 or up)
- install all dependencies mentioned in the requirements file


## TO CHECK THE DOCS 
- run the app locally using 'uvicorn main:app --reload' from the 'assignment_code' repository
- run http://127.0.0.1:8000/docs


## TO BUILD DOCKER IMAGE 
- run `docker build -t <iamge tag> .`  in the same directory as Dockerfile
- run `docker run <image tag>`

## CURLS TO CHECK CODE WORKING
### To add a coupon_code "1234"
curl -X 'POST' \
  'http://127.0.0.1:8000/api/coupon-codes/v1/add_coupon_repeat_count/?coupon_code=1234' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "user_total_repeat_count": 3,
  "user_per_day_repeat_count": 2,
  "user_per_week_repeat_count": 1,
  "global_total_repeat_count": 1
}'

### To check duplicate entry
curl -X 'POST' \
  'http://127.0.0.1:8000/api/coupon-codes/v1/add_coupon_repeat_count/?coupon_code=1234' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "user_total_repeat_count": 3,
  "user_per_day_repeat_count": 2,
  "user_per_week_repeat_count": 1,
  "global_total_repeat_count": 1
}'

### To apply a coupon code
curl -X 'POST' \
  'http://127.0.0.1:8000/api/coupon-codes/v1/add_coupon_repeat_count/?coupon_code=1234' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "user_total_repeat_count": 3,
  "user_per_day_repeat_count": 2,
  "user_per_week_repeat_count": 1,
  "global_total_repeat_count": 1
}'

### To verify a coupon code exist
curl -X 'GET' \
  'http://127.0.0.1:8000/api/coupon-codes/v1/verify_coupon/user/1/coupon-code/123' \
  -H 'accept: application/json'

### Note : the code uses fast api for faster code execution and better async support 
- we are performing async execution of request so all api are non-blocking
- In doing so there may be the possiblity of race condition where bith read and write are performed simultaneously leading to bad result which could be improved by using lock whenever writeing to db 
- additional features to be added dockerizing the app, adding database engine, formalizing request and response in a fixed manner 


### dir structure
assignment_code/
|-- app/
|   |--src/
|   |    |--data/coupom_db.py
|   |    |--models.py     # contains all database types
|   |    |--requests.py   # contains all requests types
|   |    |--responses.py  # contains all responses types
|   |    |--repository.py  # contains database interaction logic
|   |    |--service.py # contains the core logic
│   |-- __init__.py
│   |-- main.py
│   |-- routes.py       # contains all routes code
|-- tests/
│   |-- __init__.py
│   |-- unit_tests.py
|-- Dockerfile     # main dockerfile
├-- .dockerignore
|-- requirements.txt  
|--readme.md
|--setup.md