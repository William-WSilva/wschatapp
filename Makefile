backup:
	docker exec -t container-wschatapp pg_dump -U wsilva -d wschatappdb > backups/initial_dump.sql
	cp backups/initial_dump.sql docker-entrypoint-initdb.d/initial_dump.sql
	git add backups/initial_dump.sql docker-entrypoint-initdb.d/initial_dump.sql
	
down: backup
	docker-compose down

