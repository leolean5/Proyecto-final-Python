### Caso de Prueba 1: Registro de Usuario

**Objetivo:**
Verificar que los usuarios puedan registrarse correctamente con un nombre de usuario, correo electrónico y contraseña válidos.

**Pasos para Reproducir:**
1. Navegar a la página de registro: `/accounts/register/`.
2. Ingresar los siguientes datos en el formulario:
   - Nombre de usuario: `usuario_prueba`
   - Correo electrónico: `usuario@prueba.com`
   - Contraseña: `contraseña123`
   - Confirmación de contraseña: `contraseña123`
3. Hacer clic en el botón "Registrarse".
4. Confirmar que aparece el mensaje: "¡Tu cuenta ha sido creada, usuario_prueba! Ya puedes iniciar sesión."
5. Verificar que el usuario sea redirigido correctamente a la página de inicio de sesión.

**Resultado Esperado:**
El usuario es registrado exitosamente, se muestra el mensaje de confirmación y se redirige a la página de inicio de sesión.

---

### Caso de Prueba 2: Edición de Perfil

**Objetivo:**
Verificar que un usuario registrado pueda actualizar correctamente su información de perfil.

**Pasos para Reproducir:**
1. Iniciar sesión con un usuario existente.
2. Navegar a la página de edición de perfil: `/accounts/profile/edit/`.
3. Modificar los siguientes campos del formulario:
   - Nombre: `Nombre Editado`
   - Apellido: `Apellido Editado`
   - Correo Electrónico: `nuevo_correo@ejemplo.com`
4. Hacer clic en el botón "Guardar Cambios".
5. Confirmar que aparece el mensaje: "¡Tu perfil ha sido actualizado con éxito!"

**Resultado Esperado:**
Los cambios realizados en el perfil se guardan correctamente y se muestra un mensaje de confirmación.

---

### Caso de Prueba 3: Creación de una Publicación en el Blog

**Objetivo:**
Verificar que un usuario autenticado pueda crear una publicación en el blog.

**Pasos para Reproducir:**
1. Iniciar sesión con un usuario registrado.
2. Navegar a la página de creación de publicaciones: `/crear/`.
3. Ingresar los siguientes datos en el formulario:
   - Título: `Título de Prueba`
   - Subtítulo: `Subtítulo de Prueba`
   - Contenido: `Este es el contenido de prueba de la publicación.`
   - Imagen: Seleccionar una imagen válida desde el dispositivo.
4. Hacer clic en el botón "Crear".
5. Confirmar que la publicación aparece en la lista de publicaciones.

**Resultado Esperado:**
La publicación se crea correctamente, se almacena en la base de datos y aparece listada en la página principal del blog.

---
