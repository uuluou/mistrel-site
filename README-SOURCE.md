# parvel source

Lancer :
  ADMIN_TOKEN=un_bon_secret_ici npm install && node server.js
  admin : /admin.html (même token)

Sans ADMIN_TOKEN le serveur ne démarre pas.

server.js : backend express + sqlite
public/ : le site. Images dans public/assets/
products.json, site.json : données de départ
build_pages.py : régénère les pages (python3 build_pages.py)

Images non incluses dans l'archive. Les mettre dans public/assets/.
