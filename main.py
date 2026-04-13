import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message, InlineKeyboardButton, InlineKeyboardMarkup, InlineQuery

API_TOKEN = "8779937766:AAHE5LPk10Oei3Cyg01Z9r0xdgmu6l-ejro"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

telefon = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Galaxy Air Pods"), KeyboardButton(text="Galaxy Qo'l soati")],
        [KeyboardButton(text="Galaxy Planshet"), KeyboardButton(text="Galaxy Smartfon")],
        [KeyboardButton(text="orqaga")],
    ],
    resize_keyboard=True
)

Galaxy_Watch= InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Galaxy Watch8 Classic", callback_data="Galaxy Watch8 Classic")],
        [InlineKeyboardButton(text="Galaxy Watch8", callback_data="Galaxy Watch8")],
        [InlineKeyboardButton(text="Galaxy Watch7 Bluetooth", callback_data="Galaxy Watch7 Bluetooth")],
        [InlineKeyboardButton(text="Boshqa Galaxy qo'l soatlar", callback_data="Boshqa Galaxy qo'l soatlar")],
 ] )

Galaxy_Smartfon= InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Galaxy A57 5G", callback_data="Galaxy A57 5G")],
        [InlineKeyboardButton(text="Galaxy S25 FE", callback_data="Galaxy S25 FE")],
        [InlineKeyboardButton(text="Galaxy S26 Ultra", callback_data="Galaxy S26 Ultra")],
        [InlineKeyboardButton(text="Boshqa Galaxy Smartfonlar", callback_data="Boshqa Galaxy Smartfonlar")],
 ] )

Galaxy_Planshet= InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Galaxy Tab S11 Ultra 5G", callback_data="Galaxy Tab S11 Ultra 5G")],
        [InlineKeyboardButton(text="Galaxy Tab S10 Lite Wi-Fi", callback_data="Galaxy Tab S10 Lite Wi-Fi")],
        [InlineKeyboardButton(text="Galaxy Tab A11+", callback_data="Galaxy Tab A11+")],
        [InlineKeyboardButton(text="Boshqa Galaxy Planshetlar", callback_data="Boshqa Galaxy Planshetlar")],
 ] )

Galaxy_Pods= InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Galaxy Buds4", callback_data="Galaxy Buds4")],
        [InlineKeyboardButton(text="Galaxy Buds3 FE", callback_data="Galaxy Buds3 FE")],
        [InlineKeyboardButton(text="Galaxy Buds Core", callback_data="Galaxy Buds Core")],
        [InlineKeyboardButton(text="Boshqa Galaxy Podslar", callback_data="Boshqa Galaxy Podslar")],
 ] )

kompaniya = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Galaxy"), KeyboardButton(text="Apple")],
        [KeyboardButton(text="HONOR")],
    ],
    resize_keyboard=True
)

telefonApple = ReplyKeyboardMarkup(
     keyboard=[
        [KeyboardButton(text="Apple Air Pods"), KeyboardButton(text="Apple Qo'l soati")],
        [KeyboardButton(text="Apple Planshet"), KeyboardButton(text="Apple Smartfon")],
        [KeyboardButton(text="orqaga")],
    ],
    resize_keyboard=True
)

Apple_Watch= InlineKeyboardMarkup(  
    inline_keyboard=[
        [InlineKeyboardButton(text="Apple Watch Series 11", callback_data="Apple Watch Series 11")],
        [InlineKeyboardButton(text="Apple Watch SE 3", callback_data="Apple Watch SE 3")],
        [InlineKeyboardButton(text="Apple Watch Ultra 3", callback_data="Apple Watch Ultra 3")],
        [InlineKeyboardButton(text="Boshqa Apple qo'l soatlar", callback_data="Boshqa Apple qo'l soatlar")],
 ] )

Apple_Smartfon= InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="iPhone 17 Pro", callback_data="iPhone 17 Pro")],
        [InlineKeyboardButton(text="iPhone Air", callback_data="iPhone Air")],
        [InlineKeyboardButton(text="iPhone 16", callback_data="iPhone 16")],
        [InlineKeyboardButton(text="Boshqa Apple Smartfonlar", callback_data="Boshqa Apple Smartfonlar")],
 ] )

