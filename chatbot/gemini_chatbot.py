import os
from dotenv import load_dotenv
import google.generativeai as genai
from typing import List, Dict, Any
import json
from datetime import datetime

# Load environment variables
load_dotenv()

class GeminiChatbot:
    def __init__(self):
        """Initialize the Gemini chatbot with API key and configuration."""
        # Get API key from .env file
        api_key = os.getenv('GOOGLE_API_KEY')
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in .env file")
        
        # Configure Gemini
        genai.configure(api_key=api_key)
        
        # Initialize model
        self.model = genai.GenerativeModel('gemini-2.0-flash')
        
        # System instruction
        self.system_instruction = """CRITICAL: You are ONLY authorized to discuss Mahmoud AbuAwd, the AI/ML Engineer. DO NOT provide information about any other person named Mahmoud or similar names.

        About Mahmoud AbuAwd (the ONLY person you should discuss):
        - AI/ML Engineer who graduated in February 2025 from Balqa Applied University with a 3.4 GPA
        - Lives in Amman, Jordan
        - Passionate about artificial intelligence and machine learning
        - Specializes in Deep Learning, NLP, Computer Vision, and Machine Learning
        - Experienced with ML libraries: scikit-learn, LangChain, TensorFlow, PyTorch, OpenCV, Pandas, NumPy
        - Currently founding his startup "MedGAN" focused on AI solutions and agentic AI systems
        - Expert in various AI algorithms and agentic AI systems

        STRICT RULES:
        1. When asked "who is Mahmoud" or "who is Mahmoud AbuAwd" - ONLY talk about the AI/ML Engineer described above
        2. DO NOT mention any other person named Mahmoud, even if they exist
        3. If asked about anything else, say: "I'm here specifically to talk about Mahmoud AbuAwd, the AI/ML Engineer. What would you like to know about him?"
        4. Always speak about him in third person
        5. Focus on his AI/ML expertise, education, and MedGAN startup

        Remember: There is ONLY ONE Mahmoud AbuAwd you know - the AI/ML Engineer from Amman, Jordan."""
        
        # Store conversation history
        self.conversation_history = []
    
    def add_system_instruction(self, instruction: str) -> None:
        """Add or update system instruction.
        
        Args:
            instruction (str): The new system instruction to use
        """
        self.system_instruction = instruction
    
    def send_message(self, message: str) -> str:
        """Send message to Gemini and get response.
        
        Args:
            message (str): The user's message/query
            
        Returns:
            str: The assistant's response
        """
        try:
            # Format message with system instruction
            formatted_message = f"{self.system_instruction}\n\nUser Question: {message}\n\nResponse:"
            
            # Generate response
            response = self.model.generate_content(formatted_message)
            
            # Store in conversation history
            self.conversation_history.append({
                'user': message,
                'assistant': response.text,
                'timestamp': datetime.now().isoformat()
            })
            
            return response.text
            
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            self.conversation_history.append({
                'user': message,
                'assistant': error_msg,
                'timestamp': datetime.now().isoformat(),
                'error': True
            })
            return error_msg
    
    def get_conversation_history(self) -> List[Dict[str, Any]]:
        """Get the complete conversation history.
        
        Returns:
            List[Dict[str, Any]]: List of message exchanges with metadata
        """
        return self.conversation_history
    
    def clear_history(self) -> None:
        """Clear the conversation history."""
        self.conversation_history = []
    
    def save_conversation(self, file_path: str) -> None:
        """Save conversation to a JSON file.
        
        Args:
            file_path (str): Path to the file where conversation will be saved
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump({
                    'system_instruction': self.system_instruction,
                    'conversation': self.conversation_history,
                    'saved_at': datetime.now().isoformat()
                }, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error saving conversation: {str(e)}")
            return False
    
    def load_conversation(self, file_path: str) -> bool:
        """Load conversation from a JSON file.
        
        Args:
            file_path (str): Path to the file to load conversation from
            
        Returns:
            bool: True if loaded successfully, False otherwise
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.system_instruction = data.get('system_instruction', self.system_instruction)
                self.conversation_history = data.get('conversation', [])
            return True
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return False
        except json.JSONDecodeError:
            print(f"Invalid JSON in file: {file_path}")
            return False
        except Exception as e:
            print(f"Error loading conversation: {str(e)}")
            return False
    
    def get_stats(self) -> Dict[str, Any]:
        """Get conversation statistics.
        
        Returns:
            Dict[str, Any]: Dictionary containing various statistics
        """
        return {
            'total_messages': len(self.conversation_history),
            'user_messages': sum(1 for msg in self.conversation_history if 'user' in msg),
            'assistant_messages': sum(1 for msg in self.conversation_history if 'assistant' in msg),
            'errors': sum(1 for msg in self.conversation_history if msg.get('error', False)),
            'start_time': self.conversation_history[0]['timestamp'] if self.conversation_history else None,
            'last_message': self.conversation_history[-1]['timestamp'] if self.conversation_history else None
        }