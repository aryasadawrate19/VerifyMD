# VerifyMD

VerifyMD is an AI-powered medical image analysis tool that helps healthcare professionals verify their diagnostic decisions. The application uses Google's Gemini Pro model to analyze medical images and provide detailed, structured reports.

## 🚀 Features

- Medical image analysis using Google's Gemini Pro model
- Support for multiple image formats (JPG, JPEG, PNG, DICOM)
- Structured analysis report including:
  - Image type and region identification
  - Detailed key findings
  - Diagnostic assessment with confidence levels
  - Patient-friendly explanations
- User-friendly web interface built with Streamlit

## ⚠️ Disclaimer

This tool is for educational and informational purposes only. All analyses should be reviewed by qualified healthcare professionals. Do not make medical decisions based solely on this analysis.

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/aryasadawrate19/VerifyMD.git
cd VerifyMD
```

2. Install dependencies using the requirements file:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the project root and add your Google API key:
```
GOOGLE_API_KEY=your_api_key_here
```

## 🚀 Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the provided local URL (typically `http://localhost:8501`)

3. Upload a medical image using the file uploader

4. Click the "Analyze Image" button to receive the AI-powered analysis

## 📝 Analysis Report Structure

The analysis includes:

1. **Image Type & Region**
   - Imaging modality identification
   - Anatomical region and positioning
   - Image quality assessment

2. **Key Findings**
   - Systematic observations
   - Abnormality descriptions
   - Measurements and densities
   - Severity ratings

3. **Diagnostic Assessment**
   - Primary diagnosis with confidence level
   - Differential diagnoses
   - Evidence-based support
   - Critical findings

4. **Patient-Friendly Explanation**
   - Simplified explanations
   - Clear definitions
   - Visual analogies
   - Common concerns addressed

## 🔧 Technical Stack

- Frontend: Streamlit
- AI Model: Google Gemini Pro via LangChain
- Image Processing: PIL (Python Imaging Library)
- Environment Management: python-dotenv

## 📄 License

This project is intended for educational and research purposes only. Not for clinical use.

## 👥 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.
