from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

facts = {
    1: {
        "fact": "The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion of the iron.",
        "detail": "The Eiffel Tower, an iconic symbol of Paris, is made mostly of iron. When temperatures rise during the summer, the metal expands, causing the tower to grow in height by up to 15 cm. This phenomenon is known as thermal expansion."
    },
    2: {
        "fact": "Honey never spoils; archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.",
        "detail": "Honey's unique composition, including low water content and natural acidity, creates an environment that inhibits the growth of microorganisms. This allows honey to remain preserved for long periods. Archaeologists have indeed discovered pots of honey in ancient Egyptian tombs that are still edible after over 3,000 years."
    },
    3: {
        "fact": "A group of flamingos is called a flamboyance.",
        "detail": "Flamingos, known for their vibrant pink coloration and long necks, often gather in large groups. These groups are called a flamboyance, which is a fitting term given the flamboyant display of color and grace these birds exhibit when they congregate."
    },
    4: {
        "fact": "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes.",
        "detail": "The Anglo-Zanzibar War holds the record for being the shortest war in history. It lasted for only 38 minutes, starting at 9:02 AM and ending at 9:40 AM on August 27, 1896. The conflict arose when the Sultan of Zanzibar died, and a successor was declared without British approval. British forces swiftly defeated the Zanzibari defenders, leading to a quick surrender."
    },
    5: {
        "fact": "Cows have best friends and can become stressed when separated from them.",
        "detail": "Cows are social animals that form strong bonds with other cows, especially within their herd. Research has shown that cows can have 'best friends' among other cows and develop close relationships with specific individuals. When separated from their preferred companions, cows can experience stress and exhibit behaviors indicative of distress."
    }
}

# getting all fact
@app.get('/')
def index():
    return facts

# getting fact using id
@app.get('{fact_id}')
def get_facts(fact_id : int):
    return facts[fact_id]

# getting fact
@app.get('{fact_id}/fact')
def get_facts(fact_id : int):
    return facts[fact_id]['fact']

# getting detail
@app.get('{fact_id}/detail')
def get_facts(fact_id : int):
    return facts[fact_id]['detail']

# add fact
class Fact(BaseModel):
    fact : str
    detail : str

@app.post('/create_fact/{fact_id}')
def create_student(fact_id: int, fact: Fact):
    if fact_id in facts:
        return {"Error" : "Id already exist"}

    facts[fact_id] = fact
    return facts[fact_id]