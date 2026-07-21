import React from 'react';
import VehicleCard from './VehicleCard';

export default function VehicleList({ vehicles, onPurchase, onRestock, onDelete }) {
  if (vehicles.length === 0) {
    return (
      <div className="text-center py-12">
        <p className="text-xl text-gray-600">No vehicles available</p>
      </div>
    );
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {vehicles.map((vehicle) => (
        <VehicleCard 
          key={vehicle.id} 
          vehicle={vehicle}
          onPurchase={onPurchase}
          onRestock={onRestock}
          onDelete={onDelete}
        />
      ))}
    </div>
  );
}
