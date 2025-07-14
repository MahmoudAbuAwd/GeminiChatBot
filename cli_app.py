from chatbot.gemini_chatbot import GeminiChatbot

def main():
    try:
        chatbot = GeminiChatbot()
        print("🤖 Gemini Chatbot initialized!")
        
        while True:
            user_input = input("\nYou: ").strip()
            
            if user_input.lower() == 'quit':
                break
                
            response = chatbot.send_message(user_input)
            print(f"\n🤖 Bot: {response}")
            
    except KeyboardInterrupt:
        print("\nChatbot stopped by user.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()