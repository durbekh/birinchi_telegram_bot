import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from py import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Assalomu alaykum, nima hizmat ?")


@dp.message(F.text == "1")
async def cmd_1(message: Message):
    await message.reply("Titanik")

@dp.message(F.text == "2")
async def cmd_2(message: Message):
    await message.reply("Avatar")

@dp.message(F.text == "3")
async def cmd_3(message: Message):
    await message.reply("Inception")

@dp.message(F.text == "4")
async def cmd_4(message: Message):
    await message.reply("The Godfather")

@dp.message(F.text == "5")
async def cmd_5(message: Message):
    await message.reply("Forrest Gump")

@dp.message(F.text == "6")
async def cmd_6(message: Message):
    await message.reply("The Dark Knight")

@dp.message(F.text == "7")
async def cmd_7(message: Message):
    await message.reply("Interstellar")

@dp.message(F.text == "8")
async def cmd_8(message: Message):
    await message.reply("Gladiator")

@dp.message(F.text == "9")
async def cmd_9(message: Message):
    await message.reply("Pulp Fiction")

@dp.message(F.text == "10")
async def cmd_10(message: Message):
    await message.reply("Avengers: Endgame")

@dp.message(F.text == "11")
async def cmd_11(message: Message):
    await message.reply("The Matrix")

@dp.message(F.text == "12")
async def cmd_12(message: Message):
    await message.reply("Fight Club")

@dp.message(F.text == "13")
async def cmd_13(message: Message):
    await message.reply("Saving Private Ryan")

@dp.message(F.text == "14")
async def cmd_14(message: Message):
    await message.reply("The Shawshank Redemption")

@dp.message(F.text == "15")
async def cmd_15(message: Message):
    await message.reply("Jurassic Park")

@dp.message(F.text == "16")
async def cmd_16(message: Message):
    await message.reply("Iron Man")

@dp.message(F.text == "17")
async def cmd_17(message: Message):
    await message.reply("Spider-Man: No Way Home")

@dp.message(F.text == "18")
async def cmd_18(message: Message):
    await message.reply("Black Panther")

@dp.message(F.text == "19")
async def cmd_19(message: Message):
    await message.reply("Doctor Strange")

@dp.message(F.text == "20")
async def cmd_20(message: Message):
    await message.reply("Captain America: Civil War")

@dp.message(F.text == "21")
async def cmd_21(message: Message):
    await message.reply("Guardians of the Galaxy")

@dp.message(F.text == "22")
async def cmd_22(message: Message):
    await message.reply("Ant-Man")

@dp.message(F.text == "23")
async def cmd_23(message: Message):
    await message.reply("Thor: Ragnarok")

@dp.message(F.text == "24")
async def cmd_24(message: Message):
    await message.reply("Deadpool")

@dp.message(F.text == "25")
async def cmd_25(message: Message):
    await message.reply("Logan")

@dp.message(F.text == "26")
async def cmd_26(message: Message):
    await message.reply("The Wolverine")

@dp.message(F.text == "27")
async def cmd_27(message: Message):
    await message.reply("Avengers: Infinity War")

@dp.message(F.text == "28")
async def cmd_28(message: Message):
    await message.reply("Shazam!")

@dp.message(F.text == "29")
async def cmd_29(message: Message):
    await message.reply("Aquaman")

@dp.message(F.text == "30")
async def cmd_30(message: Message):
    await message.reply("Justice League")

@dp.message(F.text == "31")
async def cmd_31(message: Message):
    await message.reply("Man of Steel")

@dp.message(F.text == "32")
async def cmd_32(message: Message):
    await message.reply("Wonder Woman")

@dp.message(F.text == "33")
async def cmd_33(message: Message):
    await message.reply("The Flash")

@dp.message(F.text == "34")
async def cmd_34(message: Message):
    await message.reply("Green Lantern")

@dp.message(F.text == "35")
async def cmd_35(message: Message):
    await message.reply("Suicide Squad")
@dp.message(F.text == "36")
async def cmd_36(message: Message):
    await message.reply("The Batman")

@dp.message(F.text == "37")
async def cmd_37(message: Message):
    await message.reply("Joker")

@dp.message(F.text == "38")
async def cmd_38(message: Message):
    await message.reply("Birds of Prey")

@dp.message(F.text == "39")
async def cmd_39(message: Message):
    await message.reply("Black Adam")

@dp.message(F.text == "40")
async def cmd_40(message: Message):
    await message.reply("The Lion King")

@dp.message(F.text == "41")
async def cmd_41(message: Message):
    await message.reply("Aladdin")

@dp.message(F.text == "42")
async def cmd_42(message: Message):
    await message.reply("Frozen")

@dp.message(F.text == "43")
async def cmd_43(message: Message):
    await message.reply("Moana")

@dp.message(F.text == "44")
async def cmd_44(message: Message):
    await message.reply("Zootopia")

@dp.message(F.text == "45")
async def cmd_45(message: Message):
    await message.reply("Encanto")

@dp.message(F.text == "46")
async def cmd_46(message: Message):
    await message.reply("Turning Red")

@dp.message(F.text == "47")
async def cmd_47(message: Message):
    await message.reply("Coco")

@dp.message(F.text == "48")
async def cmd_48(message: Message):
    await message.reply("Luca")

@dp.message(F.text == "49")
async def cmd_49(message: Message):
    await message.reply("Raya and the Last Dragon")

@dp.message(F.text == "50")
async def cmd_50(message: Message):
    await message.reply("Lightyear")

