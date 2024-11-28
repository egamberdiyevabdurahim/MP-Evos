from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from main import database
from aiogram import types, Router, F
from main.models import meals, meal_categories
from loader import _

router = Router()


@router.message(Command('menu'))
async def show_categories(message: types.Message):
    query = meal_categories.select()
    categories_list = await database.fetch_all(query)

    builder = InlineKeyboardBuilder()
    for category in categories_list:
        category_name = category["category_name"]
        category_id = category["id"]

        button = InlineKeyboardButton(
            text=category_name,
            callback_data=f"category_{category_id}"
        )
        builder.add(button)

    builder.adjust(2)
    await message.answer("Choose a category:", reply_markup=builder.as_markup())


@router.callback_query(F.data.startswith("category_"))
async def show_meals_for_category(call: types.CallbackQuery, state: FSMContext):
    category_id = int(call.data.split("_")[1])
    query = meals.select().where(meals.c.category_id == category_id)
    meals_list = await database.fetch_all(query)

    builder = InlineKeyboardBuilder()

    for meal in meals_list:
        meal_name = meal["meal_name"]
        meal_id = meal["id"]
        price = meal["price"]

        button = InlineKeyboardButton(
            text=f"{meal_name} - ${price}",
            callback_data=f"meal_{meal_id}"
        )
        builder.add(button)

    builder.adjust(2)
    await call.message.answer(_("Choose a meal:"), reply_markup=builder.as_markup())

@router.callback_query(F.data.startswith("meal_"))
async def meal_selected(call: types.CallbackQuery, state: FSMContext):
    meal_id = int(call.data.split("_")[1])  # Extract meal_id
    query = meals.select().where(meals.c.id == meal_id)  # Fetch the meal details
    meal = await database.fetch_one(query)

    if meal:
        meal_name = meal["meal_name"]
        price = meal["price"]

        builder = InlineKeyboardBuilder()
        builder.add(
            InlineKeyboardButton(text="-", callback_data=f"remove_{meal_id}"),
            InlineKeyboardButton(text="1", callback_data=f"add_{meal_id}"),
            InlineKeyboardButton(text="Add to Basket", callback_data=f"add_basket_{meal_id}")
        )


        await call.message.answer(
            f"You selected: {meal_name} - ${price}",
            reply_markup=builder.as_markup()
        )

@router.callback_query(F.data.startswith("remove_"))
async def remove_meal(call: types.CallbackQuery, state: FSMContext):
    meal_id = int(call.data.split("_")[1])
    await call.message.answer(_(f"Removed one {meal_id} from your basket."))

@router.callback_query(F.data.startswith("add_"))
async def add_meal(callback_query: types.CallbackQuery, state: FSMContext):
    meal_id = int(callback_query.data.split("_")[1])
    await callback_query.message.answer(f"Added one {meal_id} to your basket.")

@router.callback_query(F.data.startswith("add_basket_"))
async def add_to_basket(callback_query: types.CallbackQuery, state: FSMContext):
    meal_id = int(callback_query.data.split("_")[2])
    await callback_query.message.answer(f"{meal_id} has been added to your basket.")