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

### **EXPLORATORY DATA ANALYSIS**

  <table>
  <tr>
    <td align="left">
      <img width="500" height="300" alt="hist" src="https://github.com/user-attachments/assets/d2c0eb52-0b3c-4c3c-b927-f3fba2c9d95f" />
    </td>
    <td align="right">
      <img width="500" height="300" alt="pie" src="https://github.com/user-attachments/assets/f7ca4fa1-3c07-437f-87e7-296046aed5ac" />
    </td>
  </tr>
</table>

<table>
  <tr>
    <td align="left">
      <img width="500" height="300" alt="box" src="https://github.com/user-attachments/assets/9f4ca1a9-f104-41b4-b5d3-eb21e6ff4c04" />
    </td>
    <td align="right">
      <img width="500" height="300" alt="bar" src="https://github.com/user-attachments/assets/69d784d7-d27c-470c-adb1-954d3df2673c" />
    </td>
  </tr>
</table>

<table>
  <tr>
    <td align="left">
      <img width="500" height="300" alt="reg" src="https://github.com/user-attachments/assets/e2eb8113-2dd3-4602-914a-ec50fbdef5da" />
    </td>
    <td align="right">
      <img width="500" height="300" alt="vio" src="https://github.com/user-attachments/assets/583cf437-a709-4c05-9e46-92a344e3fdee" />
   </td>
  </tr>
</table>

### **ASSUMPTIONS OF LINEAR REGRESSION**
- Errors should be randomly distributed with no pattern.This ensures linearity and that the model is not systematically biased.From below plot we can assume that there is no pattern in the errors, and the errors are randomly distributed indicating satisfied assumptions.
<p align="center">
  <img width="450" height="350" alt="pt" src="https://github.com/user-attachments/assets/dcf1c283-c6cc-4ea4-86b9-a2f8762070fb" />
</p>

- Normally distributed errors mean that most predictions are close to actual values, with fewer deviations.It helps ensure that model predictions are unbiased.Errors should be symmetrically distributed around zero.From the below plot we can assume that errors are Normally Distibuted.
<p align="center">
  <img width="450" height="350" alt="nd" src="https://github.com/user-attachments/assets/6efebf6b-02d4-4264-b001-2e7877f48b24" />
</p>

- Homoscedasticity ensures that the model’s predictions are equally reliable for all the values.The variance of errors should be constant across all the values and it should be close to the regression line.From the below plot we can assume that Homoscedasticity is satisfied.
<p align="center">
  <img width="450" height="350" alt="hs" src="https://github.com/user-attachments/assets/0293f268-f8c9-45b1-b99b-dc6b94318476" />
</p>

### **CORRELATION MATRIX**
- A correlation matrix displays how every variable in a dataset is related to every other variable by values ranging from -1 to +1.
- Values near 1 indicate strong positive correlation, near -1 indicate strong negative correlation, and near 0 indicate no relationship.
- Each variable is perfectly correlated with itself, so the diagonal of the matrix always has 1.
- The correlation between variable A and B is the same as between B and A.
- It is often represented by heatmap, making it easier to spot strong or weak correlations at a glance.
<p align="center">
  <img width="500" height="450" alt="cr" src="https://github.com/user-attachments/assets/685eab31-bc8d-4161-8579-603548fd8727" />
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