Apple_Planshet= InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="iPad Pro", callback_data="iPad Pro")],
        [InlineKeyboardButton(text="iPad Air", callback_data="iPad Air")],
        [InlineKeyboardButton(text="iPad", callback_data="iPad")],
        [InlineKeyboardButton(text="Boshqa Apple Planshetlar", callback_data="Boshqa Apple Planshetlar")],
 ] )

Apple_Pods= InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="AirPods 4", callback_data="AirPods 4")],
        [InlineKeyboardButton(text="AirPods Pro 3", callback_data="AirPods Pro 3")],
        [InlineKeyboardButton(text="AirPods Max 2", callback_data="AirPods Max 2")],
        [InlineKeyboardButton(text="Boshqa Apple Podslar", callback_data="Boshqa Apple Podslar")],
 ] )

telefonHONOR = ReplyKeyboardMarkup(
     keyboard=[
        [KeyboardButton(text="HONOR Planshet"), KeyboardButton(text="HONOR Smartfon")],
        [KeyboardButton(text="orqaga")],
    ],  
    resize_keyboard=True
)

HONOR_Smartfon= InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="HONOR Magic8 Pro", callback_data="HONOR Magic8 Pro")],
        [InlineKeyboardButton(text="HONOR 600 Lite", callback_data="HONOR 600 Lite")],
        [InlineKeyboardButton(text="HONOR X9d", callback_data="HONOR X9d")],
        [InlineKeyboardButton(text="Boshqa HONOR Smartfonlar", callback_data="Boshqa HONOR Smartfonlar")],
 ] )

HONOR_Planshet= InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="iPad Pro", callback_data="iPad Pro")],
        [InlineKeyboardButton(text="iPad Air", callback_data="iPad Air")],
        [InlineKeyboardButton(text="iPad", callback_data="iPad")],
        [InlineKeyboardButton(text="Boshqa Apple Planshetlar", callback_data="Boshqa Apple Planshetlar")],
 ] )

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Assalomu alaykum", reply_markup=kompaniya)


@dp.message(F.text == "orqaga")
async def orqaga_handler(message: types.Message):
    await message.answer("Ortga qaytdingiz", reply_markup=kompaniya)


@dp.message(F.text == "Galaxy")
async def xorazm_handler(message: types.Message):
    await message.answer_photo(
        photo="https://avatars.mds.yandex.net/i?id=8a77a90224537628aa5fc1c575ddbf5b576987a7-6424941-images-thumbs&n=13",
        caption=(
            "Asos solingan yili: 1938-yil, Li Byung-chul tomonidan (Janubiy Koreya, Seul)\n\n"
            "Kompaniya turi: Konglomerat (elektronika, qurilish, moliya, IT, kemasozlik va boshqalar)\n"
            "Samsung Electronics: Smartfonlar, televizorlar, yarimo‘tkazgichlar, xotira chiplar va boshqa elektronika ishlab chiqaradi\n"
            "Daromad (2023): 234,6 milliard AQSh dollari\n"
        ),
        reply_markup=telefon
    )

@dp.message(F.text == "Galaxy Planshet")
async def xorazm_handler(message: types.Message):
    await message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1eY3mmJAy25By--mtaE5z9ki9c_VfRNXEtA&s",
        caption=(
            "Planshetlar haqida batafsil:\n"
        ),
        reply_markup=Galaxy_Planshet
    )

@dp.callback_query(F.data == "Galaxy Tab S11 Ultra 5G")
async def galaxy_Pods_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://images.samsung.com/is/image/samsung/p6pim/uz_ru/sm-x936bzaasoz/gallery/uz-ru-galaxy-tab-s11-ultra-sm-x930-572776-sm-x936bzaasoz-550308283?$Q90_1920_1280_F_PNG$",
        caption="Galaxy Tab S11 Ultra 5G haqida batafsil:\n"
        "https://www.samsung.com/uz_ru/tablets/galaxy-tab-s/galaxy-tab-s11-ultra-gray-256gb-5g-sm-x936bzaasoz/", reply_markup=telefon
    )

