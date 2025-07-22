build:
	docker build -t whatsapp-bot .

run:
	docker run --env-file .env -p 5050:5050 whatsapp-bot

test:
	docker run --env-file .env -p 5050:5050 whatsapp-bot pytest  
