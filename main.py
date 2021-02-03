from indeed import get_indeed_jobs
from stackoverflow import get_stackoverflow_jobs
from save import save_to_file

url_indeed = {
    'URL': "https://www.indeed.com/jobs",
    'options': [('limit', 50)]
}

url_stackoverflow = {
    'URL': "https://www.stackoverflow.com/jobs",
    'options': [('sort','i')]
}

def main():
    query = input('What do you want to query? ex: python\n')
    location = input('Where do you work at? ex: london\n')
    print(f'scrapping {query} job in {location}')

    websites = [url_indeed, url_stackoverflow]
    for website in websites:
        website['query'] = query
        website['location'] = location

    indeed_jobs = get_indeed_jobs(url_indeed)
    stackoverflow_jobs = get_stackoverflow_jobs(url_stackoverflow) 
    jobs = indeed_jobs + stackoverflow_jobs
    save_to_file(jobs)

if __name__ == "__main__":
    main()