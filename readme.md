# Bank Marketing Prediction

Welcome to the **Bank Marketing Prediction** project! This web application is designed to predict whether a client is likely to subscribe to a term deposit based on several factors like contact duration, employee variation rate, and client age.

## 🚀 Getting Started

### Prerequisites

Before getting started, ensure that you have the following installed:

- Python (>= 3.8)
- Django (>= 3.2)
- XGBoost (>= 1.3.0)

### 🛠️ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/firasabdelaziz/bank-marketing-prediction.git
cd bank-marketing-prediction
```

2. **Create a virtual environment and install dependencies:**

```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows
pip install -r requirements.txt
```

3. **Make and apply migrations:**

```bash
python manage.py makemigrations
python manage.py migrate
```

4. **Run the development server:**

```bash
python manage.py runserver
```

5. **Access the application** by navigating to [http://127.0.0.1:8000](http://127.0.0.1:8000).

## 📐 Features

- **Predict Client Subscription**: Use the form to input contact duration, employee variation rate, and client age to predict whether a client will subscribe to a term deposit.
- **XGBoost Machine Learning Model**: The predictions are powered by an XGBoost model (`xgboost_model.json`) that processes input data and returns a probability.
- **Interactive UI**: Built with **Bootstrap 5**, the UI is responsive and user-friendly, providing a clean and modern design.

## 🖥️ Files Overview

### 1. **`prediction/forms.py`**
   - Contains the form where users input values for contact duration, employee variation rate, and client age.

### 2. **`prediction/views.py`**
   - Handles the view logic to process the form and pass the results to the template.

### 3. **`prediction/utils.py`**
   - Contains the prediction model using **XGBoost** to load the model and make predictions.

### 4. **Templates:**
   - **`base.html`**: Base template with the common structure for all pages.
   - **`predict.html`**: Form to input data and display prediction results.

### 5. **Static Files:**
   - **`style.css`**: Custom styles for the web app to enhance the user interface.

## 🔍 Model Overview

- **Model Type**: **XGBoost Regressor**
- **Model Location**: `prediction/ml_model/xgboost_model.json`
- **Prediction Output**: 
  - Likelihood of subscribing to a term deposit (binary: yes/no).
  - Probability of prediction.

## 💡 How It Works

1. **User Input**: The user enters the contact duration, employee variation rate, and client age into the form.
2. **Prediction**: Upon submission, the form data is sent to the backend, where the XGBoost model is used to predict whether the client will subscribe to a term deposit.
3. **Results**: The prediction is displayed along with the probability percentage.

## 🧑‍💻 Development Setup

To get the app running on your local machine, follow these steps:

1. **Clone the repository** to your local machine.
2. **Install required dependencies** using `pip install -r requirements.txt`.
3. **Run the Django server**: `python manage.py runserver`.
4. **Access the app** in your browser at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## 📁 Directory Structure

```
bank-marketing-prediction/
│
├── prediction/
│   ├── migrations/
│   ├── ml_model/
│   │   └── xgboost_model.json      # XGBoost model file
│   ├── templates/
│   │   └── prediction/
│   │       ├── base.html           # Base HTML template
│   │       └── predict.html        # Prediction form and result template
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py                   # Form for prediction
│   ├── models.py
│   ├── tests.py
│   ├── urls.py                    # URL routing for views
│   └── utils.py                   # Prediction model logic
├── static/
│   └── css/
│       └── style.css              # Custom styles for the app
├── manage.py
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
```

## 🔧 Customizing

- **Model Update**: You can replace the `xgboost_model.json` file in the `ml_model/` directory with your own trained XGBoost model.
- **UI Customization**: Modify the **CSS** file to adjust the design and appearance of the app.

## 📝 Notes

- Ensure the **XGBoost model file** (`xgboost_model.json`) is correctly placed in the `prediction/ml_model/` directory for predictions to work.
- If you encounter issues with Django versions or dependencies, check the `requirements.txt` for compatible versions of the libraries.

## 💬 Questions or Issues?

Feel free to open an issue on GitHub or reach out if you have any questions regarding the setup or usage of this project!