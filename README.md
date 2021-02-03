# Job-Finder

# What it does? 

### scrapping job information in stackoverflow and indeed

# How do i use it?

### 1. run main.py

### 2. input what you want to query and where you want to work.

### 3. open jobs.csv and utilize scrapped information as you want.

# How does it work?

## extract.py

### 1. get_full_URL(URL): combine base URL with query, location and option(limit in indeed, sort in SO) into one full URL.

### 2. get_page(URL): parse HTML to text.

### 3. get_last_page(page, website): scrap pagination and return the last page.

### 4. extract_jobs(URL, last_page, website): scrape jobcards.

### 5. extract_job(job_card, website): scrape title, company, location, link.

## save.py

### save_to_file(jobs): convert jobs into csv(comma seperated values) file
