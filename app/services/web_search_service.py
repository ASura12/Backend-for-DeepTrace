from serpapi import GoogleSearch

API_KEY = "daf3016ef1e8ca81304ab4a3eb6f3ae97c5acfe92d973fd32ebe73f8ce0323cd"   # 🔴 paste your key here

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