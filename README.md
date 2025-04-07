# MNIST Digit Classification 🧠🔢

This project compares the performance of **Logistic Regression**, **Support Vector Machine (SVC)**, and **Random Forest Classifier** on the [MNIST dataset](https://www.openml.org/d/554), a classic benchmark dataset of handwritten digits.

![MNIST Sample](https://upload.wikimedia.org/wikipedia/commons/2/27/MnistExamples.png)

## 📁 Dataset Info
- **Name**: MNIST 784
- **Source**: [OpenML](https://www.openml.org/d/554)
- **Samples**: 70,000
- **Features**: 784 (28x28 pixels flattened)
- **Classes**: 10 (digits 0 through 9)

## 🔧 Models Used
- **Logistic Regression**
- **Support Vector Classifier (SVC)**
- **Random Forest Classifier**

## 🧪 Evaluation Metrics
- Accuracy
- F1 Score (macro)

## 📊 Results (on test set)
| Model                | Accuracy | F1 Score (macro) |
|---------------------|----------|------------------|
| Logistic Regression | 0.9178   | 0.9166           |
| SVC                 | 0.9764   | 0.9763           |
| Random Forest       | 0.9673   | 0.9671           |



## 🖼️ Sample Predictions

The code includes visualization of the first 16 test images with their **true** and **predicted** labels:

