'use client';

import Head from 'next/head';
import axios from 'axios';
import './app.css';
import { useState } from 'react';

function Home() {
  const [latitude, setLatitude] = useState('');
  const [longitude, setLongitude] = useState('');
  const [numeroDeQuartos, setNumeroDeQuartos] = useState('');
  const [areaConstruida, setAreaConstruida] = useState('');
  const [prediction, setPrediction] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handlePredict = async () => {
    if (
      latitude &&
      longitude &&
      numeroDeQuartos &&
      areaConstruida &&
      Number(latitude) >= -26.923 &&
      Number(latitude) <= -21.856 &&
      Number(longitude) >= -51.978 &&
      Number(longitude) <= -42.797 &&
      Number(numeroDeQuartos) > 0 &&
      Number(areaConstruida) > 0
    ) {
      setIsLoading(true);
	  setPrediction('');
      try {
        const data = {
          'latitude': Number(latitude),
          'longitude': Number(longitude),
          'rooms': Number(numeroDeQuartos),
          'size': Number(areaConstruida),
        };

		const response = await axios.post('/front-end/predict', data);
		if (response.data.predicted_price !== undefined) {
		  const predictedPrice = response.data.predicted_price / 100;
		  const formattedPrice = predictedPrice.toLocaleString('pt-BR', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
		  setPrediction(`Predicted Apartment Rental Price (in Reais): R$${formattedPrice}`);
		} else {
		  setPrediction('An error occurred while making the prediction. Please try again later.');
		}
      } catch (error) {
        console.error("Error while making the prediction: ", error);
        setPrediction('An error occurred while making the prediction. Please try again later.');
      } finally {
        setIsLoading(false);
      }
    } else {
      setPrediction('Please enter all valid values to obtain a prediction!');
    }
  };

return (
  <div style={{ backgroundColor: '#4F4F4F', height: '100vh', display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', margin: '0' }}>
    <Head>
      <title>Apartment Rental Price Prediction</title>
    </Head>
    <h1 style={{ textAlign: 'center', fontWeight: '500', fontSize: '24px', color: 'white' }}>Apartment Rental Price Prediction for Sao Paulo - Brazil</h1>
    <div style={{ width: '50%', margin: '0 auto', border: 'none', padding: '20px', borderRadius: '10px', textAlign: 'center' }}>
      <div className="tooltip">
	  <input
        type="number"
        placeholder=" Latitude"
        value={latitude}
        onChange={(e) => setLatitude(e.target.value)}
        style={{ margin: '10px', padding: '10px', color: '#000000', borderRadius: '10px', width: '80%' }}
		/>
        <span className="tooltiptext1">Latitude must be between <span className="bold-text">-21.856</span> and <span className="bold-text">-26.923</span></span>
      </div>
	  <div className="tooltip">
      <input
        type="number"	
        placeholder=" Longitude"
        value={longitude}
        onChange={(e) => setLongitude(e.target.value)}
        style={{ margin: '10px', padding: '10px', color: '#000000', borderRadius: '10px', width: '80%' }}
		/>
          <span className="tooltiptext1">Longitude must be between <span className="bold-text">-42.797</span> and <span className="bold-text">-51.978</span></span>
        </div>
	  <div className="tooltip">
      <input
        type="number"
        placeholder=" Number of Bedrooms"
        value={numeroDeQuartos}
        onChange={(e) => setNumeroDeQuartos(e.target.value)}
        style={{ margin: '10px', padding: '10px', color: '#000000', borderRadius: '10px', width: '80%' }}
		/>
        <span className="tooltiptext2">values greater than <span className="bold-text">zero</span></span>
		</div>
	  <div className="tooltip">
      <input
        type="number"
        placeholder=" Built Area (m²)"
        value={areaConstruida}
        onChange={(e) => setAreaConstruida(e.target.value)}
        style={{ margin: '10px', padding: '10px', color: '#000000', borderRadius: '10px', width: '80%' }}
		/>
        <span className="tooltiptext2">values greater than <span className="bold-text">zero</span></span>
		</div>
      <button onClick={handlePredict} style={{ fontSize: '17px', width: '190px', margin: '20px', padding: '15px', backgroundColor: '#DC143C', border: 'none', color: 'white', borderRadius: '10px' }}>
        Estimate Price
      </button>
        {isLoading && <div style={{ textAlign: 'center', fontSize: '20px', marginTop: '20px', color: 'white' }}>Loading...</div>}
		<div style={{ textAlign: 'center', fontSize: '20px', marginTop: '20px', color: 'white' }}>{prediction}</div>
    </div>
  </div>
);
}

export default Home;