@dp.message(F.text == "51")
async def cmd_51(message: Message):
    await message.reply("Inside Out")

@dp.message(F.text == "52")
async def cmd_52(message: Message):
    await message.reply("Soul")

@dp.message(F.text == "53")
async def cmd_53(message: Message):
    await message.reply("Up")

@dp.message(F.text == "54")
async def cmd_54(message: Message):
    await message.reply("Wall-E")

@dp.message(F.text == "55")
async def cmd_55(message: Message):
    await message.reply("Finding Nemo")

@dp.message(F.text == "56")
async def cmd_56(message: Message):
    await message.reply("Finding Dory")

@dp.message(F.text == "57")
async def cmd_57(message: Message):
    await message.reply("Toy Story")

@dp.message(F.text == "58")
async def cmd_58(message: Message):
    await message.reply("Toy Story 2")

@dp.message(F.text == "59")
async def cmd_59(message: Message):
    await message.reply("Toy Story 3")

@dp.message(F.text == "60")
async def cmd_60(message: Message):
    await message.reply("Toy Story 4")

@dp.message(F.text == "61")
async def cmd_61(message: Message):
    await message.reply("Cars")

@dp.message(F.text == "62")
async def cmd_62(message: Message):
    await message.reply("Cars 2")

@dp.message(F.text == "63")
async def cmd_63(message: Message):
    await message.reply("Cars 3")

@dp.message(F.text == "64")
async def cmd_64(message: Message):
    await message.reply("Monsters, Inc.")

@dp.message(F.text == "65")
async def cmd_65(message: Message):
    await message.reply("Monsters University")

@dp.message(F.text == "66")
async def cmd_66(message: Message):
    await message.reply("A Bug's Life")

@dp.message(F.text == "67")
async def cmd_67(message: Message):
    await message.reply("The Incredibles")

@dp.message(F.text == "68")
async def cmd_68(message: Message):
    await message.reply("The Incredibles 2")

@dp.message(F.text == "69")
async def cmd_69(message: Message):
    await message.reply("Brave")

@dp.message(F.text == "70")
async def cmd_70(message: Message):
    await message.reply("Onward")

@dp.message(F.text == "71")
async def cmd_71(message: Message):
    await message.reply("Ratatouille")

@dp.message(F.text == "72")
async def cmd_72(message: Message):
    await message.reply("Big Hero 6")

@dp.message(F.text == "73")
async def cmd_73(message: Message):
    await message.reply("Wreck-It Ralph")

@dp.message(F.text == "74")
async def cmd_74(message: Message):
    await message.reply("Ralph Breaks the Internet")
@dp.message(F.text == "75")
async def cmd_75(message: Message):
    await message.reply("Bolt")

@dp.message(F.text == "76")
async def cmd_76(message: Message):
    await message.reply("Meet the Robinsons")

@dp.message(F.text == "77")
async def cmd_77(message: Message):
    await message.reply("Chicken Little")

@dp.message(F.text == "78")
async def cmd_78(message: Message):
    await message.reply("Atlantis: The Lost Empire")

@dp.message(F.text == "79")
async def cmd_79(message: Message):
    await message.reply("Treasure Planet")

@dp.message(F.text == "80")
async def cmd_80(message: Message):
    await message.reply("Hercules")

@dp.message(F.text == "81")
async def cmd_81(message: Message):
    await message.reply("Tarzan")

@dp.message(F.text == "82")
async def cmd_82(message: Message):
    await message.reply("The Hunchback of Notre Dame")

@dp.message(F.text == "83")
async def cmd_83(message: Message):
    await message.reply("Pocahontas")

@dp.message(F.text == "84")
async def cmd_84(message: Message):
    await message.reply("Mulan")

@dp.message(F.text == "85")
async def cmd_85(message: Message):
    await message.reply("Beauty and the Beast")

@dp.message(F.text == "86")
async def cmd_86(message: Message):
    await message.reply("The Little Mermaid")

@dp.message(F.text == "87")
async def cmd_87(message: Message):
    await message.reply("Cinderella")

@dp.message(F.text == "88")
async def cmd_88(message: Message):
    await message.reply("Sleeping Beauty")

@dp.message(F.text == "89")
async def cmd_89(message: Message):
    await message.reply("Snow White and the Seven Dwarfs")

@dp.message(F.text == "90")
async def cmd_90(message: Message):
    await message.reply("Bambi")

@dp.message(F.text == "91")
async def cmd_91(message: Message):
    await message.reply("Dumbo")

@dp.message(F.text == "92")
async def cmd_92(message: Message):
    await message.reply("Peter Pan")

@dp.message(F.text == "93")
async def cmd_93(message: Message):
    await message.reply("Lady and the Tramp")

@dp.message(F.text == "94")
async def cmd_94(message: Message):
    await message.reply("101 Dalmatians")

@dp.message(F.text == "95")
async def cmd_95(message: Message):
    await message.reply("The Aristocats")

@dp.message(F.text == "96")
async def cmd_96(message: Message):
    await message.reply("Robin Hood")

@dp.message(F.text == "97")
async def cmd_97(message: Message):
    await message.reply("The Rescuers")

@dp.message(F.text == "98")
async def cmd_98(message: Message):
    await message.reply("The Fox and the Hound")

@dp.message(F.text == "99")
async def cmd_99(message: Message):
    await message.reply("Oliver & Company")

@dp.message(F.text == "100")
async def cmd_100(message: Message):
    await message.reply("The Great Mouse Detective")

if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))

