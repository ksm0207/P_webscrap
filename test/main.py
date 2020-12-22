from indeed import get_jobs
from stackoverflow import stack_get_jobs
from save import save_to_file

stack_over = stack_get_jobs()
indeed_jobs = get_jobs()
jobs = stack_over + indeed_jobs  # 엑셀 시트에 넣을 변수 2개의 Array를 합침

# jobs를 파일로 저장함 --> 구글시트
save_to_file(jobs)
