from extract import get_page, get_last_page, extract_jobs

def get_stackoverflow_last_page(url):
    page = get_page(url)
    last_page = get_last_page(page,'stackoverflow')

    return last_page

def get_stackoverflow_jobs(url):
    last_page = get_stackoverflow_last_page(url)
    jobs = extract_jobs(url,last_page,'stackoverflow')
    return jobs