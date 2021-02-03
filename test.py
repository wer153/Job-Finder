def get_full_URL(URL):

    targetURL = f"{URL['URL']}?q={URL['query']}"
    for option, value in URL['options']:
        targetURL+=f"&{option}={value}"

    return targetURL

url_indeed = {
    'URL': "https://www.indeed.com/jobs",
    'query': 'python',
    'options': [('limit', 50)]
}


print(get_full_URL(url_indeed))