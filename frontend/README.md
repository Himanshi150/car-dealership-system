# Car Dealership Frontend

A modern React application for managing car dealership inventory.

## Setup Instructions

### Install Dependencies
```bash
npm install
```

### Development Server
```bash
npm run dev
```

The frontend will start at `http://localhost:3000` and automatically proxy API calls to `http://localhost:8000`.

### Build for Production
```bash
npm run build
```

The built files will be in the `dist/` directory.

## Features

- User authentication (register/login)
- View all available vehicles
- Search vehicles by make
- Purchase vehicles (decreases inventory)
- Restock vehicles (increases inventory)
- Add new vehicles to inventory
- Delete vehicles
- Responsive design with Tailwind CSS

## Tech Stack

- React 18
- Vite (build tool)
- Tailwind CSS (styling)
- Axios (HTTP client)
