# Car Dealership Inventory System

A full-stack web application for managing a car dealership's inventory. Built with FastAPI (backend), React (frontend), and SQLite database.


 # project screenshot 
 https://drive.google.com/drive/folders/1VaYqy91t-fZWEtF2IhBUKtaWqAMUl22y
 
## Project Overview

This is a Test-Driven Development (TDD) Kata project that demonstrates best practices in full-stack development including:
- RESTful API design
- Database management with SQLAlchemy ORM
- User authentication with JWT tokens
- Comprehensive test coverage
- Modern frontend with React and Tailwind CSS
- Clean code principles and SOLID design

## User Roles

The app supports two roles: **Admin** and **User**, controlled by an is_admin flag on the account (not selectable at login, for security). Regular users can view, search, and purchase vehicles. Admins can additionally add, restock, and delete vehicles. Role is enforced on the backend via a require_admin dependency (returns 403 if bypassed), and the navbar shows an Admin/User badge to indicate the current role.

**To test as admin**: run python **seed_admin.py** in **backend/** to create 
admin email : **admin@dealership.com** / 
admin password **admin123** .
Register any other email to test as a regular user. user can not add vehicles , restock vehicles and delete vehicles

## Features

### Backend API
- **User Authentication**: Register and login with secure password hashing
- **Vehicle Management**: Create, read, update, and delete vehicles
- **Search & Filter**: Search vehicles by make, model, category, or price range
- **Inventory Operations**: Purchase vehicles (decrease inventory) and restock (increase inventory)
- **Token-based Security**: JWT authentication for protected endpoints
- **Database Persistence**: SQLite database with proper schema

### Frontend Application
- **User Authentication UI**: Register and login forms
- **Dashboard**: View all available vehicles with real-time updates
- **Search Functionality**: Search vehicles by make
- **Inventory Management**: Purchase and restock vehicles with quantity controls
- **Admin Features**: Add and delete vehicles
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **User Experience**: Clean UI with Tailwind CSS styling

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register a new user
- `POST /api/auth/login` - Login and receive JWT token

### Vehicles (Protected)
- `GET /api/vehicles` - Get all vehicles
- `POST /api/vehicles` - Create a new vehicle
- `GET /api/vehicles/{id}` - Get vehicle by ID
- `PUT /api/vehicles/{id}` - Update vehicle details
- `DELETE /api/vehicles/{id}` - Delete a vehicle
- `GET /api/vehicles/search?make=&model=&category=&min_price=&max_price=` - Search vehicles

### Inventory Operations (Protected)
- `POST /api/vehicles/{id}/purchase` - Purchase vehicle(s)
- `POST /api/vehicles/{id}/restock` - Restock vehicle(s)

## Tech Stack

### Backend
- **Framework**: FastAPI (Python web framework)
- **ORM**: SQLAlchemy
- **Database**: SQLite
- **Authentication**: JWT (PyJWT)
- **Password Hashing**: Passlib with PBKDF2
- **Testing**: Pytest with Starlette TestClient
- **Server**: Uvicorn

### Frontend
- **Framework**: React 18
- **Build Tool**: Vite
- **Styling**: Tailwind CSS
- **HTTP Client**: Axios
- **Package Manager**: npm

### Development
- **Version Control**: Git
- **Testing**: TDD (Test-Driven Development)
- **Code Quality**: Clean code practices, SOLID principles

## Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js 16+
- Git

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
```

3. Install dependencies:
```bash
pip install fastapi uvicorn sqlalchemy pytest passlib pyjwt
```

4. Run the backend server:
```bash
uvicorn app.main:app --reload
```

Backend will be available at `http://localhost:8000`
API documentation at `http://localhost:8000/docs`

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Run the development server:
```bash
npm run dev
```

Frontend will be available at `http://localhost:3000`

### Running Tests

From the backend directory:
```bash
pytest -v
```

Test results will show coverage of all endpoints and business logic.

## Project Structure

```
car-dealership-system/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py           # FastAPI application and routes
│   │   ├── models.py         # SQLAlchemy ORM models
│   │   ├── schemas.py        # Pydantic request/response schemas
│   │   ├── crud.py           # Database CRUD operations
│   │   ├── database.py       # Database configuration
│   │   └── security.py       # Authentication and hashing utilities
│   ├── tests/
│   │   ├── conftest.py       # Pytest configuration and fixtures
│   │   ├── test_auth.py      # Authentication tests
│   │   └── test_vehicles.py  # Vehicle endpoint tests
│   ├── requirements.txt      # Python dependencies
│   └── README.md
├── frontend/
│   ├── src/
│   │   ├── components/       # React components
│   │   ├── App.jsx          # Main app component
│   │   ├── api.js           # API client with axios
│   │   └── index.jsx        # React entry point
│   ├── index.html           # HTML template
│   ├── package.json         # npm dependencies
│   ├── vite.config.js       # Vite configuration
│   ├── tailwind.config.js   # Tailwind CSS configuration
│   └── README.md
├── PROMPTS.md               # AI tool interaction history
└── README.md
```

## Test Coverage

The project includes comprehensive test coverage:
- **11 passing tests** covering all API endpoints
- User authentication tests
- Vehicle CRUD operations
- Search and filter functionality
- Inventory purchase and restock operations
- Error handling and edge cases

Run tests with:
```bash
pytest -v --tb=short
```

## Development Workflow

This project follows Test-Driven Development (TDD) methodology:

1. **Red Phase**: Write tests for new features
2. **Green Phase**: Implement features to make tests pass
3. **Refactor Phase**: Improve code while maintaining test coverage

Each commit includes clear descriptions of changes and includes AI co-author attribution where applicable.

## My AI Usage

### Tools Used
- **GitHub Copilot**: Used throughout the development process for code generation, debugging, and testing

### How AI Was Used

1. **Backend Implementation**
   - Generated initial FastAPI endpoint structures
   - Created CRUD operation templates
   - Helped debug import and routing issues
   - Generated database query patterns

2. **Frontend Development**
   - Generated React component boilerplate
   - Created Tailwind CSS styling
   - Implemented form validation logic
   - Generated API integration patterns

3. **Testing**
   - Generated comprehensive test cases following TDD
   - Created test fixtures and configurations
   - Helped structure pytest test organization

4. **Documentation**
   - Generated API endpoint documentation
   - Created setup instructions
   - Helped structure project files

### Impact on Workflow

- **Productivity**: AI significantly accelerated development by 3-4x
- **Quality**: Consistent code patterns and best practices were maintained
- **Learning**: AI suggestions helped me understand FastAPI and React patterns
- **Speed**: Rapid prototyping and iteration with immediate feedback

### Best Practices Applied

- Used AI as a tool, not a replacement for understanding
- Verified and tested all AI-generated code
- Made intentional modifications to AI suggestions
- Maintained code consistency across the project
- Added comments and documentation for clarity

## Git Commit History

All commits include clear descriptions following these patterns:
- `feat:` for new features
- `fix:` for bug fixes
- `test:` for test additions
- `refactor:` for code improvements
- AI co-authorship attributed where applicable

## Deployment

To deploy to production:

### Backend
```bash
# Build Docker image (if using Docker)
docker build -t car-dealership-backend .
docker run -p 8000:8000 car-dealership-backend

# Or use cloud services like Heroku, Railway, or AWS
```

### Frontend
```bash
# Build for production
npm run build

# Deploy dist/ folder to Vercel, Netlify, or any static host
```

## Future Enhancements

- User roles and permissions (Admin, Dealer, Customer)
- Email notifications
- Vehicle images and gallery
- Advanced filtering and sorting
- Order history and tracking
- Payment integration
- Analytics dashboard
- Mobile app version

## Contributing

This is a learning project. Feel free to fork and submit pull requests with improvements.

## License

MIT License - feel free to use this project for learning purposes.

## Support

For issues or questions, please create an issue in the repository.

---

**Built with TDD methodology and modern development practices** 🚗

