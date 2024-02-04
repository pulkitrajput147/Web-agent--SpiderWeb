
from Agent1 import scrape_and_store_data
from Agent2 import QueryAnsweringAgent
import json
import openai


# Using Chatgpt for more Interactive Response
def generate_chatgpt_response(information):
    # Use ChatGPT to generate a more interactive response
    user_prompt = f"Tell me more about {information['company_name']}."
    chatgpt_response = openai.Completion.create(
        model="text-davinci-003",
        prompt=user_prompt,
        temperature=0.7,
        max_tokens=100
    )
    return chatgpt_response['choices'][0]['text']

def main():

    # Agent 1 - Data Scraping and Storage
    url = input("Enter the website URL: ")
    output_file = "scraped_data.json"
    scrape_and_store_data(url, output_file)

    # Agent 2 - Query Answering
    # Read data from the output file created by Agent 1
    try:
        with open(output_file, 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        print(f"Error: {output_file} not found. Please run Agent 1 to generate the file.")
        exit()

    # Initialize QueryAnsweringAgent with database name and collection name
    qa_agent = QueryAnsweringAgent(db_name="company_data_db", collection_name="company_collection")

    # Store data in the database
    qa_agent.store_data_in_database(data)

    # Answer user query
    user_query = input("Enter your query: ")
    results = qa_agent.answer_query(user_query)

    if results:
        for result in results:
            # Generate a more interactive response using ChatGPT
            chatgpt_response = generate_chatgpt_response(result)
            print(chatgpt_response)

    else:
        print("No matching results found.")

# Entry point for the program
if __name__ == "__main__":
    # Set your OpenAI GPT-3 API key
    openai.api_key = 'your-api-key'
    main()
