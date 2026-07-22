import React, { useState, useEffect } from 'react';
import { vehiclesAPI } from '../api';
import VehicleList from './VehicleList';
import AddVehicleForm from './AddVehicleForm';

export default function Dashboard({ onLogout }) {
  const [vehicles, setVehicles] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [loading, setLoading] = useState(true);
  const [showAddForm, setShowAddForm] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchVehicles();
  }, []);

  const fetchVehicles = async () => {
    setLoading(true);
    try {
      const response = await vehiclesAPI.getAll();
      setVehicles(response.data);
      setError('');
    } catch (err) {
      setError('Failed to load vehicles');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleSearch = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await vehiclesAPI.search({ make: searchTerm });
      setVehicles(response.data);
    } catch (err) {
      setError('Search failed');
    } finally {
      setLoading(false);
    }
  };

  const handleClearSearch = async () => {
    setSearchTerm('');
    await fetchVehicles();
  };

  const handleVehicleAdded = async () => {
    setShowAddForm(false);
    await fetchVehicles();
  };

  const handlePurchase = async (vehicleId, quantity) => {
    try {
      await vehiclesAPI.purchase(vehicleId, quantity);
      await fetchVehicles();
    } catch (err) {
      setError('Purchase failed: ' + (err.response?.data?.detail || 'Unknown error'));
    }
  };

  const handleRestock = async (vehicleId, quantity) => {
    try {
      await vehiclesAPI.restock(vehicleId, quantity);
      await fetchVehicles();
    } catch (err) {
      setError('Restock failed');
    }
  };

  const handleDelete = async (vehicleId) => {
    if (window.confirm('Are you sure you want to delete this vehicle?')) {
      try {
        await vehiclesAPI.delete(vehicleId);
        await fetchVehicles();
      } catch (err) {
        setError('Delete failed');
      }
    }
  };

  return (
    <div className="min-h-screen bg-neutral-50">
      <nav className="bg-white text-neutral-900 p-4 border-b border-neutral-200">
        <div className="max-w-7xl mx-auto flex justify-between items-center">
          <h1 className="text-2xl font-bold">Car Dealership System</h1>
          <button
            onClick={onLogout}
            className="bg-red-600 hover:bg-red-700 px-4 py-2 rounded-lg font-semibold"
          >
            Logout
          </button>
        </div>
      </nav>

      <div className="max-w-7xl mx-auto p-6">
        {error && (
          <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
            {error}
            <button onClick={() => setError('')} className="ml-4 font-bold">×</button>
          </div>
        )}

        <div className="mb-6 flex gap-4">
          <form onSubmit={handleSearch} className="flex-1">
            <input
              type="text"
              placeholder="Search by make..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </form>
          {searchTerm && (
            <button
              onClick={handleClearSearch}
              className="bg-gray-600 text-white px-4 py-2 rounded-lg hover:bg-gray-700"
            >
              Clear Search
            </button>
          )}
          <button
            onClick={() => setShowAddForm(!showAddForm)}
            className="bg-green-600 text-white px-6 py-2 rounded-lg hover:bg-green-700 font-semibold"
          >
            {showAddForm ? 'Cancel' : '+ Add Vehicle'}
          </button>
        </div>

        {showAddForm && (
          <div className="mb-6 bg-white p-6 rounded-lg shadow-md">
            <AddVehicleForm onVehicleAdded={handleVehicleAdded} />
          </div>
        )}

        {loading ? (
          <div className="text-center py-8">
            <p className="text-xl text-gray-600">Loading vehicles...</p>
          </div>
        ) : (
          <VehicleList 
            vehicles={vehicles} 
            onPurchase={handlePurchase}
            onRestock={handleRestock}
            onDelete={handleDelete}
          />
        )}
      </div>
    </div>
  );
}
