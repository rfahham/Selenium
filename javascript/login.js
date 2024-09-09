const { Builder, By, until } = require(`selenium-webdriver`);
const chrome = require(`selenium-webdriver/chrome`);

const options = new.options();
options.addArguments('--disable-extensions');
options.addArguments('--disable-popup-blocking');
options.addArguments('--disable-infobars');

const driver = new Builder()
    .forBrowser('chrome')
    .setChromeOptions(options)
    .build();

describe('Login Teste', () => {
    it('must be able to log in to the system with a valid user', async () => {
        await driver.get('site');
        await driver.findElement(by.id('username')).sendkeys('myusername');
        await driver.findElement(by.id('password')).sendkeys('mypassword');
        await driver.findElement(by.id('submit')).click();
        await driver.await(until.urlContains('/dashboard'), 5000); 
    })
})

after(async () => {
    await driver.quit();
});