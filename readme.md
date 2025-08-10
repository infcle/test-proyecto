# Test-Proyecto

Este proyecto contiene **pruebas automatizadas** para una aplicación web desarrolladas con **Selenium WebDriver** en Python. El objetivo es validar funcionalidades clave como login, gestión de productos y ventas, y filtrado de registros, asegurando la calidad del sistema de forma automatizada.

## Estructura del proyecto

```
test-proyecto/
│
├── config/
│   └── config.yml              # Configuración de entorno (URL, usuario, contraseña)
│
├── pages/                      # Page Objects (clases para interactuar con las páginas)
│
├── test/
│   ├── test_login.py           # Pruebas de login
│   ├── test_product.py         # Pruebas de productos
│   ├── test_venta.py           # Pruebas de ventas
│
├── utils/
│   ├── screenshot_utils.py     # Utilidad para capturas de pantalla
│   └── test_helpers.py         # Decoradores y helpers reutilizables
│
└── run_all_tests.py            # Script para ejecutar todos los tests
```

## Requisitos

- Python 3.8 o superior
- [Selenium](https://pypi.org/project/selenium/)
- Un navegador compatible (por ejemplo, Firefox)
- Geckodriver (para Firefox) o el driver correspondiente a tu navegador

Instala las dependencias con:

```sh
pip install selenium pyyaml
```

## Configuración

Edita el archivo `config/config.yml` con la URL base de tu aplicación y las credenciales de prueba:

```yaml
base_url: "http://localhost:8000"
username: "usuario@correo.com"
password: "tu_contraseña"
```

## Ejecución de pruebas

Puedes ejecutar cada test individualmente:

```sh
python test/test_login.py
python test/test_product.py
python test/test_venta.py
```

O ejecutar todos los tests automáticamente con:

```sh
python run_all_tests.py
```

Cada script abrirá el navegador, ejecutará la prueba y cerrará la ventana al finalizar.  
Las capturas de pantalla de los resultados y errores se guardan automáticamente en carpetas según el test.

## Personalización

- Puedes agregar o modificar los Page Objects en la carpeta `pages/`.
- Los helpers reutilizables y decoradores están en `utils/test_helpers.py`.
- Ajusta los selectores y flujos según la estructura real de tu aplicación web.

## Notas

- Si algún test falla, revisa las capturas de pantalla generadas para depurar el problema.
- Asegúrate de que el servidor de la aplicación esté corriendo antes de ejecutar los tests.
- Puedes adaptar los scripts para otros navegadores cambiando el driver en los archivos de test.

---

**Autor:**  
Elmer Coronel
Curso QA - Proyecto