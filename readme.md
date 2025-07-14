# Gemini ChatBot

A simple yet powerful chatbot built using Google's Gemini 2.0 Flash model, with Streamlit for web deployment.

## Features

- Utilizes Google's Gemini 2.0 Flash model via API
- Customizable system instructions for tailored responses
- Easy-to-use Streamlit web interface
- Lightweight and fast implementation

## Prerequisites

Before you begin, ensure you have the following:

- Python 3.7 or higher
- A Google API key with access to Gemini models
- pip package manager

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MahmoudAbuAwd/GeminiChatBot.git
   cd GeminiChatBot
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Google API key:
   - Create a `.env` file in the project root
   - Add your API key:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

## Usage

### Running the Streamlit Web App

1. Launch the web application:
   ```bash
   streamlit run web_app.py
   ```

2. Open your browser and navigate to the local address provided (typically `http://localhost:8501`)

### Customizing System Instructions

Edit the `system_instruction` parameter in `web_app.py` to change the chatbot's behavior and personality.

## Configuration

The following configurations are available:

- **Model Selection**: Currently using Gemini 2.0 Flash (can be modified in code)
- **Temperature**: Adjusts response creativity (0.0 to 1.0)
- **Max Tokens**: Limits response length

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Google for the Gemini AI models
- Streamlit for the easy web deployment framework

## Contact

For questions or feedback, please contact [Mahmoud AbuAwd](https://github.com/MahmoudAbuAwd).
