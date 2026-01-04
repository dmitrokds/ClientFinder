import logging

import ai_agent.create, ai_agent.schema, ai_agent.ask


async def main():
    await ai_agent.create.init(
        name = "searcher",
        prompts = ["""You are the best searcher of clients.
Your task is to find the best fit clients for company - you will be given with 'company description'.

Find customers based on the description - those are the best fir. You will be given with 'customer description'

In company(in site or external sources) you have to find a phone of the person described in 'target person'
If it is possible give a name of the writer

Give a descripition of the company - one or two sentence of the company that will give clearness of their products
And description why you selected it
Sort it by the most relevant companies

Search for phones that have telegram"""],
        schema = await ai_agent.schema.creating('''
            {
                "res": [{
                    "name": str,
                    "phone**": str,
                    "company**": str,
                    "website**": str,
                    "company_description**": str,
                    "why_description**": str,
                    "where_you_find_phone": str
                }]
            }'''
        ),
        google_search=True,
        thinking_level = "HIGH",
        model = "gemini-3-flash-preview"
    )
    
    
    
    await ai_agent.create.init(
        name = "personalizer",
        prompts = ["""You are a manager that needs to hook as many customers as possible.
                   
You will be given with with company name and url.

Also you have msg template - don't change anything except all that is in brackets - {here will be description what to write}

Your task is to change brackets with description to personalize message

The message has to be short and has to fit idealy to the context + has to be about idealy what was written in the description.
Do not overcomplicate - give the right straight forward message.

Give 10 suitable candidates"""],
        schema = await ai_agent.schema.creating('''
            {
                "res": str
            }'''
        ),
        google_search=True,
        thinking_level = "HIGH",
        model = "gemini-3-flash-preview"
    )
    print("models are created")
    
    
    
    company_description = """Мене звати Дмитро, я CEO ClarusBot
Ми впроваджуємо в компаніях AI-менеджера, який бере на себе клієнтську комунікацію: консультації, типові питання, супровід замовлення, повідомлення за сценаріями.
Для вас це означає менше ручної роботи, менше пропущених звернень і економія на операційних витратах."""

    customer_description = """Наш таргет люди які готові спробувати щось нове це може бути як магазин речей але вже з якимись інтеграціями але найідеальніший варіант це компанії з маленьким асортиментом товару і які мають багато лідів або питань"""
    
    target_person = "Шукаємо тих то зможе зразу закрити це питання та як умога швидше впровадити нашу систему тому шукай босів фопів абокогось головного"
    status, resp = await ai_agent.ask.init("searcher", f"""
Company Description: {company_description}

Customer Description: {customer_description}

Target person: {target_person}
""")
    print(resp)
    
    
    
import asyncio
if __name__ == "__main__":
    logging
    asyncio.run(main())