# Cricket Score Predictor
This project is designed to predict cricket match scores using machine learning models.

## Inputs for Prediction
1.Name of Teams Playing  
2.Location  
3.Current Score  
4.Wickets Taken  
5.Overs done  
6.Runs made in last 5 overs

## Usage
This script is designed to predict cricket scores using a machine learning model. The model is trained using the **XGBoost** algorithm, which is known for its high performance and efficiency in handling structured data. I utilize the **scikit-learn** (`sklearn`) library to manage the data preprocessing, model training, and evaluation processes.I also utilized

### Requirements:
- **XGBoost:** Used for building the regression model. It provides an implementation of the gradient boosting algorithm.
- **scikit-learn (sklearn):** Used for splitting the dataset, preprocessing data, and evaluating the model's performance.
- **yaml**: Utilized for safely parsing YAML files, which contain structured data configurations.
- **tqdm**: A library used to display progress bars for loops, making it easier to track the progress of operations, such as data loading.

### Example:
To run the script, ensure you have the necessary libraries installed:

```bash
pip install xgboost scikit-learn pandas numpy streamlit pyyaml tqdm
