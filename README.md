# RetinaXplain: Diabetic Retinopathy Screening

## Smart India Hackathon 2026

**Problem Statement ID:** 26038  
**Problem Statement:** Explainable AI for Diabetic Retinopathy Screening in Rural India

## Problem

Diabetic Retinopathy (DR) can cause preventable blindness if it is not identified early. Rural healthcare centres often have limited access to ophthalmologists, so retinal-image screening needs to be faster, accessible, and easy for doctors to validate.

## Our Solution

RetinaXplain is a web-based prototype for diabetic-retinopathy screening using retinal fundus images.

A healthcare worker can:

1. Upload a retinal fundus image
2. Click the Analyze button
3. View the predicted DR severity level
4. View the confidence score
5. Receive a referral recommendation

## DR Severity Levels

| Level | Condition | Suggested Action |
|---|---|---|
| 0 | No DR | Continue annual screening |
| 1 | Mild NPDR | Monitor and rescreen in 6 months |
| 2 | Moderate NPDR | Refer to an ophthalmologist within 3 months |
| 3 | Severe NPDR | Urgent ophthalmologist referral |
| 4 | Proliferative DR | Immediate specialist referral |

## Key Features

- Web-based interface for retinal fundus-image upload
- DR severity classification from Level 0 to Level 4
- Confidence score for each prediction
- Clinical recommendation based on predicted severity
- Designed for a future low-bandwidth rural telemedicine workflow
- Planned Grad-CAM attention map to show the retinal regions used by the AI
- Human-in-the-loop review concept for ophthalmologists

## Current Prototype Status

This repository contains an early user-interface prototype built in Google Colab using Python and Gradio.

The current version demonstrates the screening workflow and user interface. A future version will integrate and clinically validate a trained model using public retinal-image datasets such as APTOS 2019, IDRiD, DRIVE, and Messidor-2.

## Technology Stack

- Python
- Gradio
- NumPy
- Pillow
- Planned: TensorFlow/Keras or PyTorch
- Planned deployment: Hugging Face Spaces

## System Flow

```text
Fundus Image Upload
        ↓
Image Quality Check
        ↓
Image Enhancement
        ↓
AI DR Severity Prediction
        ↓
Confidence Score and Explainability Map
        ↓
Referral Recommendation and Ophthalmologist Review
```

## Ethical and Safety Note

This prototype is intended only for educational and screening-workflow demonstration purposes. It is not a medical diagnosis system and must not replace an ophthalmologist’s clinical judgement.

## Dataset Plan

- APTOS 2019 Blindness Detection
- IDRiD: Indian Diabetic Retinopathy Image Dataset
- DRIVE: Digital Retinal Images for Vessel Extraction
- Messidor-2

## Team Members

- Your Name — Team Lead / Developer
- Team Member 2 — Role
- Team Member 3 — Role
- Team Member 4 — Role

## Links

- GitHub Repository: Add your repository link here
- Live Demo: To be added after Hugging Face deployment
- Demo Video: Optional / To be added
