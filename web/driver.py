#%%
from playwright.async_api import Browser, Locator, Page, async_playwright

from parsers import save

from .plat import is_docker

# Define the URL and user agent
headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36"}
user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Mobile/15E148 Snapchat/10.77.5.59 (like Safari/604.1)"
class PrigozhinSelenium:
    def __init__(self) -> None:
        self.url = "https://megamarket.ru/catalog/?q=моторное%20масло%205л"


    async def go_sber(self):
        self.playwright = await async_playwright().start()
        self.browser: Browser = await self.playwright.firefox.launch(headless=is_docker(), chromium_sandbox=False)
        return self
    
    async def create_context_page(self, proxy = None):
        context = await self.browser.new_context()
        self.page = await context.new_page()
        return self

    async def parse(self):
        page = self.page
        page.on("request", lambda request: print( 
	        ">>", request.method, request.url,
            request.resource_type)) 
        page.on("response", lambda response: print( 
	        "<<", response.status, response.url))
        await page.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())
        await page.goto(self.url)
        await page.wait_for_load_state("networkidle", timeout=30000)
        print(await page.title())
        mobs = await page.locator('.item-block').all()
        if len(mobs) == 0:
            print("Found 0 elements")
            raise IndexError
        print(f"Found {len(mobs)} items.")
        self.save_html(await self.page.content())
        return mobs        

    async def parse_loaded(self):
        mobs = await self.page.locator('.item-block').all()
        if len(mobs) == 0:
            print("Found 0 elements")
            raise IndexError
        print(f"Found {len(mobs)} items.")
        self.save_html(await self.page.content())
        return mobs
    
    def captcha(self):
        cpt = Captcha(self.page)
        return cpt
    
    def save_html(self, page: Page):
        with open('page.html', 'w') as f:
            f.write(page)
            print("Page saved!")
            save()

    async def grace_shutdown(self):
        print("Driver shutdown...")
        await self.browser.close()

class Captcha():
    def __init__(self, page: Page) -> None:
        self.captcha = page.locator("#captcha_image")
        self.field = page.locator("[name=captcha]")
        self.submit_btn = page.locator("[name=submit]")
        print("Captcha found!")
    
    async def screenshot(self, name = "test.png"):
        await self.captcha.screenshot(path=name)
        print(f"Captcha saved as {name}")
    
    async def send_keys_to_captcha(self, keys: str):
        await self.field.type(keys)
    
    async def submit(self):
        await self.submit_btn.click(timeout=10000)
        print("Captcha submitted")



# %%
