# Guía de colaboración

## Flujo de ramas
- `main`: código estable (producción) NO TOCAR NADA EN MAIN.
- `develop`: rama de integración.
- `feature/<nombre>`: nuevas funcionalidades. Siempre salen desde `develop`.

## Roles

### Colaboradores
1. Crear una rama feature desde develop:
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b feature/nombre
   ```

2. Hacer commits en `feature/nombre`.

3. Subir la rama al remoto:
   ```bash
   git push origin feature/nombre
   ```

4. Abrir un **Pull Request** en GitHub de `feature/nombre` → `develop`.

---

### Líder del proyecto
1. Revisar y aceptar los PR de los colaboradores hacia `develop`.

2. Cuando todo en `develop` esté probado:
   ```bash
   git checkout main
   git pull origin main
   git merge develop
   git tag vX.Y
   git push origin main
   git push origin vX.Y
   ```

---

## Convenciones
- Usar nombres de ramas en inglés: `feature/notes`, `bugfix/login`, etc.
- Mensajes de commit claros y en presente: "Add notes API" en vez de "added".
