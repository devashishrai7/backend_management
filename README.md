PROJECT NAME: backend_management

A modular backend application with authentication, CRUD APIs, database integration, Docker support, and minimal error handling.


PROJECT STRUCTURE: -

backend_management/
│
├── app/
|   |──core/
|   │   ├── dependencies
|   │   ├── error_handler
│   |   └── security
│   │
|   |──modules/
|   │   ├── analytics/
|   |   |   |── analytics_controller
|   |   |   |── analytics_model
|   |   |   |── analytics_routes
│   |   │   └── analytics.schema
│   |   │
|   │   ├── auth/
|   │   │   ├── auth.controller
|   │   │   |── auth.model
│   |   │   ├── auth.routes
│   |   │   └── auth.schema
│   │   |
│   |   ├── content/
|   |   |   |── content_controller
|   |   |   |── content_model
|   |   |   |── content_routes
│   |   │   └── content.schema
|   │   │
│   |   |── dashboard/
|   |   |   |── dashboard_controller
|   |   |   |── dashboard_model
|   |   |   |── dashboard_routes
│   |   │   └── dashboard.schema
│   │   |
|   │   ├── leads/
|   |   |   |── leads_controller
|   |   |   |── leads_model
|   |   |   |── leads_routes
|   │   │   └── leads.schema
│   |   │
│   |   ├── sales/
|   |   |   |── sales_controller
|   |   |   |── sales_model
|   |   |   |── sales_routes
│   |   │   └── sales.schema
|   │   │
│   |   └── settings/
|   |       |── settings_controller
|   |       |── settings_model
|   |       |── settings_routes
│   |       └── settings.schema
│   │
│   ├── .env
│   │
│   ├── config
│   │
│   ├── database
│   │
│   └── main (main entry file)
│
├── docker-compose.yml
├── Dockerfile
├── postman_collection.json
├── README.md
└── requirements.txt


FEATURES: -

- Modular folder structure
- Authentication (Signup / Login)
- CRUD APIs for all modules
- Database connection & models
- Centralized routing
- Minimal error-handling middleware
- Docker support


TECH STACK:-

Backend        : Python (FastAPI)
Database       : MySQL
Authentication : JWT
Container      : Docker
API Testing    : Swagger UI and Postman


INSTALLATION:-

1. Clone Repository

git clone https://github.com/devashishrai7/backend_management.git
cd backend_management


2. Install Dependencies

python -m venv venv
source venv/bin/activate   (Linux/Mac)
venv\Scripts\activate      (Windows)
pip install -r requirements.txt


ENVIRONMENT VARIABLES: -

Create a .env file using .env

JWT_SECRET_KEY="your_jwt_secret"
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=backend_management


RUN APPLICATION:-
uvicorn app.main:app --reload


DOCKER RUN:-

docker build -t backend_management .
docker run -p 3000:3000 backend_management

Or using Docker Compose:
docker-compose up --build


API ROUTES SUMMARY:-

Authentication
POST /auth/signup   - User registration
POST /auth/login    - User login

Dashboard
POST /dashboard     - Create dashboard
GET /dashboard      - Fetch dashboard data

Analytics
POST /analytics     - Create Analytics
GET /analytics      - Fetch analytics data

Leads
POST   /leads/create-lead       - Create lead
GET    /leads                   - List leads

Sales
POST /sales         - Generate Sales
GET /sales          - Fetch sales

Contens
POST /contents      - Create contents
GET /contents       - Fetch contents

Setting
PUT /settings      - Update settings
GET /settigs        - Fetch settings


ERROR HANDLING:-

Centralized error-handling middleware handles:
401 - Unauthorized
403 - Forbidden
404 - Not Found
422 - Validation Error
500 - Internal Server Error


POSTMAN COLLECTION: -

File: postman_collection.json
Import into Postman to test APIs.


AUTHOR: -

Devashish Rajbhar
Backend Developer (Python / Laravel)
devashish0797@gmail.com