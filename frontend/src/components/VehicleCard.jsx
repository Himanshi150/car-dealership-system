import React, { useState } from 'react';

export default function VehicleCard({ vehicle, onPurchase, onRestock, onDelete }) {
  const [purchaseQuantity, setPurchaseQuantity] = useState(1);
  const [restockQuantity, setRestockQuantity] = useState(1);
  const [showPurchase, setShowPurchase] = useState(false);
  const [showRestock, setShowRestock] = useState(false);

  const handlePurchaseClick = () => {
    onPurchase(vehicle.id, purchaseQuantity);
    setPurchaseQuantity(1);
    setShowPurchase(false);
  };

  const handleRestockClick = () => {
    onRestock(vehicle.id, restockQuantity);
    setRestockQuantity(1);
    setShowRestock(false);
  };

  const inStock = vehicle.quantity > 0;

  return (
    <div className="bg-white border border-neutral-200 rounded-lg overflow-hidden hover:shadow-md transition-shadow">
      <div className="bg-neutral-100 p-4 text-neutral-900 border-b border-neutral-200">
        <h3 className="text-xl font-bold">{vehicle.make} {vehicle.model}</h3>
        <p className="text-sm opacity-90">{vehicle.category}</p>
      </div>

      <div className="p-4">
        <div className="mb-4">
          <div className="flex justify-between mb-2">
            <span className="text-gray-600">Price:</span>
            <span className="font-semibold text-lg text-neutral-900">${vehicle.price.toLocaleString()}</span>
          </div>
          <div className="flex justify-between">
            <span className="text-gray-600">In Stock:</span>
            <span className={`font-semibold ${inStock ? 'text-green-600' : 'text-red-600'}`}>
              {vehicle.quantity} units
            </span>
          </div>
        </div>

        <div className="space-y-2">
          {!showPurchase && (
            <button
              onClick={() => setShowPurchase(true)}
              disabled={!inStock}
              className={`w-full py-2 rounded-lg font-semibold ${
                inStock
                    ? 'bg-neutral-700 text-white hover:bg-neutral-800'
                    : 'bg-neutral-200 text-neutral-400 cursor-not-allowed'
               }`}
            >
              {inStock ? 'Purchase' : 'Out of Stock'}
            </button>
          )}

          {showPurchase && (
            <div className="flex gap-2">
              <input
                type="number"
                min="1"
                max={vehicle.quantity}
                value={purchaseQuantity}
                onChange={(e) => setPurchaseQuantity(parseInt(e.target.value))}
                className="flex-1 px-2 py-1 border border-gray-300 rounded"
              />
              <button
                onClick={handlePurchaseClick}
                className="bg-green-600 text-white px-3 py-1 rounded hover:bg-green-700"
              >
                Buy
              </button>
              <button
                onClick={() => setShowPurchase(false)}
                className="bg-gray-600 text-white px-3 py-1 rounded hover:bg-gray-700"
              >
                Cancel
              </button>
            </div>
          )}

          <button
            onClick={() => setShowRestock(!showRestock)}
            className="w-full py-2 rounded-lg font-semibold border border-neutral-300 text-neutral-900 hover:bg-neutral-100"
          >
            Restock
          </button>

          {showRestock && (
            <div className="flex gap-2">
              <input
                type="number"
                min="1"
                value={restockQuantity}
                onChange={(e) => setRestockQuantity(parseInt(e.target.value))}
                className="flex-1 px-2 py-1 border border-gray-300 rounded"
              />
              <button
                onClick={handleRestockClick}
                className="bg-green-600 text-white px-3 py-1 rounded hover:bg-green-700"
              >
                Add
              </button>
              <button
                onClick={() => setShowRestock(false)}
                className="bg-gray-600 text-white px-3 py-1 rounded hover:bg-gray-700"
              >
                Cancel
              </button>
            </div>
          )}

          <button
            onClick={() => onDelete(vehicle.id)}
            className="w-full py-2 rounded-lg font-semibold bg-red-600 text-white hover:bg-red-700"
          >
            Delete
          </button>
        </div>
      </div>
    </div>
  );
}
