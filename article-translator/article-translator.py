from openai import OpenAI

client = OpenAI(api_key='')

# get article; at the moment chatgpt is not able to pull from a link
article = "Pferdsbach ist ein ehemaliges Dorf im Gebiet der heutigen Stadt Büdingen im Wetteraukreis und lag in der Gemarkung des heutigen Stadtteils Dudenrod. Über Jahrhunderte lebten und arbeiteten dort Menschen. Armut und Not trieben die Einwohner jedoch 1847 fast geschlossen zur Auswanderung nach Pittsburgh in Nordamerika. Dem voraus gingen lange Verhandlungen, die nötige Klärung der offenen Vermögensfragen und des Verkaufs der vollständigen Gemeinde mit Äckern, Wiesen und Waldflächen, Häusern und Scheunen sowie die Klärung bestehender Rechte und Pflichten. Zurück blieb eine Wüstung. Auf die ehemaligen Gebäude deutet nichts mehr hin, lediglich Reste des Friedhofs und ein Gedenkstein erinnern an die Gemeinde und die Menschen, die dort lebten."

# prompt
prompt = f"Translate the folowing article: {article}"

# translate article
def article_translator(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role":"user", "content":prompt},
                  {"role":"assistant", "content":"Your are a professional translator. You translate new articles into english"},
                  {"role":"system", "content":"Direct english translator"}],
        temperature=.1 # low to not have creativity
    )
    return response.choices[0].message.content

print(article_translator(prompt))