from bs4 import BeautifulSoup
from selenium import webdriver # módulo que contiene implementaciones de controladores de navegadores web
from webdriver_manager.chrome import ChromeDriverManager # controlador de Chrome  
from selenium.webdriver.support import expected_conditions as EC # método para escribir códigos que esperan hasta que ciertas condiciones sean cumplidas
from selenium.webdriver.support.ui import WebDriverWait # método para escribir códigos que utilizan esperas implícitas o explícitas
from selenium.webdriver.common.by import By # método para localizar elementos por sus atributos HTML
from selenium.webdriver import ActionChains # módulo para implementar interacciones con el navegador from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
#d = webdriver.Chrome('your-chrome-driver-path',chrome_options=chrome_options)

# Inicializa la página web en el navegador Chrome
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
url = 'https://www.despegar.com.co/'
driver.get(url) # aca le pido al webdriver que me traiga la pagina que le solicite en url

elemento_oferta = '.shifu-3-header .header-corners-container .header-product-item .shifu-3-button-circle.OFFERS'
delay = 10
try:
    element_present = EC.presence_of_element_located((By.CSS_SELECTOR, elemento_oferta))
    WebDriverWait(driver, delay).until(element_present)
except TimeoutError:
    print('Timed out waiting for page to load')
print(driver.current_url)

element1 = driver.find_element_by_css_selector(elemento_oferta)
ActionChains(driver).click(element1).perform()
print(driver.current_url)

soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

etiqueta_promociones = soup.select('slider-item')  # selecciona todos los elementos que tienen la clase slider-item

def chequear_nulo(etiqueta):
    if etiqueta is not None:
        return etiqueta.text

def chequear_imagen(etiqueta):
    if etiqueta is not None:
        return etiqueta['src']

for etiqueta in (etiqueta_promociones):
    titulo = etiqueta.select_one('.offer-card-title.small-title ')
    imagen = etiqueta.select_one('.offer-card-image .offer-card-image-main')
    categoria = etiqueta.select_one('.offer-card-product')
    precio_oferta = etiqueta.select_one('.offer-card-pricebox-price-amount ')
    precio_normal = etiqueta.select_one('.offer-card-pricebox-price .offer-card-pricebox-price-old')
    print(chequear_nulo(titulo), chequear_imagen(imagen), chequear_nulo(categoria), chequear_nulo(precio_oferta), chequear_nulo(precio_normal))
