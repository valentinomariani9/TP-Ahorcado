from selenium import webdriver

def before_all(context):
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # si querés que no se abra la ventana
    options.add_argument("--window-size=1920,1080")
    context.driver = webdriver.Chrome(options=options)
    context.driver.implicitly_wait(3)

def after_all(context):
    context.driver.quit()