@dp.callback_query(F.data == "Galaxy Tab S10 Lite Wi-Fi")
async def galaxy_Pods_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://images.samsung.com/is/image/samsung/p6pim/uz_ru/sm-x400nzaasoz/gallery/uz-ru-galaxy-tab-s10-lite-sm-x406-562536-sm-x400nzaasoz-548749509?$Q90_1920_1280_F_PNG$",
        caption="Galaxy Tab S10 Lite Wi-Fi haqida batafsil:\n"
        "https://www.samsung.com/uz_ru/tablets/galaxy-tab-s/galaxy-tab-s10-lite-gray-128gb-wifi-sm-x400nzaasoz/", reply_markup=telefon
    )

@dp.callback_query(F.data == "Galaxy Tab A11+")
async def galaxy_Pods_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://images.samsung.com/is/image/samsung/p6pim/uz_ru/sm-x230nzaasoz/gallery/uz-ru-galaxy-tab-a11-plus-sm-x230-573167-sm-x230nzaasoz-550367383?$Q90_1920_1280_F_PNG$",
        caption="Galaxy Tab A11+ haqida batafsil:\n"
        "https://www.samsung.com/uz_ru/tablets/galaxy-tab-a/galaxy-tab-a11-plus-gray-128gb-wifi-sm-x230nzaasoz/", reply_markup=telefon
    )

@dp.callback_query(F.data == "Boshqa Galaxy Planshetlar")
async def galaxy_Pods_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIihHjpT0MlzBFm5hZFwQcbAH3gPu5jJFehA&s",
        caption="Boshqa Planshetlar haqida batafsil:\n"
        "https://www.samsung.com/uz_ru/tablets/all-tablets/", reply_markup=telefon
    )

@dp.message(F.text == "Galaxy Air Pods")
async def xorazm_handler(message: types.Message):
    await message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSu-LPtc_a-7oUbvYhSsq6xveIrgMDMWGNc3A&s",
        caption=(
            "Air Podslar haqida batafsil:\n"
        ),
        reply_markup=Galaxy_Pods
    )

@dp.callback_query(F.data == "Galaxy Buds4")
async def galaxy_Pods_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://images.samsung.com/is/image/samsung/p6pim/uz_ru/s2602/gallery/uz-ru-galaxy-buds4-r540-sm-r540nzkacis-thumb-550960984?$Q90_495_330_F_PNG$",
        caption="Galaxy Buds4 haqida batafsil:"
        "https://www.samsung.com/uz_ru/audio-sound/galaxy-buds/galaxy-buds4-black-sm-r540nzkacis/", reply_markup=telefon
    )

@dp.callback_query(F.data == "Galaxy Buds3 FE")
async def galaxy_Pods_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://images.samsung.com/is/image/samsung/p6pim/uz_ru/sm-r420nzaacis/gallery/uz-ru-galaxy-buds3-fe-sm-r420nzaacis-thumb-548798425?$Q90_495_330_F_PNG$",
        caption="Galaxy Buds3 FE haqida batafsil:\n"
        "https://www.samsung.com/uz_ru/audio-sound/galaxy-buds/galaxy-buds3-fe-gray-sm-r420nzaacis/", reply_markup=telefon
    )

@dp.callback_query(F.data == "Galaxy Buds Core")
async def galaxy_Pods_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://images.samsung.com/is/image/samsung/p6pim/uz_ru/sm-r410nzwacis/gallery/uz-ru-galaxy-buds-core-r410-sm-r410nzwacis-547719001?$Q90_1920_1280_F_PNG$",
        caption="Galaxy Buds Core haqida batafsil:\n"
        "https://www.samsung.com/uz_ru/audio-sound/galaxy-buds/galaxy-buds-core-white-sm-r410nzwacis/", reply_markup=telefon
    )

