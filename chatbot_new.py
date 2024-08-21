import nltk
import schedule
import time
from datetime import datetime

# Download required NLTK data
nltk.download('punkt')

# Predefined responses based on user input
responses = {
    "hello": "Hi! How can I assist you today?",
    "schedule": "What would you like to schedule?",
    "meeting": "I have scheduled your meeting.",
    "bye": "Goodbye! Have a nice day!"
}

def chatbot_response(user_input):
    """Generate a response based on user input."""
    words = nltk.word_tokenize(user_input.lower())
    for word in words:
        if word in responses:
            return responses[word]
    return "I'm not sure how to help with that."

def schedule_task(task_name, task_time):
    """Schedule a task at a specific time."""
    print(f"Task '{task_name}' scheduled for {task_time}")
    # Schedule the task
    schedule.every().day.at(task_time).do(lambda: print(f"Executing task: {task_name}"))

def main():
    """Main function to run the chatbot."""
    print("Chatbot is running... Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        
        if "schedule" in user_input.lower():
            task_name = input("What task would you like to schedule? ")
            task_time = input("At what time? (HH:MM) ")
            schedule_task(task_name, task_time)
        
        response = chatbot_response(user_input)
        print("Chatbot: " + response)
        
        if user_input.lower() == "bye":
            break
        
        # Run scheduled tasks
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
