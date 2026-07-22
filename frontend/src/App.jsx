import './index.css';
import React, { useState } from 'react';
import Login from './components/Login';
import Register from './components/Register';
import Dashboard from './components/Dashboard';

export default function App() {
  const [page, setPage] = useState('login');
  const [isLoggedIn, setIsLoggedIn] = useState(!!localStorage.getItem('token'));

  const handleLoginSuccess = () => {
    setIsLoggedIn(true);
    setPage('dashboard');
  };

  const handleLogout = () => {
    localStorage.removeItem('token');
    setIsLoggedIn(false);
    setPage('login');
  };

  if (isLoggedIn) {
    return <Dashboard onLogout={handleLogout} />;
  }

  return (
    <div className="min-h-screen bg-neutral-100 flex items-center justify-center p-4">
      <div className="bg-white rounded-lg shadow-2xl w-full max-w-md p-8">
        {page === 'login' ? (
          <>
            <Login onLoginSuccess={handleLoginSuccess} />
            <p className="text-center mt-4">
              Don't have an account?{' '}
              <button
                onClick={() => setPage('register')}
                className="text-neutral-900 hover:underline font-semibold underline-offset-2"
              >
                Register
              </button>
            </p>
          </>
        ) : (
          <>
            <Register onRegisterSuccess={() => setPage('login')} />
            <p className="text-center mt-4">
              Already have an account?{' '}
              <button
                onClick={() => setPage('login')}
                className="text-neutral-900 hover:underline font-semibold underline-offset-2"
              >
                Login
              </button>
            </p>
          </>
        )}
      </div>
    </div>
  );
}