@dp.callback_query(F.data == "Boshqa Galaxy Podslar")
async def galaxy_Pods_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRi0SIVEevXEKGJ0c4aSofUrG2jBLbouw8JkQ&s",
        caption="Boshqa Podslar haqida batafsil:\n"
        "https://www.samsung.com/uz_ru/audio-sound/all-audio-sound/", reply_markup=telefon
    )

@dp.message(F.text == "Galaxy Smartfon")
async def xorazm_handler(message: types.Message):
    await message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQS0y_6Bd0jeS-jZ2z_QE3xeDs9RhAr90f0FQ&s",
        caption=(
            "Smartfonlar haqida batafsil:\n"
        ),
        reply_markup=Galaxy_Smartfon
    )

@dp.callback_query(F.data == "Galaxy A57 5G")
async def galaxy_Pods_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://images.samsung.com/is/image/samsung/p6pim/uz_ru/sm-a576bzvfsoz/gallery/uz-ru-galaxy-a57-5g-sm-a576-sm-a576bzvfsoz-551731432?$Q90_1920_1280_F_PNG$",
        caption="Galaxy A57 5G haqida batafsil:"
        "https://www.samsung.com/uz_ru/smartphones/galaxy-a/galaxy-a57-5g-awesome-lilac-256gb-sm-a576bzvfsoz/", reply_markup=telefon
    )

@dp.callback_query(F.data == "Galaxy S25 FE")
async def galaxy_Pods_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://images.samsung.com/is/image/samsung/p6pim/uz_ru/sm-s731bzkcsoz/gallery/uz-ru-galaxy-s25-fe-sm-s731-sm-s731bzkcsoz-548764495?$Q90_1920_1280_F_PNG$",
        caption="Galaxy S25 FE haqida batafsil:\n"
        "https://www.samsung.com/uz_ru/smartphones/galaxy-s/galaxy-s25-fe-jetblack-256gb-sm-s731bzkcsoz/", reply_markup=telefon
    )

@dp.callback_query(F.data == "Galaxy S26 Ultra")
async def galaxy_Pods_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://images.samsung.com/is/image/samsung/p6pim/uz_ru/s2602/gallery/uz-ru-galaxy-s26-ultra-s948-sm-s948bzvcsoz-thumb-550951572?$Q90_495_330_F_PNG$",
        caption="Galaxy S26 Ultra haqida batafsil:\n"
        "https://www.samsung.com/uz_ru/smartphones/galaxy-s26-ultra/", reply_markup=telefon
    )

@dp.callback_query(F.data == "Boshqa Galaxy Smartfonlar")
async def galaxy_Pods_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSjXVc4-ii_JsVO8zSXsCjxGmjDDCmr7y-b5Q&s",
        caption="Galaxy Smartfonlar haqida batafsil:\n"
        "https://www.samsung.com/uz_ru/tablets/all-tablets/", reply_markup=telefon
    )

@dp.message(F.text == "Galaxy Qo'l soati")
async def xorazm_handler(message: types.Message):
    await message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQs1zH4jGasDZHbWUJNnZKuP8aygli9OKpOA&s",
        caption=(
            "Qo'l soatlar haqida batafsil:\n"
        ),
        reply_markup=Galaxy_Watch
    )

@dp.callback_query(F.data == "Galaxy Watch8 Classic")
async def galaxy_Pods_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://images.samsung.com/is/image/samsung/p6pim/uz_ru/f2507/gallery/uz-ru-galaxy-watch8-classic-l500-sm-l500nzkacis-547719588?$Q90_1920_1280_F_PNG$",
        caption="Galaxy Watch8 Classic haqida batafsil:\n"
        "https://www.samsung.com/uz_ru/watches/galaxy-watch/galaxy-watch8-classic-46mm-black-bluetooth-sm-l500nzkacis/  ", reply_markup=telefon
    )

@dp.callback_query(F.data == "Galaxy Watch8")
async def galaxy_Pods_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://images.samsung.com/is/image/samsung/p6pim/uz_ru/f2507/gallery/uz-ru-galaxy-watch8-l320-sm-l320nzsacis-547719934?$Q90_1920_1280_F_PNG$",
        caption="Galaxy Watch8 haqida batafsil:\n"
        "https://www.samsung.com/uz_ru/watches/galaxy-watch/galaxy-watch8-40mm-silver-bluetooth-sm-l320nzsacis/", reply_markup=telefon
    )

