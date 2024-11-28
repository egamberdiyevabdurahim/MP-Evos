from aiogram.fsm.context import FSMContext

from main import database
from aiogram import types, Router
from main.models import orders
from utils.basket import get_user_basket, clear_user_basket
from utils.notify_devs import send_notification_to_devs

router = Router()

@router.callback_query(F.data=="confirm_order")
async def confirm_order(call: types.CallbackQuery, state: FSMContext):
    user_basket = await get_user_basket(call.from_user.id)

    if user_basket:
        total_price = 0
        meal_ids = []

        for item in user_basket:
            meal_id = item['meal_id']
            quantity = item['quantity']
            price = item['price']
            meal_total = quantity * price
            total_price += meal_total
            meal_ids.append(meal_id)

        order_query = orders.insert().values(
            user_id=call.from_user.id,
            total_price=total_price,
            meal_ids=meal_ids,
        )
        order_id = await database.execute(order_query)

        await call.message.answer(f"Your order has been placed! Total: ${total_price}. Thank you!")

        await send_notification_to_devs(f"New order placed by user {call.from_user.id}. Total: ${total_price}")

        await clear_user_basket(call.from_user.id)

    else:
        await call.message.answer("Your basket is empty. Add some meals to your basket first.")
