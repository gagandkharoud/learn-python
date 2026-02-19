import asyncio

# 1. 'async def' is just like 'async function'
async def fetch_ai_data(t):
    print("🤖 AI is thinking...")
    # 2. 'await asyncio.sleep' is like 'await new Promise(r => setTimeout(r, 2000))'
    await asyncio.sleep(t) 
    print(f"✅ AI is done!{t}")
    return {"response": "Success"}

async def main():
    print("Starting task...")
    # 3. Just like JS, you MUST 'await' an async function
    #result = await fetch_ai_data()
    #print(f"Result: {result}")
    # This starts BOTH at the same time
    results = await asyncio.gather(fetch_ai_data(2), fetch_ai_data(4))
    print(results)

# 4. This is the only "weird" part. 
# You have to tell Python to 'run' the top-level async function.
asyncio.run(main())