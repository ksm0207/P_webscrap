from indeed import extract_indeed_pages, extract_indeed_jobs

# 페이지의 가장 큰 숫자는 18을 나타냅니다
max_indeed_pages = extract_indeed_pages()

# 페이지의 가장 큰 숫자를 받아 18번동안 작동합니다
indeed_jobs = extract_indeed_jobs(max_indeed_pages)
