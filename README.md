Test task

Pytest suite:
- docker-compose up -d --build
- docker-compose exec web pytest tests/


Robot suite:
- docker-compose up -d --build
- robot -d robot_framework/logs robot_framework/


Performance suite:
- docker-compose up -d --build
- locust -f performance/locust.py -u 500 -r 10 -t 200s --headless --print-stats --logfile locust_report.log --html locust_html.html