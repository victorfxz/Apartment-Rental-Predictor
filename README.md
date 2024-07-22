# Apartment Rental Price Prediction for Sao Paulo - Brazil
<p align="center"><img src="https://camo.githubusercontent.com/2395b9addd283caae164beb046a4c22d0bcf28c6b2a56eca306248eb3ab52164/68747470733a2f2f6d7277616c6c70617065722e636f6d2f696d616765732f68642f73616f2d7061756c6f2d6272617a696c2d706f6e74652d6573746169616469612d6272696467652d717732366c35323839393537776165362e6a7067" width="550"></p>

## Project Overview
<p align="justify">This final project of the MLOps Zoomcamp course aims to predict apartment rental prices in São Paulo, Brazil, using a dataset with information on approximately 13,000 apartments in this large city. The objective is to develop a machine learning model to facilitate decision-making for potential tenants, those considering future purchases, and even investors or small businesses looking to establish themselves in the city. This model will help them better understand and evaluate rental prices in this vast metropolis, which encompasses various neighborhoods and buildings. Consequently, I hope this project can contribute to more transparent and accessible real estate choices, leading to data-driven decisions about whether living in a chosen building is truly worthwhile.</p>

> ✅ The dataset used is available at: https://www.kaggle.com/datasets/argonalyst/sao-paulo-real-estate-sale-rent-april-2019

## Problem Description
<p align="justify">Rental prices for any type of apartment are influenced by several factors to reach an acceptable value for the owner, such as location, size/built area, number of rooms, and other property features. As São Paulo (Brazil) is the largest city in Brazil, with numerous businesses and companies of all sizes and sectors established, these factors are amplified, significantly increasing living costs and quality of life. Consequently, depending on the neighborhood and building, prices can vary considerably, making the decision to rent an apartment challenging due to the need to balance necessity, available funds, and the purpose of the lease. In this context, this project aimed to develop a machine learning model that can predict, more accurately, apartment rental prices to help interested parties find affordable and/or suitable housing based on their needs.</p>

## Technologies and Tools Used
### Key Technologies
ㅤ<img src="https://github.com/user-attachments/assets/d48aa56b-bce1-404d-9b72-25632905c001" width="13">ㅤ**Anaconda** - Used for package management and creating the virtual environment  
ㅤ<img src="https://github.com/user-attachments/assets/ec87d23a-028b-43f1-b739-8195e256c817" width="13">ㅤ**Docker** - Used for containerization of the application  
ㅤ<img src="https://github.com/user-attachments/assets/8f674d6d-62f0-4e7d-a5b1-922d72911d53" width="13">ㅤ**Flask** - Used for deploying the model (web service)  
ㅤ<img src="https://github.com/user-attachments/assets/27fb21a1-33bb-478e-b755-e33bec6c3bbf" width="13">ㅤ**Grafana** - Used for monitoring the performance of the prediction model  
ㅤ<img src="https://github.com/user-attachments/assets/818cc442-56fd-4400-874d-a1d0a791cfbb" width="13">ㅤ**MLflow** - Used for experiment tracking and logging of the prediction model  
ㅤ<img src="https://github.com/user-attachments/assets/eb3e7942-ae1e-4542-be6b-79b5d5078c25" width="13">ㅤ**Node.js** - Used for front-end development  
ㅤ<img src="https://cdn.worldvectorlogo.com/logos/prefect-1.svg" width="13">ㅤ**Prefect** - Used for workflow orchestration  
ㅤ<img src="https://github.com/user-attachments/assets/d19d6bf8-7500-47c7-92bf-c3f46229099a" width="13">ㅤ**Vercel** - Used as a cloud-based web application hosting and deployment platform  

### Libraries Used
ㅤ<img src="https://github.com/user-attachments/assets/9dd16004-ce95-4961-8e5a-fe22369784be" width="14">ㅤ**Pandas** -Used for data manipulation and analysis  
ㅤ<img src="https://github.com/user-attachments/assets/97bba754-6e20-4fc9-ac8d-b8c919555837" alt="PybSklearn" width="13">ㅤ**Scikit-learn** - Used for building, training, and evaluating the prediction model  
ㅤ<img src="https://github.com/user-attachments/assets/acdeb0d6-3baf-4dda-a06d-d518e0d9a2b0" alt="PybMathplot" width="13">ㅤ**Matplotlib** - Used for data visualization  

