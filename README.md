Test task

Pytest suite:
- docker-compose up -d --build
- docker-compose exec web pytest tests/

Performance suite:
- docker-compose up -d --build
- locust -f performance/locust.py -u 5 -r 10 -t 200s --headless --print-stats --logfile locust_report.log --html locust_html.html