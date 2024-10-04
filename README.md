## Worker PPE Detection using YOLOv8

This project involves a deep learning model to detect whether a worker is wearing all the required Personal Protective Equipment (PPE), such as helmets, gloves, masks, vests, and shoes. The model is built using the YOLOv8 neural network architecture, specifically designed for object detection tasks.

## Key Features

- **Neural Network Architecture**: Utilizes YOLOv8, a state-of-the-art deep learning model for object detection, known for its speed and accuracy.
- **Classes of Detection**: The model is trained to detect the following classes:
  - **Helmet**: Detects if a helmet is worn.
  - **No-Helmet**: Detects if no helmet is worn.
  - **Gloves**: Detects if gloves are worn.
  - **No-Gloves**: Detects if no gloves are worn.
  - **Mask**: Detects if a mask is worn.
  - **No-Mask**: Detects if no mask is worn.
  - **Goggles**: Detects if goggles are worn.
  - **No-Goggles**: Detects if no goggles are worn.
  - **Vest**: Detects if a safety vest is worn.
  - **No-Vest**: Detects if no safety vest is worn.
  - **Shoes**: Detects if safety shoes are worn.
  - **No-Shoes**: Detects if no safety shoes are worn.
- **Alert System**: The model is equipped with an alert mechanism that triggers when any "no" class is detected (e.g., no-helmet, no-gloves, no-mask, no-goggles, no-vest, no-shoes). When an alert is triggered, an email is sent using the `smtplib` library, containing an alert message and a photograph highlighting the detected non-compliance.

## Dataset and Optimization

- **Dataset**: Trained on a dataset of approximately 4,500 images, containing various PPE scenarios to ensure robust detection across different conditions.
- **Optimizer**: Employed the AdamW optimizer to enhance model convergence and performance.

## Usage

This model can be used in safety compliance applications to monitor and ensure workers are properly equipped with all necessary PPE, improving workplace safety standards.

## Output Example

**Input Image:**
![Input Image](https://i.imgur.com/xHrUzWX.jpeg)

**Detected Image:**
![Detected Image](https://i.imgur.com/3isqLC5.png)

**Email Alert:**
![Email Alert](https://i.imgur.com/T765Nsz.png)

## Model Evaluation

**Confusion Matrix:**
![Confusion Matrix](https://i.imgur.com/WPiCSXE.png)
