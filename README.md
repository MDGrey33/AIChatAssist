# AIChatAssist - SlackBot-Powered Insights and AI Conversations

AIChatAssist is a cutting-edge solution designed to provide Slack users with the ability to easily retrieve key information from conversations and engage in intelligent, context-aware discussions using the latest relevant ChatGPT model. This tool offers seamless integration between Slack and AI-powered assistance to help users make better business decisions, stay informed, and collaborate more effectively.

## Key Features for Business Users

1. **Instant Slack Conversation Summaries**
    - **What It Does:** AIChatAssist allows users to query Slack channels based on specific filters, such as time range and channel name, and retrieve a structured summary of key decisions and actions discussed within that time frame.
    - **Benefit:** No need to sift through countless messages—get straight to the important decisions and topics that matter to your business.
    - **Example:** Simply request a summary of a conversation, and the bot will extract decisions, discussions, and action items to keep you informed.

2. **AI-Powered Conversations for Deeper Insights**
    - **What It Does:** Using the latest relevant ChatGPT model, AIChatAssist engages with you to answer specific questions based on retrieved Slack data. Whether you’re looking for key decision-makers or clarifications, the bot provides detailed, AI-driven responses.
    - **Benefit:** Ask follow-up questions or clarify details without needing to go back and read through all the conversations. AIChatAssist provides precise, natural language answers.
    - **Example:** “Who approved this decision?” or “Was this discussed with the finance team?” The bot responds with relevant details instantly.

3. **Multi-Turn Conversations**
    - **What It Does:** AIChatAssist allows for continuous, multi-message conversations with the bot, allowing users to refine their queries and ask follow-up questions.
    - **Benefit:** Engage in a natural, conversational workflow where you can keep refining your requests until you get exactly the information you need.
    - **Example:** “What decisions were made?” followed by “Who was involved in approving the decision to add customer credit?” AIChatAssist maintains context and provides the answers without repeating earlier steps.

4. **Simple SlackBot Commands for Easy Access**
    - **What It Does:** AIChatAssist is controlled through simple SlackBot commands, making it easy for users to access conversation summaries, retrieve decision-making information, and engage with AI-powered insights.
    - **Benefit:** You don’t need to be an expert—just use the bot’s intuitive commands and start retrieving valuable insights from Slack with minimal effort.
    - **Example:** “/get-summary #sales-channel 01-01-2024 01-31-2024” provides a summary of the entire month of discussions in the sales channel.

5. **Secure and Reliable Slack Integration**
    - **What It Does:** AIChatAssist uses Slack OAuth authentication to ensure that only authorized users can access conversation data from specific channels. The app securely manages user tokens and permissions.
    - **Benefit:** You can trust that sensitive information is protected, and only the right users can access the appropriate Slack data.
    - **Example:** Each user must authenticate with their Slack account before querying channel information, ensuring data privacy and security.

## Getting Started

1. **Authenticate:** Begin by using the provided OAuth link to authenticate with your Slack workspace.
2. **Ask Questions:** Once authenticated, simply ask the bot for summaries or insights based on your business needs.
3. **Explore:** Use natural language queries to dive deeper into specific conversations and get AI-powered assistance in real time.

## Quickstart for Developers

This project is in early development. To get started, follow these steps:

1. **Clone the Repository:**
    ```sh
    git clone https://github.com/MDGrey33/AIChatAssist
    cd AIChatAssist
    ```

2. **Set Up the Environment with Poetry:**
    - Install [Poetry](https://python-poetry.org/docs/#installation) if you haven't already.
    - Install dependencies:
        ```sh
        poetry install
        ```

3. **Activate the Virtual Environment:**
    ```sh
    poetry shell
    ```

4. **Run the Application:**
    ```sh
    python main.py
    ```

### Project Structure

- **`main.py`**: The entry point of the application.
- **`bot/`**: Contains the core logic for the Slack bot, including command handling and message processing.
- **`config/`**: Configuration files and settings for the application.
- **`models/`**: AI models and related utilities.
- **`utils/`**: Helper functions and utilities used throughout the project.
- **`tests/`**: Unit tests and test cases to ensure the functionality of the application.

### Pre-commit Hooks and Testing

- **Pre-commit Hooks:** This project uses pre-commit hooks to ensure code quality. Your commits will only pass if all tests run successfully.
- **Testing Expectations:** Developers are expected to create new tests to cover their code or edit existing tests if changes were made to the code they cover.

To set up pre-commit hooks, run:
```sh
poetry run pre-commit install
```

By following these steps, you can set up the development environment and start contributing to AIChatAssist. Feel free to explore the codebase and understand the different components of the project.