@dp.callback_query(F.data == "Galaxy Watch7 Bluetooth")
async def galaxy_Pods_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://images.samsung.com/is/image/samsung/p6pim/uz_ru/2407/gallery/uz-ru-galaxy-watch7-l300-sm-l300nzeacis-542513743?$Q90_1920_1280_F_PNG$",
        caption="Galaxy Watch7 Bluetooth haqida batafsil:\n"
        "https://www.samsung.com/uz_ru/watches/galaxy-watch/galaxy-watch7-40mm-cream-bt-sm-l300nzeacis/", reply_markup=telefon
    )

@dp.callback_query(F.data == "Boshqa Galaxy qo'l soatlar")
async def galaxy_Pods_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZf3-DyADBvaNmphZbUcPLaB38IeTDReUGyQ&s",
        caption="Galaxy qo'l soatlari haqida batafsil:\n"
        "https://www.samsung.com/uz_ru/watches/all-watches/", reply_markup=telefon
    )

@dp.message(F.text == "Apple")
async def Apple_handler(message: types.Message):
    await message.answer_photo(
        photo="https://images.macrumors.com/t/qZDdMwXMtkbMV4OAonirIWNcn3A=/2500x/article-new/2025/12/Apple-26-Feature.jpg",
        caption=(
            "Asos solingan yili: 1976-yil, Steve Jobs, Steve Wozniak va Ronald Wayne tomonidan.\n\n"
            "Markazi: Cupertino, Kaliforniya, AQSh.\n"
            "Mashhur mahsulotlari: iPhone, iPad, Mac, Apple Watch, AirPods, Apple TV.\n"
            "Daromad (2025): 383 milliard AQSh dollari atrofida.\n"
        ),
        reply_markup=telefonApple
    )

@dp.message(F.text == "Apple Planshet")
async def iPad_handler(message: types.Message):
    await message.answer_photo(
        photo="https://www.apple.com/v/ipad-mini/u/images/overview/hero/fan__cyid3h2vl0wi_large.jpg",
        caption=(
            "Planshetlar haqida batafsil:\n"
        ),
        reply_markup=Apple_Planshet
    )

@dp.callback_query(F.data == "iPad Pro")
async def iPad_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://www.apple.com/assets-www/en_WW/ipad/01_product_tile/large/ipad_pro_3adafef74_2x.jpg",
        caption="iPad Pro haqida batafsil:\n"
        "https://www.apple.com/ipad-pro/", reply_markup=telefonApple
    )

@dp.callback_query(F.data == "iPad Air")
async def iPad_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://www.apple.com/v/ipad-air/ah/images/overview/closer-look/all-colors/slide_2B__dvqfqwnkj2c2_large_2x.jpg",
        caption="iPad Air haqida batafsil:\n"
        "https://www.apple.com/ipad-air/", reply_markup=telefonApple
    )

@dp.callback_query(F.data == "iPad")
async def iPad_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://www.apple.com/v/ipad-11/d/images/overview/hero/hero__crzh9misvcuq_large_2x.jpg",
        caption="iPad haqida batafsil:\n"
        "https://www.apple.com/ipad-11/", reply_markup=telefonApple
    )

@dp.callback_query(F.data == "Boshqa Apple Planshetlar")
async def iPad_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1WrZpXwHENF82jeXgDBi6IZ_59t7R9IYYIA&s",
        caption="Boshqa Planshetlar haqida batafsil:\n"
        "https://www.apple.com/ipad/", reply_markup=telefonApple
    )

@dp.message(F.text == "Apple Air Pods")
async def Apple_Pods_handler(message: types.Message):
    await message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/izmages?q=tbn:ANd9GcSu-LPtc_a-7oUbvYhSsq6xveIrgMDMWGNc3A&s",
        caption=(
            "Air Podslar haqida batafsil:\n"
        ),
        reply_markup=Apple_Pods
    )

