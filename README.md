# 🤖 Multi-Page Chatbot App

A Streamlit application featuring **6 specialized chatbots**, each connected to the OpenAI API with multi-turn conversations using the responses endpoint.

## ✨ Features

- **🏠 Home Page** - Welcome and overview
- **💻 Coding Assistant** - Programming help and code reviews
- **✍️ Creative Writing** - Writing assistance and brainstorming
- **💼 Business Consultant** - Strategic advice and business insights
- **🌍 Language Tutor** - Language learning and practice
- **🏃 Health Coach** - Wellness guidance and health tips

## 🚀 Key Features

- **Multi-turn conversations** - Each chatbot maintains its own conversation history
- **Customizable system messages** - Modify AI behavior for each conversation
- **OpenAI API integration** - Uses GPT-5-nano model via the responses endpoint
- **Clean UI** - Modern, user-focused interface with emojis
- **Session management** - Separate chat histories for each page

## 📋 Requirements

- Python 3.8+
- OpenAI API key
- Required packages (see `requirements.txt`)

## 🛠️ Installation

1. **Clone or download** this repository
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your OpenAI API key:**
   - Create a `.env` file in the project root
   - Add your API key: `OPENAI_API_KEY=your_actual_api_key_here`

## 🚀 Running the App

1. **Start the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** and navigate to the displayed URL (usually `http://localhost:8501`)

3. **Choose a page** from the sidebar and start chatting!

## 🔧 Configuration

### Environment Variables
- `OPENAI_API_KEY` - Your OpenAI API key (required)
- `OPENAI_MODEL` - AI model to use (default: gpt-5-nano)
- `OPENAI_BASE_URL` - OpenAI API base URL (default: https://api.openai.com/v1)

### Customizing System Messages
Each chatbot page includes an expandable section where you can:
- View the current system message
- Modify the AI's behavior and expertise
- Clear conversation history when updating

## 📱 App Structure

```
app.py              # Main Streamlit application
chatbot.py          # Chatbot class with OpenAI integration
config.py           # Configuration and environment variables
requirements.txt    # Python dependencies
README.md           # This file
```

## 💡 Usage Tips

- **Start with the Home page** to see an overview of all features
- **Customize system messages** to tailor each chatbot's expertise
- **Use the sidebar** to navigate between different specialized assistants
- **Clear chat history** when switching topics or updating system messages
- **Each page maintains separate conversations** - perfect for different use cases

## 🔒 Security Notes

- Never commit your `.env` file to version control
- Keep your OpenAI API key secure and private
- The app loads API keys from environment variables for security

## 🐛 Troubleshooting

- **API Key Error**: Ensure your `.env` file contains a valid OpenAI API key
- **Import Errors**: Make sure all dependencies are installed with `pip install -r requirements.txt`
- **Connection Issues**: Check your internet connection and OpenAI API status

## 📈 Future Enhancements

- Stream responses for real-time chat experience
- File upload capabilities for document analysis
- Export conversation histories
- User authentication and conversation persistence
- Additional AI model options

---

**Happy Chatting! 🎉**
