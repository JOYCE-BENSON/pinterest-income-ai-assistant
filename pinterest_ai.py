import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from openai import RateLimitError, AuthenticationError
from datetime import datetime

# --------------------------------------------
# 1. Load API Key
# --------------------------------------------
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("❌ ERROR: No API key found in .env file.")
    exit()

# --------------------------------------------
# 2. LLM Setup
# --------------------------------------------
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)

# --------------------------------------------
# 3. Prompt Templates
# --------------------------------------------

niche_prompt = PromptTemplate(
    input_variables=["interests"],
    template="""
You are a Pinterest marketing expert.
Based on the user's interests: {interests}

Generate 5–7 profitable Pinterest niche ideas.
For each niche, explain briefly:
- Why the niche is profitable
- Why it works well on Pinterest

Respond in clear bullet points.
"""
)

pin_prompt = PromptTemplate(
    input_variables=["niche"],
    template="""
You are a Pinterest SEO copywriter.

Generate 8–10 Pinterest pin ideas for the niche: {niche}
Include:
- Pin title
- Hook
- Call to action
"""
)

# --------------------------------------------
# 4. Helper Functions
# --------------------------------------------

def save_to_file(filename, content):
    os.makedirs("data", exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

# --------------------------------------------
# 5. AI Functions (with fallback mode)
# --------------------------------------------

def generate_niches(interests):
    prompt = niche_prompt.format(interests=interests)

    try:
        return llm.invoke(prompt).content

    except (RateLimitError, AuthenticationError):
        return """
⚠️ Demo Mode Activated (API unavailable)

Suggested Pinterest niches:
- Affiliate marketing for beginners
- Digital products & templates
- Passive income ideas
- Pinterest SEO & growth strategies
- Online business tools
"""

def generate_pins(niche):
    prompt = pin_prompt.format(niche=niche)

    try:
        return llm.invoke(prompt).content

    except (RateLimitError, AuthenticationError):
        return f"""
⚠️ Demo Mode Pins for: {niche}

1. How Beginners Can Start Affiliate Marketing on Pinterest
2. 5 Tools Every Pinterest Affiliate Marketer Needs
3. Step-by-Step Pinterest Pin Formula That Converts
4. Mistakes Killing Your Affiliate Pinterest Pins
5. How to Drive Traffic Without Paid Ads
"""

# --------------------------------------------
# 6. Main Program
# --------------------------------------------

def run():
    print("\n🟣 Welcome to the AI Pinterest Income Assistant!")
    print("-" * 50)

    interests = input("What are your niche interests? ")
    language = input("Preferred language (English/Swahili): ")
    pins_per_week = input("How many pins per week do you want to create? ")

    print("\n🔍 Generating profitable niches...\n")
    niches = generate_niches(interests)
    print(niches)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    niche_file = f"data/niches_{timestamp}.txt"
    save_to_file(niche_file, niches)

    print(f"\n💾 Niches saved to {niche_file}")

    chosen_niche = input("\nChoose one niche to generate pins for: ")

    print("\n📌 Generating Pinterest pin ideas...\n")
    pins = generate_pins(chosen_niche)
    print(pins)

    pins_file = f"data/pins_{timestamp}.txt"
    save_to_file(pins_file, pins)

    print(f"\n💾 Pins saved to {pins_file}")
    print("\n✅ Project completed successfully!")

# --------------------------------------------
# 7. Run App
# --------------------------------------------

if __name__ == "__main__":
    run()