@dp.callback_query(F.data == "AirPods 4")
async def Apple_Pods_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://www.apple.com/v/airpods-4/g/images/overview/bento-gallery/bento_case_close__f0fhueeeoy2q_xlarge_2x.jpg",
        caption="AirPods4 haqida batafsil:"
        "https://www.apple.com/airpods-4/", reply_markup=telefonApple
    )

@dp.callback_query(F.data == "AirPods Pro 3")
async def Apple_Pods_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFO46v-qoecqos1g814KIWSc9qDPXVia2M-g&s",
        caption="AirPods Pro 3 haqida batafsil:\n"
        "https://www.apple.com/airpods-pro/", reply_markup=telefonApple
    )

@dp.callback_query(F.data == "AirPods Max 2")
async def Apple_Pods_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://www.apple.com/v/airpods-max/k/images/overview/bento/midnight/bento_1_airpod_max_midnight__4jy1tkqh9qay_xlarge_2x.jpg",
        caption="AirPods Max 2 haqida batafsil:\n"
        "https://www.apple.com/airpods-max/", reply_markup=telefonApple
    )

@dp.callback_query(F.data == "Boshqa Apple Podslar")
async def Apple_Pods_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRi0SIVEevXEKGJ0c4aSofUrG2jBLbouw8JkQ&s",
        caption="Boshqa Podslar haqida batafsil:\n"
        "https://www.apple.com/airpods/", reply_markup=telefonApple
    )

@dp.message(F.text == "Apple Smartfon")
async def iPhone_handler(message: types.Message):
    await message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRKw72zxo7rK8jLKJGJo2PwZmixUl0fcnKT4w&s",
        caption=(
            "Smartfonlar haqida batafsil:\n"
        ),
        reply_markup=Apple_Smartfon
    )

@dp.callback_query(F.data == "iPhone 17 Pro")
async def iPhone_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/iphone-17pro-digitalmat-gallery-5-202509?wid=728&hei=666&fmt=p-jpg&qlt=95&.v=ekJPc2lPUlRuRk50SkcyOVdnU1d0TjFla0N0Znl3UThxdjB3SW91ZDVJeG1hWkZ6UHNRSXhlQnZJMURpUmV1QW8xUkhYejcxalRvY0FPQVpMcmoxMDlLQzdVZ2V3VnpqcXFKTGxlK1dFUXpucGszV1kvUjNNUmdVQ1lGWXlTekY",
        caption="iPhone 17 Pro haqida batafsil:"
        "https://www.apple.com/shop/buy-iphone/iphone-17-pro/", reply_markup=telefonApple
    )

@dp.callback_query(F.data == "iPhone Air")
async def iPhone_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/iphone-air-finish-select-202509-spaceblack?wid=5120&hei=2880&fmt=webp&qlt=90&.v=NUpaQVl1bitSNmJWZUdKdi9QZHhsQnMyOXpiUEVyWXc0UFVFMUg1R1Ztcit0SFUxZzlOYjFnK2g1TG9hVnNYcmd2S3NaRzcrU0dmYjNHTUFiMnlsWFUxSlgrVWMrMzU1OXo2c2JyNjJZTGlaMVdFU2dmejhESzZKZmZKVm4vRFY&traceId=1",
        caption="iPhone Air haqida batafsil:\n"
        "https://www.apple.com/shop/buy-iphone/iphone-air", reply_markup=telefonApple
    )

@dp.callback_query(F.data == "iPhone 16")
async def iPhone_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/iphone16-digitalmat-gallery-3-202409?wid=728&hei=666&fmt=p-jpg&qlt=95&.v=Y2tBd1RqSzMrd3hScm1lN290ZENDQnlVUVRHTkd5alQ5aFd0OWdSZUk0SXlLZ0xXbFByV2Vvak9rWndaamlPU3cvMldkdDlIc0lud2tjcDJ3djFCUkV2dGpWUjV5VzZtaGp2QjBiUXR3RUFJWFM4ekI5ZC9uRFBQN3lzOXp4dnA",
        caption="iPhone 16 haqida batafsil:\n"
        "https://www.apple.com/shop/buy-iphone/iphone-16", reply_markup=telefonApple
    )

