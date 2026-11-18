"""Воронка: анализ чата -> лид -> портрет клиента -> холодный контакт."""
import json, os, re
from dotenv import load_dotenv
import google.generativeai as genai
from prompts import LEAD_PROMPT, PROFILE_PROMPT, COLD_PROMPT

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.0-flash")

def ask(prompt: str) -> str:
    return model.generate_content(prompt).text.strip()

def parse_json(text: str) -> dict:
    text = re.sub(r"^```(?:json)?|```$", "", text.strip(), flags=re.M).strip()
    return json.loads(text)

def run():
    chats = json.load(open("data/chats.json", encoding="utf-8"))
    results = []
    for c in chats:
        lead = parse_json(ask(LEAD_PROMPT + c["chat"]))
        row = {"id": c["id"], "lead": lead}
        if lead.get("is_lead") and lead.get("score", 0) >= 60:
            profile = parse_json(ask(PROFILE_PROMPT.replace("{chat}", c["chat"]).replace("{lead}", json.dumps(lead, ensure_ascii=False))))
            row["profile"] = profile
            row["cold_message"] = ask(COLD_PROMPT.replace("{profile}", json.dumps(profile, ensure_ascii=False)))
        results.append(row)
        print(f"[{c['id']}] lead={lead.get('is_lead')} score={lead.get('score')}")
    json.dump(results, open("results.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("Сақталды: results.json")

if __name__ == "__main__":
    run()
