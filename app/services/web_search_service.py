from serpapi import GoogleSearch

API_KEY = "YOUR_API_KEY"   # 🔴 paste your key here

def search_google(query):
    params = {
        "q": query,
        "api_key": API_KEY,
        "num": 1
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    if "organic_results" in results:
        return results["organic_results"][0]

    return None