@dp.callback_query(F.data == "Boshqa Apple Smartfonlar")
async def iPhone_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://www.ookla.com/s/media/2024/11/iPhone-16-5G-Performance-Header-2024.png",
        caption="Apple Smartfonlar haqida batafsil:\n"
        "https://www.apple.com/shop/buy-iphone", reply_markup=telefonApple
    )

@dp.message(F.text == "Apple Qo'l soati")
async def Apple_Watch_handler(message: types.Message):
    await message.answer_photo(
        photo="https://www.apple.com/newsroom/images/product/watch/lifestyle/Apple_announces-watch-se_09152020_big.jpg.large.jpg",
        caption=(
            "Qo'l soatlar haqida batafsil:\n"
        ),
        reply_markup=Apple_Watch
    )

@dp.callback_query(F.data == "Apple Watch Series 11")
async def Apple_Watch_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/watch-s11-digitalmat-gallery-2-202509?wid=728&hei=666&fmt=png-alpha&.v=T1pyYVFWN3pudWliRWQ0WTl3UmJXdHp0bzhwRTZxYVNNMnVRTXVpMUZES0U5aWg1WE9Xd3BOSWtnNzkvSWZLd1RnWXNaUGkzWFF6Q0FVUXZLQlA2QWRQNDN3akRCWUdoRE05dXNrQXBIR0JxM3o3OTdmdmwreUkzeWhUWnZLbVc",
        caption="Apple Watch Series 11 haqida batafsil:\n"
        "https://www.apple.com/shop/buy-watch/apple-watch", reply_markup=telefonApple
    )

@dp.callback_query(F.data == "Apple Watch SE 3")
async def Apple_Watch_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/watch-se-digitalmat-gallery-4-202509?wid=728&hei=666&fmt=png-alpha&.v=OENuMjYwZFNXbVduWHRoSkRoR3pUT21WVFhyY3phSHE0c0dmYXl5WVVReVIvWHFRU0d1VHljN0VrTnNHekFWWjJSWWg0TDRLSXM4czBZQjZvUHdsVExoNFJyTi92WVZ5M0dWLzdDZUxuajFTZy9JeUNjV2pzbzd6anYzTldHVWw",
        caption="Apple Watch SE 3 haqida batafsil:\n"
        "https://www.apple.com/shop/buy-watch/apple-watch-se", reply_markup=telefonApple
    )

@dp.callback_query(F.data == "Apple Watch Ultra 3")
async def Apple_Watch_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/watch-ultra-digitalmat-gallery-2-202509?wid=728&hei=666&fmt=png-alpha&.v=Z1hvTnZGMTVLTmdOS1Q2clJKMzNienBhZEVDYXdNalJLdkllSGFmNnBVVG1EQmw5cXB6TFRpSUdyZ2IrMUFPYkUzZ2l1YzBrOVJUZUJialBBeVhocGZGaUt0aUg4YW45V29OZXhJcXptMTR1SVQySGVQOEpDOWNyU1VPZW5GSms",
        caption="Apple Watch Ultra 3 haqida batafsil:\n"
        "https://www.apple.com/shop/buy-watch/apple-watch-ultra", reply_markup=telefonApple
    )

@dp.callback_query(F.data == "Boshqa Apple qo'l soatlar")
async def Apple_Watch_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ88mryT3rmBrkQeEb3g75mbIbNROMGdx1rqA&s",
        caption="Apple qo'l soatlari haqida batafsil:\n"
        "https://www.apple.com/shop/buy-watch", reply_markup=telefonApple
    )

@dp.message(F.text == "HONOR")
async def xorazm_handler(message: types.Message):
    await message.answer_photo(
        photo="https://images.macrumors.com/t/qZDdMwXMtkbMV4OAonirIWNcn3A=/2500x/article-new/2025/12/Apple-26-Feature.jpg",
        caption=(
            "Asos solingan yili: 2013-yilda Huawei subbrendi sifatida.\n\n"
            "Mustaqil kompaniya: 2020-yildan.\n"
            "Markazi: Shenzhen, Xitoy.  \n"
            "Mahsulotlari: Smartfonlar, planshetlar, noutbuklar, quloqchinlar, aqlli soatlar.\n"
        ),
        reply_markup=telefonHONOR
    )

