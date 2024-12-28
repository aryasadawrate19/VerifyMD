from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os


def analyze_image(image_data_base64):
    """Analyze the medical image using ChatGoogleGenerativeAI."""
    # Load environment variables
    load_dotenv()
    query_content = [
        {"type": "text", "text": """
        You are a highly skilled medical imaging expert with extensive knowledge in radiology and diagnostic imaging. Analyze the patient's medical image and structure your response as follows:

        ### 1. Image Type & Region
        - Specify imaging modality (X-ray/MRI/CT/Ultrasound/etc.)
        - Identify the patient's anatomical region and positioning
        - Comment on image quality and technical adequacy

        ### 2. Key Findings
        - List primary observations systematically
        - Note any abnormalities in the patient's imaging with precise descriptions
        - Include measurements and densities where relevant
        - Describe location, size, shape, and characteristics
        - Rate severity: Normal/Mild/Moderate/Severe

        ### 3. Diagnostic Assessment
        - Provide primary diagnosis with confidence level
        - List differential diagnoses in order of likelihood
        - Support each diagnosis with observed evidence from the patient's imaging
        - Note any critical or urgent findings

        ### 4. Patient-Friendly Explanation
        - Explain the findings in simple, clear language that the patient can understand
        - Avoid medical jargon or provide clear definitions
        - Include visual analogies if helpful
        - Address common patient concerns related to these findings
        """},
        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_data_base64}"}},
    ]

    # Initialize the medical agent
    medical_agent = ChatGoogleGenerativeAI(model='gemini-1.5-pro', temperature=0.5)

    # Create HumanMessage and invoke the model
    message = HumanMessage(content=query_content)
    response = medical_agent.invoke([message])

    return response
