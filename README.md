## **MACHINE LEARING BASED SALARY PREDICTION USING REGRESSION MODEL**

### **PROBLEM STATEMENT**
Many students and organizations lack a clear understanding of the salary outcomes associated with academic performance. Predicting salaries based on student performance can help in career planning and informed decision-making.

### **OBJECTIVE**
To develop a regression based machine learning predictive model that analyse student academic records to forecast future salary outcomes."

### **PROJECT WORKFLOW**
<p align="left">
<img width="300" height="200" alt="image" src="https://github.com/user-attachments/assets/c076f47f-4c3e-46fa-a293-b974e6e2a500" />
  
### **DATASET OVERVIEW**
- The dataset is obtained from Kaggle, a widely used platform for machine learning datasets
- The original dataset contains approximately 1,00,000 records, including both placed and not  placed students 
- For this project, the dataset was filtered to include only placed students for salary prediction 
- The filtered dataset contains 84,432 records and 26 columns (features) 
- The target variable is Salary, which is predicted using regression techniques 
- The dataset consists of both numerical and categorical variables 
- It includes student-related information such as education, skills, experience, and other attributes influencing salary

### **DATA PREPROCESSING**
- Dropped irrelevant columns such as Student ID or unique identifiers, as they do not contribute to salary prediction 
- Identified and handled  null values using  techniques such as removal to ensure data completeness 
- Converted categorical variables such as gender and degree field into numerical format 
- Selected the most relevant features that significantly influence salary prediction and removed  less important columns 
- Split the dataset into training and testing sets to evaluate the model’s performance on unseen data 
- Prepared the final cleaned dataset in a structured format suitable for building and testing the regression model

### **Exploratory Data Analysis**

<p align="center">
 <img width="300" height="150" alt="hist" src="https://github.com/user-attachments/assets/7f162ae6-90fb-4c82-bff1-9e9ad43c7d9f" />
 <img width="300" height="150" alt="pie" src="https://github.com/user-attachments/assets/fe1d6cca-28db-4d73-962d-e6281ba09a38" />
 <img width="300" height="150" alt="bar" src="https://github.com/user-attachments/assets/c540ad39-01ee-41a9-b2a1-73f6d186ddc7" />
</p>

### **EVALUATION MATRIX**
- The performance of the regression model was evaluated using multiple error metrics to ensure accurate prediction of salary 
- Mean Squared Error (MSE) measures the average squared difference between the predicted values and the actual values
- Root Mean Squared Error (RMSE) calculates the square root of the average squared differences, placing higher importance on larger errors 
- Mean Absolute Percentage Error (MAPE) measures the average percentage difference between actual and predicted values to interpret model accuracy 
- Lower values of MAE and RMSE indicate smaller prediction errors and better model performance 
- A lower MAPE value indicates higher accuracy and better reliability of the model 

### **MODEL PERFORMANCE**
- The regression model was evaluated using performance metrics on both training and testing data 
- Training data results: MSE = 1.1070, RMSE = 1.0521, MAPE = 7.81% 
- Testing data results: MSE = 1.1059, RMSE = 1.0516, MAPE = 7.82% 
- The training and testing error values are very close, indicating consistent model performance 
- The model achieved an approximate accuracy of 92%, showing reliable predictions 
- There is no significant difference between training and testing results, indicating the model is not overfitting 
- The model maintains stability across both training and testing datasets

### **DEPLOYMENT**
- The trained regression model was deployed using Streamlit to create an interactive web application
- A user-friendly interface was developed to allow users to input details such as experience, education, and other relevant features 
- The application processes user input and sends it to the trained model for prediction 
- The model generates real-time salary predictions based on the given inputs 
- The model was saved using pickle and loaded into the Streamlit app for efficient prediction 
- This deployment makes the model accessible to non-technical users and supports real-world usage 

### **FUTURE WORK**
- To improve model accuracy by training on a larger and more diverse dataset 
- Experiment with advanced algorithms such as Boosting Models
- Incorporate additional features such as  location, and industry trends for better predictions 
- Enhance model interpretability by using advanced explainability techniques 
- Deploy the application on cloud platforms for wider accessibility and real-time usage 
- Implement real-time data integration to keep the model updated with current trends 







