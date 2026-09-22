import gradio as gr
import numpy as np

CLASSES = [
    "No DR",
    "Mild NPDR",
    "Moderate NPDR",
    "Severe NPDR",
    "Proliferative DR"
]

def analyze_image(image):
    if image is None:
        return (
            "Please upload a retinal fundus image before clicking Analyze.",
            "No prediction",
            "0%"
        )

    image_array = np.array(image)

    # Prototype mode: UI demonstration.
    # Replace this with your trained and clinically validated DR model later.
    seed = int(image_array.mean() * 1000) % (2**32 - 1)
    rng = np.random.default_rng(seed)

    probabilities = rng.random(5)
    probabilities = probabilities / probabilities.sum()

    predicted_index = int(np.argmax(probabilities))
    predicted_class = CLASSES[predicted_index]
    confidence = float(probabilities[predicted_index] * 100)

    recommendations = {
        "No DR": "No DR is predicted. Continue annual diabetic eye screening.",
        "Mild NPDR": "Mild DR is predicted. Maintain blood-sugar control and repeat screening within 6 months.",
        "Moderate NPDR": "Moderate DR is predicted. Refer the patient to an ophthalmologist within 3 months.",
        "Severe NPDR": "Severe DR is predicted. Urgent ophthalmologist referral is recommended.",
        "Proliferative DR": "Potential proliferative DR is predicted. Immediate specialist review is recommended."
    }

    report = f"""
## Screening Report

**Predicted DR severity:** {predicted_class}

**Confidence score:** {confidence:.1f}%

**Recommendation:** {recommendations[predicted_class]}

---
### Important safety note
This is an educational prototype demonstrating the screening workflow. It is **not a medical diagnosis** and must be reviewed by a qualified ophthalmologist.
"""

    return report, predicted_class, f"{confidence:.1f}%"

with gr.Blocks(
    title="RetinaXplain — DR Screening",
    theme=gr.themes.Soft()
) as demo:

    gr.Markdown("""
# RetinaXplain

## Explainable AI for Diabetic Retinopathy Screening in Rural India

Upload a retinal fundus image to demonstrate the AI-assisted diabetic-retinopathy screening workflow.

**Workflow:** Upload image → AI screening result → Confidence score → Referral recommendation
""")

    with gr.Row():
        with gr.Column():
            image_input = gr.Image(
                label="Upload Retinal Fundus Image",
                type="pil",
                height=380
            )
            analyze_button = gr.Button(
                "Analyze Image",
                variant="primary",
                size="lg"
            )

        with gr.Column():
            report_output = gr.Markdown(
                value="## Waiting for image upload"
            )

    with gr.Row():
        severity_output = gr.Textbox(label="Predicted Severity")
        confidence_output = gr.Textbox(label="Confidence")

    analyze_button.click(
        fn=analyze_image,
        inputs=image_input,
        outputs=[report_output, severity_output, confidence_output]
    )

    gr.Markdown("""
---
### SIH 2026 | Problem Statement 26038

**Future clinical pipeline:** Image-quality assessment, enhancement, lesion segmentation, trained DR grading model, Grad-CAM explainability, calibrated confidence, and ophthalmologist review.
""")

demo.launch()
