# ipv-sistemas-Informacao-empresariais

## Criar pacote de ficheiros addon
```bash
docker compose exec -u root odoo \
  odoo scaffold martche_custom /mnt/extra-addons
```


## Restart Docker
```bash
  docker compose restart odoo
```