### Other Tools Used for Development
ㅤ<img src="https://github.com/user-attachments/assets/ec1b86c6-492f-4345-ad16-6dc138b990c3" width="13">ㅤ**Git** - Used for version control  
ㅤ<img src="https://github.com/user-attachments/assets/704b646c-58ae-426d-8f1c-e7c2c7fc964b" width="13">ㅤ**Visual Studio Code** - Used for debugging and managing Python code and other files  
ㅤ<img src="https://github.com/user-attachments/assets/d3eee82b-8a6b-4789-8182-d4d6816f0273" width="13">ㅤ**Jupyter Notebook** - Used for data exploration and visualization  
ㅤ<img src="https://github.com/user-attachments/assets/52316734-849b-4f46-8bf8-6a7f839405af" width="13">ㅤ**PostgreSQL** - Used as a relational database management system  


## Dataset
<p align="justify">The <a href="https://www.kaggle.com/datasets/argonalyst/sao-paulo-real-estate-sale-rent-april-2019">dataset</a> used in this project includes information about apartments for rent in the greater city of São Paulo, Brazil, provided in April 2019. The dataset contains various features, such as whether the building has a pool, elevator, or the age of the building. However, the main features of the dataset include:</p>

- **Latitude and Longitude**: Geographic coordinates of the apartment 
- **Number of Bedrooms**: Number of bedrooms in the apartment  
- **Built Area**: Size of the apartment in square meters (m²)  
- **Rental Price**: Rental price in Brazilian Reais (R$) **[🎯 prediction target ]**

## Project hosted on Vercel [Cloud Platform]
https://apartment-rental-predictor.vercel.app/

## Project Execution [Locally]
### **Pre-requisites**

* Anaconda (latest version)
* Node.js (latest version)
* npm (latest version)
* Python (latest version)
  
### Environment Setup
Clone the repository:

```bash
git clone https://github.com/victorfxz/Apartment-Rental-Predictor/
cd Apartment-Rental-Predictor
```

Create and activate the virtual environment:
> ❗ **Note**: This requires the Anaconda Environmentㅤ[ <a href="https://www.anaconda.com/download/success"><img src="https://github.com/user-attachments/assets/62bb7b30-50ed-4a7c-a427-05718f023c62" width="14"></a> ]

```bash
conda create -n previsao-aluguel python=3.10
conda activate previsao-aluguel
```

> ❗ If you don't have pip installed:
> ```bash
> conda install pip

Install all dependencies:

```bash
pip install -r requirements.txt
```

### Data Exploration and Preprocessing
Start the `model_to_predict_apartment_rental_prices_SP-BR` notebook with Jupyter Notebook:

```bash
jupyter notebook
```

### Model Deployment
Start the Flask server to deploy the model:

```bash
python app.py
```

Create a new Next.js project using the following command:
> ❗ **Note**: This requires Node.jsㅤ[ <a href="https://nodejs.org/en/download/prebuilt-installer/current"><img src="https://github.com/user-attachments/assets/62bb7b30-50ed-4a7c-a427-05718f023c62" width="14"></a> ]

```
npx create-next-app@latest apartment-rental-predictor
```

This will create a new Next.js project in a directory called `apartment-rental-predictor`.

2. Change into the project directory:
   
```
cd apartment-rental-predictor
```

3. Install the required dependencies, including Axios:

```
npm install axios
```

### Running the Application
0. Download the `app.py` and `page.tsx` files into the app-rental-apartment folder

1. Run the Python script that powers the apartment rental predictor:

```
python app.py
```

This script will perform the necessary calculations and provide the predictions.

2. Start the Next.js development server:

```
npx next
```

This will start the development server and make the application available at `http://localhost:3000`.

## More Information
<p align="justify">In the other folders, you will find additional files that were generated or developed during this project. Further information on the usage of MLflow and Prefect can be found in the `mlflow-prefect-deployment` folder.</p>

## Final Consideration
<p align="justify">This prediction model, despite its specific segment, can be particularly interesting for people who wish to live in the city of São Paulo and want a general or location-specific estimate of apartment rental prices based on coordinates.

This project was developed as the final assignment for the MLOps Zoomcamp course.</p>

