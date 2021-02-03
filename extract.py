import requests
from bs4 import BeautifulSoup

def get_full_URL(URL):

    targetURL = f"{URL['URL']}?q={URL['query']}&l={URL['location']}"
    for option, value in URL['options']:
        targetURL+=f"&{option}={value}"

    return targetURL

def get_page(URL):
    full_URL = get_full_URL(URL)
    
    result = requests.get(full_URL)
    soup = BeautifulSoup(result.text,'html.parser')
    return soup

def get_last_page(page,website):

    def get_pagination():
        if website=='stackoverflow':
            pagination = page.find('div', {"class": "s-pagination"})
        if website=='indeed':
            pagination = page.find('div', {"class": "pagination"})
        return pagination

    def get_pages():
        pages = []
        if website=='stackoverflow':
            for link in links[:-1]:
                pages.append(link.get_text().strip())
        if website=='indeed':
            for link in links[:-1]:
                pages.append(link.string)
        return pages

    pagination = get_pagination()
    links = pagination != None and pagination.find_all('a')
    pages = get_pages()
    
    return int(pages[-1])

def extract_job(job_card, website):

    def get_title():
        if website=='stackoverflow':
            return job_card.find('a',{'class':'s-link stretched-link'})['title']
        if website=='indeed':
            return job_card.find('h2',{"class":"title"}).find('a')['title']

    def get_company():
        if website=='stackoverflow':
            company = job_card.find('h3',{'class':"fc-black-700 fs-body1 mb4"})
            if company.find('span').string is not None: company = company.find('span').string.strip()
            return company
        if website=='indeed':
            company = job_card.find("span",{"class":"company"})
            if company.find('a') is not None: company = company.find('a')
            return company.string.strip()

    def get_location():
        if website=='stackoverflow':
            return job_card.find('h3',{'class':"fc-black-700 fs-body1 mb4"}).find('span',{"class":"fc-black-500"}).string.strip()
        if website=='indeed':
            return job_card.find('div', {'class':'recJobLoc'})['data-rc-loc']

    def get_job_link():
        if website=='stackoverflow':
            job_id = job_card['data-jobid']
            return f"https://stackoverflow.com/jobs/{job_id}"

        if website=='indeed':
            job_id = job_card['data-jk']
            return  f"https://www.indeed.com/viewjob?jk={job_id}"
            
        
    title = get_title()
    company = get_company()
    location = get_location()
    job_link = get_job_link()

    return {'title':title, 'company':company, 'location':location, 'link':job_link}

def extract_jobs(URL, last_page,website):
    def get_request():
        if website=='indeed':
            return requests.get(f"{fullURL}&start={page*limit}")
        if website=='stackoverflow':
            return requests.get(f"{fullURL}&pg={page+1}")

    def get_jobcards():
        if website=='indeed':
            return soup.find_all('div', {"class": "jobsearch-SerpJobCard"})
        if website=='stackoverflow':
            return soup.find_all('div', {"class": "-job"})

    jobs = []

    fullURL= get_full_URL(URL)
    limit = 50

    for page in range(last_page):
        print(f"Scrapping {website}: Page: {page+1}/{last_page}")
        result = get_request()
        soup = BeautifulSoup(result.text,'html.parser')

        job_cards = get_jobcards()

        
        for job_card in job_cards:
            jobs.append(extract_job(job_card,website))

    return jobs