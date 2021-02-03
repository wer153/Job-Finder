from extract import get_page, get_last_page, extract_jobs

def get_indeed_last_page(url):
    page = get_page(url)
    last_page = get_last_page(page,'indeed')

    return last_page

def get_indeed_jobs(url):
    last_page = get_indeed_last_page(url)
    jobs = extract_jobs(url,last_page,'indeed')
    return jobs