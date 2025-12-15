1. Project Overview

This project is a Pinterest Money Assistant designed to help users research trending niches, generate pin content, and create monetization strategies.
The agent analyzes user goals, suggests profitable ideas, and returns content in a clear, structured format.

The goal of this project is to practice:

Prompt engineering

AI workflow design

Python + API integration

Building a small but useful GenAI tool
2. Project Objectives

The Pinterest Money Assistant will:

Identify profitable niches based on the user’s interests or target audience.

Generate keywords that match Pinterest search behavior.

Produce high-quality pin titles and descriptions that are SEO-optimized.

Suggest monetization angles such as affiliate marketing, digital products, or blog traffic.

Follow a consistent structured format for every response.

Guide the user step-by-step and ask clarifying questions when needed.

These objectives ensure the agent remains helpful, consistent, and aligned with the user’s goals.
3. System Architecture

The Pinterest Money Assistant is built using a simple but clear structure:

3.1 Components

1. Prompt Files (/prompts)

system_prompt.txt → Defines the AI’s personality and role

instructions.txt → Step-by-step instructions the AI must follow

example_prompts.txt → Example interactions that train the agent’s behavior

2. Python Application (main.py)
Handles:

Reading prompt files

Sending user queries to the OpenAI API

Formatting and displaying the AI response

3. Configuration (.env)
Stores:

API keys

Environment variables
This keeps sensitive data outside the main code.

3.2 Data Flow

User enters a request in the terminal

Python loads:

system prompt

instructions

examples

These are combined into one big prompt

The request is sent to the OpenAI API

API returns formatted output

Output is displayed to the user

3.3 Why This Architecture

Keeps prompts organized

Easier to maintain

Clean separation of AI logic and Python code

Safe handling of API keys

Easy to expand later (CSV export, UI, etc.)
4. Features & Functionality
4.1 Core Features

The Pinterest Money Assistant will provide:

Niche Research

Suggest profitable, trending, or high-demand topics

Tailored to a Kenyan or global audience

Keyword Generation

5–10 Pinterest-relevant keywords

SEO-friendly and based on user input

Pin Title Creation

3 optimized title options

Designed for high click-through rates

Pin Description Writing

1–2 high-quality descriptions

Keyword-rich and audience-targeted

Monetization Suggestions

Affiliate products

Digital downloads

Blog or website traffic ideas

Pinterest strategy recommendations

4.2 Optional Add-On Features (future upgrades)

These can be added later if the assignment allows:

CSV export of results

Save user queries

Batch processing (multiple niches at once)

GUI or web interface

Pinterest SEO score system

4.3 User Interaction Flow

User describes what they want (e.g., “Give me a niche for beauty and skincare”).

The AI follows the instructions to:

Analyze the request

Generate insights

Return formatted results

If unclear, the AI asks a clarifying question.
5. Prompt Design Strategy

The agent uses a multi-prompt architecture, meaning several files combine to shape the model’s behavior.

5.1 System Prompt

Defines:

Role

Personality

Style

Output format

This ensures consistent behavior across different user requests.

5.2 Instructions Prompt

Defines:

Step-by-step workflow

Mandatory output elements (keywords, titles, descriptions)

Clarifying question rules

Formatting requirements

This creates predictable, structured results.

5.3 Example Prompts

Shows the AI:

How users ask questions

How the agent should respond

Expected tone and clarity

These examples “train” the agent through few-shot prompting.

5.4 Prompt Combination

During runtime:

system_prompt.txt

instructions.txt

example_prompts.txt

user_input

Are merged into one large prompt before being sent to the model.

6. User Experience Flow
6.1 Starting the Tool

User runs:

python3 main.py

6.2 Interaction Flow

Program displays a welcome message

User types a goal or question

AI analyzes the request

AI returns:

Summary

Keywords

Pin titles

Description

Monetization ideas

6.3 Clarity & Safety

If the user input is unclear → Ask one clarifying question

Avoid hallucinations

Keep language simple and helpful

6.4 Ending the Session

User types:

exit


or

quit

7. Technical Requirements
7.1 Software

Python 3.10+

Ubuntu (WSL) or Linux

VS Code or Nano

7.2 Libraries

Installed via pip:

openai

python-dotenv

requests (optional if needed)

7.3 Project Structure
MyGenAIProject/
│
├── main.py
├── plan.md
├── .env
│
└── prompts/
    ├── system_prompt.txt
    ├── instructions.txt
    └── example_prompts.txt

7.4 API Keys

Stored in .env:

OPENAI_API_KEY=xxxxxxxx


Not committed to git or shared publicly.

8. Evaluation Criteria

Your project will be graded based on:

8.1 Prompt Quality

Clear system identity

Strong instructions

Helpful examples

Predictable structure

8.2 Code Functionality

Python executes without errors

Prompts load correctly

AI returns structured output

8.3 Output Quality

Keywords are relevant

Titles are optimized

Descriptions are Pinterest-ready

Monetization ideas make sense

8.4 Documentation

Complete plan.md

Good architecture explanation

Easy to understand

9. Limitations & Future Improvements
Current Limitations

Only works through command line

No GUI

Results depend heavily on the prompt quality

No long-term memory

Future Improvements

Add a web UI (Flask or Streamlit)

Save results to CSV

Add batch niche generation

Pinterest SEO score analyzer

Auto-posting (long-term stretch goal)

10. Conclusion

The Pinterest Money Assistant is a lightweight but powerful GenAI project that demonstrates:

Prompt engineering

AI workflow design

API integration

Practical real-world use case

This project helps users create money-making Pinterest content through structured, personalized, and clear AI-generated insights.
The architecture is simple, modular, and easy to extend in future versions.