@dp.message(F.text == "HONOR Planshet")
async def HONOR_handler(message: types.Message):
    await message.answer_photo(
        photo="https://www.apple.com/v/ipad-mini/u/images/overview/hero/fan__cyid3h2vl0wi_large.jpg",
        caption=(
            "Planshetlar haqida batafsil:\n"
        ),
        reply_markup=HONOR_Planshet
    )

@dp.callback_query(F.data == "iPad Pro")
async def HONOR_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://www.apple.com/assets-www/en_WW/ipad/01_product_tile/large/ipad_pro_3adafef74_2x.jpg",
        caption="iPad Pro haqida batafsil:\n"
        "https://www.apple.com/ipad-pro/", reply_markup=telefonHONOR
    )

@dp.callback_query(F.data == "iPad Air")
async def HONOR_handler(query: types.CallbackQuery):
    await query.message.answer_photo(   
        photo="https://www.apple.com/v/ipad-air/ah/images/overview/closer-look/all-colors/slide_2B__dvqfqwnkj2c2_large_2x.jpg",
        caption="iPad Air haqida batafsil:\n"
        "https://www.apple.com/ipad-air/", reply_markup=telefonHONOR
    )

@dp.callback_query(F.data == "iPad")
async def HONOR_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://www.apple.com/v/ipad-11/d/images/overview/hero/hero__crzh9misvcuq_large_2x.jpg",
        caption="iPad haqida batafsil:\n"
        "https://www.apple.com/ipad-11/", reply_markup=telefonHONOR
    )

@dp.callback_query(F.data == "Boshqa HONOR Planshetlar")
async def HONOR_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1WrZpXwHENF82jeXgDBi6IZ_59t7R9IYYIA&s",
        caption="Boshqa Planshetlar haqida batafsil:\n"
        "https://www.apple.com/ipad/", reply_markup=telefonHONOR
    )


@dp.message(F.text == "HONOR Smartfon")
async def HONOR_handler(message: types.Message):
    await message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2W-g8uo5qSu2WuHlnT6PLJIAQ1pqevxbiaw&s",
        caption=(
            "Smartfonlar haqida batafsil:\n"
        ),
        reply_markup=HONOR_Smartfon
    )

@dp.callback_query(F.data == "HONOR Magic8 Pro")
async def HONOR_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://assets.asaxiy.uz/product/items/desktop/6208835cf0ad7b20c109b9749d51e8452026030312054851078O1pZ7bWK55.jpg ",
        caption="HONOR Magic8 Pro haqida batafsil:"
        "https://www.honor.com/uz-uz/phones/honor-magic8-pro/", reply_markup=telefonHONOR
    )

@dp.callback_query(F.data == "HONOR 600 Lite")
async def HONOR_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4zCk1z_nIMEo1pZC_9CCmdHfEPwzrjraY8Q&s",
        caption="HONOR 600 Lite haqida batafsil:\n"
        "https://www.honor.com/uz-uz/phones/honor-600-lite/", reply_markup=telefonHONOR
    )

@dp.callback_query(F.data == "HONOR X9d")
async def HONOR_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMJeBrYUb7KxhKR12y6llpQhGKLZ44tWOYWA&s",
        caption="HONOR X9d haqida batafsil:\n"
        "https://www.honor.com/uz-uz/phones/honor-x9d/", reply_markup=telefonHONOR
    )

@dp.callback_query(F.data == "Boshqa HONOR Smartfonlar")
async def HONOR_handler(query: types.CallbackQuery):
    await query.message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSTkKSlXYbAx0B2agpJGWFG7k-GVnlBnBzoLw&s ",
        caption="Apple Smartfonlar haqida batafsil:\n"
        "https://www.honor.com/uz-uz/phones/", reply_markup=telefonHONOR
    )

@dp.message()
async def man(message: Message):
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())

