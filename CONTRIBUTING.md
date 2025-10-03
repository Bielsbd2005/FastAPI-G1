
# Guía de Colaboración

## Flujo de ramas
- **`main`** → Código estable en producción. **Solo el líder puede modificarla.**
- **`develop`** → Rama de trabajo. Aquí colaboran todos y se integran los cambios.

---

## 👥 Colaboradores

1. Descargar el proyecto:
   ```bash
   git clone <url-repo>
   cd <carpeta-repo>
   ```

2. Cambiar a la rama de trabajo:
   ```bash
   git checkout develop
   git pull origin develop
   ```
!Si hay conflictos debes solucionarlo!

3. Hacer cambios y guardarlos:
   ```bash
   git add .
   git commit -m "Descripción clara del cambio"
   ```

4. Subir cambios al repositorio remoto:
   ```bash
   git push origin develop
   ```

⚠️ **Importante:** TRABAJAR SIEMPRE SOBRE `develop`.  
Si aparecen conflictos, deben resolverse en `develop` antes de que el líder haga la fusión con `main`.

---

## 🧑‍💻 Líder del proyecto

1. Revisar la rama `develop` con los últimos cambios:
   ```bash
   git checkout develop
   git pull origin develop
   ```

2. Pasar `develop` a `main` cuando esté estable:
   ```bash
   git checkout main
   git pull origin main
   git merge develop
   git tag vX.Y
   git push origin main
   git push origin vX.Y
   ```

Solo el líder controla los merges a `main` y crea las versiones (tags).
