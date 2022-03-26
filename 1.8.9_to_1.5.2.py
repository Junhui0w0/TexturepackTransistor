import os
import shutil
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
import time
from tkinter import messagebox  # 들어가야함




a = ""
b = ""
path_b = ""
c = ""
d = ""

#ESC키 바로 나가기
def Quit(event):
    root.quit()

# 현재 년도/월/일
def getCurrentStrDate():
    return time.strftime("%Y%m%d")


# 복사경로
def CopyLocation():
    my_pw = pwent.get()
    if my_pw == getCurrentStrDate():
        global a
        a = filedialog.askdirectory()
        if (len(a) > 1):
            CopylocationError.config(text=a, fg="blue")
        else:
            CopylocationError.config(text="복사할 디렉토리를 선택해 주세요.", fg="red")
    else:
        CopylocationError.config(text="비밀번호가 틀렸습니다.",fg="red")


# 폴더생성경로
def myfunc():
    if var.get() == 1:
        global d
        d = filedialog.askdirectory()
        if (len(name.get()) >= 1):
            if (len(d) > 1):
                path_d = "선택경로 : " + d + "/" + name.get()
                path.configure(text=path_d, fg="blue")
            else:
                path.config(text="!! 복사경로를 설정해주세요 !!", fg="red")
        else:
            path.config(text="!! 폴더 이름을 설정해주세요 !!",fg="red")
    else:
        if (len(name.get()) >= 1):
            path_b = "선택경로 : C:/Users/wydyx/AppData/Roaming/.minecraft/texturepacks/" + name.get()
            path.configure(text=path_b, fg="purple")
        else:
            path.config(text="!! 폴더 이름을 설정해주세요 !!", fg="red")


# 실행
def EXE():
    my_pw = pwent.get()
    if my_pw == getCurrentStrDate():
        if var.get() == 1:
            my_pw = pwent.get()
            if my_pw == getCurrentStrDate():
                os.chdir(d)
                os.mkdir(name.get())
                b = d + ('/' + name.get())
                os.chdir(b)
                os.mkdir('achievement')
                os.mkdir('armor')
                os.mkdir('art')
                os.mkdir('environment')
                os.mkdir('gui')
                os.mkdir('item')
                os.mkdir('misc')
                os.mkdir('mob')
                os.mkdir('terrain')
                os.mkdir('textures')
                os.mkdir('title')

                os.chdir(b + '/textures')
                os.mkdir('blocks')
                os.mkdir('items')

                os.chdir(b + '/gui')
                os.mkdir('creative_inv')

                os.chdir(b + '/mob')
                os.mkdir('enderdragon')
                os.mkdir('villager')

                os.chdir(b)

                f = open(b + '/pack.txt', "w")
                f.write('§41.8.9 §f-> §41.5.2§f로 변경된 텍스쳐팩')
                f.write('\n')
                f.write('§6모든문의 §f: 김준희#5870')
                f.close()

                # part of 상위표기(하위표기)

                # part of TexturePack(Pack)
                try:
                    file_path = a
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/pack.png', b)
                    if 'pack.png' in file_names:
                        os.rename(os.path.join(b, 'pack.png'), os.path.join(b, str('pack.png')))
                except:
                    pass

                    # part of gui_achieve(achievement)
                try:
                    file_path = a + '/assets/minecraft/textures/gui/achievement'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/achievement_background.png', b + '/achievement')
                    if 'achievement_background.png' in file_names:
                        os.rename(os.path.join(b + '/achievement', 'achievement_background.png'),
                                  os.path.join(b + '/achievement', str('bg.png')))
                except:
                    pass

                    # Part of Gui_container(GUI)
                try:
                    file_path = a + '/assets/minecraft/textures/gui/container'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/anvil.png', b + '/gui')
                    if 'anvil.png' in file_names:
                        os.rename(os.path.join(b + '/gui', 'anvil.png'), os.path.join(b + '/gui', str('repair.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/gui/container'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/brewing_stand.png', b + '/gui')
                    if 'brewing_stand.png' in file_names:
                        os.rename(os.path.join(b + '/gui', 'brewing_stand.png'),
                                  os.path.join(b + '/gui', str('alchemy.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/gui/container'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/crafting_table.png', b + '/gui')
                    if 'crafting_table.png' in file_names:
                        os.rename(os.path.join(b + '/gui', 'crafting_table.png'),
                                  os.path.join(b + '/gui', str('crafting.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/gui/container'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/dispenser.png', b + '/gui')
                    if 'dispenser.png' in file_names:
                        os.rename(os.path.join(b + '/gui', 'dispenser.png'), os.path.join(b + '/gui', str('trap.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/gui/container'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/enchanting_table.png', b + '/gui')
                    if 'enchanting_table.png' in file_names:
                        os.rename(os.path.join(b + '/gui', 'enchanting_table.png'),
                                  os.path.join(b + '/gui', str('enchant.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/gui/container'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/stats_icons.png', b + '/gui')
                    if 'stats_icons.png' in file_names:
                        os.rename(os.path.join(b + '/gui', 'stats_icons.png'),
                                  os.path.join(b + '/gui', str('icons.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/gui/container'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/villager.png', b + '/gui')
                    if 'villager.png' in file_names:
                        os.rename(os.path.join(b + '/gui', 'villager.png'),
                                  os.path.join(b + '/gui', str('trading.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/gui/container'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/beacon.png', b + '/gui')
                    if 'beacon.png' in file_names:
                        os.rename(os.path.join(b + '/gui', 'beacon.png'), os.path.join(b + '/gui', str('beacon.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/gui/container'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/furnace.png', b + '/gui')
                    if 'furnace.png' in file_names:
                        os.rename(os.path.join(b + '/gui', 'furnace.png'), os.path.join(b + '/gui', str('furnace.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/gui/container'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/hopper.png', b + '/gui')
                    if 'hopper.png' in file_names:
                        os.rename(os.path.join(b + '/gui', 'hopper.png'), os.path.join(b + '/gui', str('hopper.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/gui/container'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/inventory.png', b + '/gui')
                    if 'inventory.png' in file_names:
                        os.rename(os.path.join(b + '/gui', 'inventory.png'),
                                  os.path.join(b + '/gui', str('inventory.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/gui/container'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/generic_54.png', b + '/gui')
                    if 'generic_54.png' in file_names:
                        os.rename(os.path.join(b + '/gui', 'generic_54.png'),
                                  os.path.join(b + '/gui', str('container.png')))
                except:
                    pass

                    # part of creative_inventory(gui_gminv)
                try:
                    file_path = a + '/assets/minecraft/textures/gui/container/creative_inventory'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/tab_inventory.png', b + '/gui/creative_inv')
                    if 'tab_inventory.png' in file_names:
                        os.rename(os.path.join(b + '/gui/creative_inv', 'tab_inventory.png'),
                                  os.path.join(b + '/gui/creative_inv', str('survival_inv.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/gui/container/creative_inventory'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/tab_item_search.png', b + '/gui/creative_inv')
                    if 'tab_item_search.png' in file_names:
                        os.rename(os.path.join(b + '/gui/creative_inv', 'tab_item_search.png'),
                                  os.path.join(b + '/gui/creative_inv', str('search.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/gui/container/creative_inventory'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/tab_items.png', b + '/gui/creative_inv')
                    if 'tab_items.png' in file_names:
                        os.rename(os.path.join(b + '/gui/creative_inv', 'tab_items.png'),
                                  os.path.join(b + '/gui/creative_inv', str('list_items.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/gui/container/creative_inventory'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/tabs.png', b + '/gui')
                    if 'tabs.png' in file_names:
                        os.rename(os.path.join(b + '/gui', 'tabs.png'),
                                  os.path.join(b + '/gui', str('allitems.png')))  # GUI위치로 변경
                except:
                    pass

                # part of GUI(GUI)
                try:
                    file_path = a + '/assets/minecraft/textures/gui'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/book.png', b + '/gui')
                    if 'book.png' in file_names:
                        os.rename(os.path.join(b + '/gui', 'book.png'), os.path.join(b + '/gui', str('book.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/gui'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/demo_background.png', b + '/gui')
                    if 'demo_background.png' in file_names:
                        os.rename(os.path.join(b + '/gui', 'demo_background.png'),
                                  os.path.join(b + '/gui', str('demo_bg.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/gui'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/options_background.png', b + '/gui')
                    if 'options_background.png' in file_names:
                        os.rename(os.path.join(b + '/gui', 'options_background.png'),
                                  os.path.join(b + '/gui', str('background.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/gui'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/widgets.png', b + '/gui')
                    if 'widgets.png' in file_names:
                        os.rename(os.path.join(b + '/gui', 'widgets.png'), os.path.join(b + '/gui', str('gui.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/gui'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/icons.png', b + '/gui')
                    if 'icons.png' in file_names:
                        os.rename(os.path.join(b + '/gui', 'icons.png'), os.path.join(b + '/gui', str('icons.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/gui'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/saturationicons.png', b + '/gui')
                    if 'saturationicons.png' in file_names:
                        os.rename(os.path.join(b + '/gui', 'saturationicons.png'),
                                  os.path.join(b + '/gui', str('icons1.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/gui'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/resource_packs.png', b + '/gui')
                    if 'resource_packs.png' in file_names:
                        os.rename(os.path.join(b + '/gui', 'resource_packs.png'),
                                  os.path.join(b + '/gui', str('slot.png')))
                except:
                    pass

                    # part of Entity(item)
                try:
                    file_path = a + '/assets/minecraft/textures/entity'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/arrow.png', b + '/item')
                    if 'arrow.png' in file_names:
                        os.rename(os.path.join(b + '/item', 'arrow.png'), os.path.join(b + '/item', str('arrows.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/entity'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/enchanting_table_book.png', b + '/item')
                    if 'enchanting_table_book.png' in file_names:
                        os.rename(os.path.join(b + '/item', 'enchanting_table_book.png'),
                                  os.path.join(b + '/item', str('book.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/entity'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/minecart.png', b + '/item')
                    if 'minecart.png' in file_names:
                        os.rename(os.path.join(b + '/item', 'minecart.png'), os.path.join(b + '/item', str('cart.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/entity'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/experience_orb.png', b + '/item')
                    if 'experience_orb.png' in file_names:
                        os.rename(os.path.join(b + '/item', 'experience_orb.png'),
                                  os.path.join(b + '/item', str('xporb.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/entity'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/boat.png', b + '/item')
                    if 'boat.png' in file_names:
                        os.rename(os.path.join(b + '/item', 'boat.png'), os.path.join(b + '/item', str('boat.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/entity'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/sign.png', b + '/item')
                    if 'sign.png' in file_names:
                        os.rename(os.path.join(b + '/item', 'sign.png'), os.path.join(b + '/item', str('sign.png')))
                except:
                    pass

                    # part of Entity_chest(item)
                try:
                    file_path = a + '/assets/minecraft/textures/entity/chest'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/trapped_double.png', b + '/item')
                    if 'trapped_double.png' in file_names:
                        os.rename(os.path.join(b + '/item', 'trapped_double.png'),
                                  os.path.join(b + '/item', str('trap_large.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/entity/chest'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/trapped.png', b + '/item')
                    if 'trapped.png' in file_names:
                        os.rename(os.path.join(b + '/item', 'trapped.png'),
                                  os.path.join(b + '/item', str('trap_small.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/entity/chest'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/normal.png', b + '/item')
                    if 'normal.png' in file_names:
                        os.rename(os.path.join(b + '/item', 'normal.png'), os.path.join(b + '/item', str('chest.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/entity/chest'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/ender.png', b + '/item')
                    if 'ender.png' in file_names:
                        os.rename(os.path.join(b + '/item', 'ender.png'),
                                  os.path.join(b + '/item', str('enderchest.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/entity/chest'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/normal_double.png', b + '/item')
                    if 'normal_double.png' in file_names:
                        os.rename(os.path.join(b + '/item', 'normal_double.png'),
                                  os.path.join(b + '/item', str('largechest.png')))
                except:
                    pass

                    # part of Entity_chest(mob)

                try:
                    file_path = a + '/assets/minecraft/textures/entity'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/steve.png', b + '/mob')
                    if 'steve.png' in file_names:
                        os.rename(os.path.join(b + '/mob', 'steve.png'), os.path.join(b + '/mob', str('char.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/entity'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/chicken.png', b + '/mob')
                    if 'chicken.png' in file_names:
                        os.rename(os.path.join(b + '/mob', 'chicken.png'), os.path.join(b + '/mob', str('chicken.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/entity'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/blaze.png', b + '/mob')
                    if 'blaze.png' in file_names:
                        os.rename(os.path.join(b + '/mob', 'blaze.png'), os.path.join(b + '/mob', str('fire.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/entity'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/zombie_pigman.png', b + '/mob')
                    if 'zombie_pigman.png' in file_names:
                        os.rename(os.path.join(b + '/mob', 'zombie_pigman.png'),
                                  os.path.join(b + '/mob', str('pigzombie.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/entity'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/snowman.png', b + '/mob')
                    if 'snowman.png' in file_names:
                        os.rename(os.path.join(b + '/mob', 'snowman.png'), os.path.join(b + '/mob', str('snowman.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/entity'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/spider_eyes.png', b + '/mob')
                    if 'spider_eyes.png' in file_names:
                        os.rename(os.path.join(b + '/mob', 'spider_eyes.png'),
                                  os.path.join(b + '/mob', str('spider_eyes.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/entity'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/squid.png', b + '/mob')
                    if 'squid.png' in file_names:
                        os.rename(os.path.join(b + '/mob', 'squid.png'), os.path.join(b + '/mob', str('squid.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/entity'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/iron_golem.png', b + '/mob')
                    if 'iron_golem.png' in file_names:
                        os.rename(os.path.join(b + '/mob', 'iron_golem.png'),
                                  os.path.join(b + '/mob', str('villager_golem.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/entity'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/witch.png', b + '/mob')
                    if 'witch.png' in file_names:
                        os.rename(os.path.join(b + '/mob', 'witch.png'), os.path.join(b + '/mob', str('witch.png')))
                except:
                    pass

                    # part of Entity_Cow(mob)

                try:
                    file_path = a + '/assets/minecraft/textures/entity/cow'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/cow.png', b + '/mob')
                    if 'cow.png' in file_names:
                        os.rename(os.path.join(b + '/mob', 'cow.png'), os.path.join(b + '/mob', str('cow.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/entity/cow'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/mooshroom.png', b + '/mob')
                    if 'mooshroom.png' in file_names:
                        os.rename(os.path.join(b + '/mob', 'mooshroom.png'),
                                  os.path.join(b + '/mob', str('redcow.png')))
                except:
                    pass

                    # part of Entity_Creeper(mob)

                try:
                    file_path = a + '/assets/minecraft/textures/entity/creeper'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/creeper.png', b + '/mob')
                    if 'creeper.png' in file_names:
                        os.rename(os.path.join(b + '/mob', 'creeper.png'), os.path.join(b + '/mob', str('creeper.png')))
                except:
                    pass

                    # part of Entity_endercrystal(mob/enderdragon)

                try:
                    file_path = a + '/assets/minecraft/textures/entity/endercrystal'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/endercrystal.png', b + '/mob/enderdragon')
                    if 'endercrystal.png' in file_names:
                        os.rename(os.path.join(b + '/mob/enderdragon', 'endercrystal.png'),
                                  os.path.join(b + '/mob/enderdragon', str('crystal.png')))
                except:
                    pass

                    # part of Entity_enderdragon(mob/enderdragon)

                try:
                    file_path = a + '/assets/minecraft/textures/entity/enderdragon'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/dragon.png', b + '/mob/enderdragon')
                    if 'dragon.png' in file_names:
                        os.rename(os.path.join(b + '/mob/enderdragon', 'dragon.png'),
                                  os.path.join(b + '/mob/enderdragon', str('ender.png')))
                except:
                    pass

                    # part of Entity_villager(mob/villager)

                try:
                    file_path = a + '/assets/minecraft/textures/entity/villager'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/butcher.png', b + '/mob/villager')
                    if 'butcher.png' in file_names:
                        os.rename(os.path.join(b + '/mob/villager', 'butcher.png'),
                                  os.path.join(b + '/mob/villager', str('butcher.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/entity/villager'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/farmer.png', b + '/mob/villager')
                    if 'farmer.png' in file_names:
                        os.rename(os.path.join(b + '/mob/villager', 'farmer.png'),
                                  os.path.join(b + '/mob/villager', str('farmer.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/entity/villager'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/librarian.png', b + '/mob/villager')
                    if 'librarian.png' in file_names:
                        os.rename(os.path.join(b + '/mob/villager', 'librarian.png'),
                                  os.path.join(b + '/mob/villager', str('librarian.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/entity/villager'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/priest.png', b + '/mob/villager')
                    if 'priest.png' in file_names:
                        os.rename(os.path.join(b + '/mob/villager', 'priest.png'),
                                  os.path.join(b + '/mob/villager', str('priest.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/entity/villager'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/smith.png', b + '/mob/villager')
                    if 'smith.png' in file_names:
                        os.rename(os.path.join(b + '/mob/villager', 'smith.png'),
                                  os.path.join(b + '/mob/villager', str('smith.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/entity/villager'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/villager.png', b + '/mob/villager')
                    if 'villager.png' in file_names:
                        os.rename(os.path.join(b + '/mob/villager', 'villager.png'),
                                  os.path.join(b + '/mob/villager', str('villager.png')))
                except:
                    pass

                    # part of Entity_enderman(mob)

                try:
                    file_path = a + '/assets/minecraft/textures/entity/enderman'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/enderman.png', b + '/mob')
                    if 'enderman.png' in file_names:
                        os.rename(os.path.join(b + '/mob', 'enderman.png'),
                                  os.path.join(b + '/mob', str('enderman.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/entity/enderman'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/enderman_eyes.png', b + '/mob')
                    if 'enderman_eyes.png' in file_names:
                        os.rename(os.path.join(b + '/mob', 'enderman_eyes.png'),
                                  os.path.join(b + '/mob', str('enderman_eyes.png')))
                except:
                    pass

                    # part of Entity_ghast(mob)

                try:
                    file_path = a + '/assets/minecraft/textures/entity/ghast'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/ghast.png', b + '/mob')
                    if 'ghast.png' in file_names:
                        os.rename(os.path.join(b + '/mob', 'ghast.png'), os.path.join(b + '/mob', str('ghast.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/entity/ghast'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/ghast_shooting.png', b + '/mob')
                    if 'ghast_shooting.png' in file_names:
                        os.rename(os.path.join(b + '/mob', 'ghast_shooting.png'),
                                  os.path.join(b + '/mob', str('ghast_fire.png')))
                except:
                    pass

                    # part of Entity_pig(mob)

                try:
                    file_path = a + '/assets/minecraft/textures/entity/pig'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/pig.png', b + '/mob')
                    if 'pig.png' in file_names:
                        os.rename(os.path.join(b + '/mob', 'pig.png'), os.path.join(b + '/mob', str('pig.png')))
                except:
                    pass

                    # part of Entity_sheep(mob)

                try:
                    file_path = a + '/assets/minecraft/textures/entity/sheep'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/sheep.png', b + '/mob')
                    if 'sheep.png' in file_names:
                        os.rename(os.path.join(b + '/mob', 'sheep.png'), os.path.join(b + '/mob', str('sheep.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/entity/sheep'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/sheep_fur.png', b + '/mob')
                    if 'sheep_fur.png' in file_names:
                        os.rename(os.path.join(b + '/mob', 'sheep_fur.png'),
                                  os.path.join(b + '/mob', str('sheep_fur.png')))
                except:
                    pass

                    # part of Entity_skeleton(mob)

                try:
                    file_path = a + '/assets/minecraft/textures/entity/skeleton'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/skeleton.png', b + '/mob')
                    if 'skeleton.png' in file_names:
                        os.rename(os.path.join(b + '/mob', 'skeleton.png'),
                                  os.path.join(b + '/mob', str('skeleton.png')))
                except:
                    pass

                    # part of Entity_slime(mob)

                try:
                    file_path = a + '/assets/minecraft/textures/entity/slime'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/slime.png', b + '/mob')
                    if 'slime.png' in file_names:
                        os.rename(os.path.join(b + '/mob', 'slime.png'), os.path.join(b + '/mob', str('slime.png')))
                except:
                    pass

                    # part of Entity_spider(mob)

                try:
                    file_path = a + '/assets/minecraft/textures/entity/spider'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/spider.png', b + '/mob')
                    if 'spider.png' in file_names:
                        os.rename(os.path.join(b + '/mob', 'spider.png'), os.path.join(b + '/mob', str('spider.png')))
                except:
                    pass

                    # part of Entity_wolf(mob)

                try:
                    file_path = a + '/assets/minecraft/textures/entity/wolf'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/wolf.png', b + '/mob')
                    if 'wolf.png' in file_names:
                        os.rename(os.path.join(b + '/mob', 'wolf.png'), os.path.join(b + '/mob', str('wolf.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/entity/wolf'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/wolf_angry.png', b + '/mob')
                    if 'wolf_angry.png' in file_names:
                        os.rename(os.path.join(b + '/mob', 'wolf_angry.png'),
                                  os.path.join(b + '/mob', str('wolf_angry.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/entity/wolf'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/wolf_tame.png', b + '/mob')
                    if 'wolf_tame.png' in file_names:
                        os.rename(os.path.join(b + '/mob', 'wolf_tame.png'),
                                  os.path.join(b + '/mob', str('wolf_tame.png')))
                except:
                    pass

                    # part of Entity_zombie(mob)

                try:
                    file_path = a + '/assets/minecraft/textures/entity/zombie'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/zombie.png', b + '/mob')
                    if 'zombie.png' in file_names:
                        os.rename(os.path.join(b + '/mob', 'zombie.png'), os.path.join(b + '/mob', str('zombie.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/entity/zombie'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/zombie_villager.png', b + '/mob')
                    if 'zombie_villager.png' in file_names:
                        os.rename(os.path.join(b + '/mob', 'zombie_villager.png'),
                                  os.path.join(b + '/mob', str('zombie_villager.png')))
                except:
                    pass

                    # part of environment(environment)

                try:
                    file_path = a + '/assets/minecraft/textures/environment'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/rain.png', b + '/environment')
                    if 'rain.png' in file_names:
                        os.rename(os.path.join(b + '/environment', 'rain.png'),
                                  os.path.join(b + '/environment', str('rain.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/mcpatcher/sky/world0'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/clouds.png', b + '/environment')
                    if 'clouds.png' in file_names:
                        os.rename(os.path.join(b + '/environment', 'clouds.png'),
                                  os.path.join(b + '/environment', str('clouds.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/mcpatcher/sky/world0'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/clouds2.png', b + '/environment')
                    if 'clouds2.png' in file_names:
                        os.rename(os.path.join(b + '/environment', 'clouds2.png'),
                                  os.path.join(b + '/environment', str('clouds2.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/mcpatcher/sky/world0'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/clouds1.png', b + '/environment')
                    if 'clouds1.png' in file_names:
                        os.rename(os.path.join(b + '/environment', 'clouds1.png'),
                                  os.path.join(b + '/environment', str('clouds1.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/mcpatcher/sky/world0'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/moon.png', b + '/environment')
                    if 'moon.png' in file_names:
                        os.rename(os.path.join(b + '/environment', 'moon.png'),
                                  os.path.join(b + '/environment', str('rain.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/mcpatcher/sky/world0'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/moon_phases.png', b + '/environment')
                    if 'moon_phases.png' in file_names:
                        os.rename(os.path.join(b + '/environment', 'moon_phases.png'),
                                  os.path.join(b + '/environment', str('moon_phases.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/mcpatcher/sky/world0'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/sun.png', b + '/environment')
                    if 'sun.png' in file_names:
                        os.rename(os.path.join(b + '/environment', 'sun.png'),
                                  os.path.join(b + '/environment', str('sun.png')))
                except:
                    pass

                # part of misc(misc)
                try:
                    file_path = a + '/assets/minecraft/textures/misc'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/enchanted_item_glint.png', b + '/misc')
                    if 'enchanted_item_glint.png' in file_names:
                        os.rename(os.path.join(b, 'enchanted_item_glint.png'), os.path.join(b, str('glint.png')))
                except:
                    pass

                    # part of particle(misc / texturePack)

                try:
                    file_path = a + '/assets/minecraft/textures/particle'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/particles.png', b)
                    if 'particles.png' in file_names:
                        os.rename(os.path.join(b, 'particles.png'), os.path.join(b, str('particles.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/particle'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/particles2.png', b)
                    if 'particles2.png' in file_names:
                        os.rename(os.path.join(b, 'particles2.png'), os.path.join(b, str('particles2.png')))
                except:
                    pass

                    # part of armor(armor)

                try:
                    file_path = a + '/assets/minecraft/textures/models/armor'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/chainmail_layer_1.png', b + '/armor')
                    if 'chainmail_layer_1.png' in file_names:
                        os.rename(os.path.join(b + '/armor', 'chainmail_layer_1.png'),
                                  os.path.join(b + '/armor', str('chain_1.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/models/armor'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/chainmail_layer_2.png', b + '/armor')
                    if 'chainmail_layer_2.png' in file_names:
                        os.rename(os.path.join(b + '/armor', 'chainmail_layer_2.png'),
                                  os.path.join(b + '/armor', str('chain_2.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/models/armor'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/diamond_layer_1.png', b + '/armor')
                    if 'diamond_layer_1.png' in file_names:
                        os.rename(os.path.join(b + '/armor', 'diamond_layer_1.png'),
                                  os.path.join(b + '/armor', str('diamond_1.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/models/armor'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/diamond_layer_2.png', b + '/armor')
                    if 'diamond_layer_2.png' in file_names:
                        os.rename(os.path.join(b + '/armor', 'diamond_layer_2.png'),
                                  os.path.join(b + '/armor', str('diamond_2.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/models/armor'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/gold_layer_1.png', b + '/armor')
                    if 'gold_layer_1.png' in file_names:
                        os.rename(os.path.join(b + '/armor', 'gold_layer_1.png'),
                                  os.path.join(b + '/armor', str('gold_1.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/models/armor'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/gold_layer_2.png', b + '/armor')
                    if 'gold_layer_2.png' in file_names:
                        os.rename(os.path.join(b + '/armor', 'gold_layer_2.png'),
                                  os.path.join(b + '/armor', str('gold_2.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/models/armor'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/iron_layer_1.png', b + '/armor')
                    if 'iron_layer_1.png' in file_names:
                        os.rename(os.path.join(b + '/armor', 'iron_layer_1.png'),
                                  os.path.join(b + '/armor', str('iron_1.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/models/armor'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/iron_layer_2.png', b + '/armor')
                    if 'iron_layer_2.png' in file_names:
                        os.rename(os.path.join(b + '/armor', 'iron_layer_2.png'),
                                  os.path.join(b + '/armor', str('iron_2.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/models/armor'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/leather_layer_1.png', b + '/armor')
                    if 'leather_layer_1.png' in file_names:
                        os.rename(os.path.join(b + '/armor', 'leather_layer_1.png'),
                                  os.path.join(b + '/armor', str('cloth_1.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/models/armor'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/leather_layer_1_overlay.png', b + '/armor')
                    if 'leather_layer_1_overlay.png' in file_names:
                        os.rename(os.path.join(b + '/armor', 'leather_layer_1_overlay.png'),
                                  os.path.join(b + '/armor', str('cloth_1_b.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/models/armor'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/leather_layer_2.png', b + '/armor')
                    if 'leather_layer_2.png' in file_names:
                        os.rename(os.path.join(b + '/armor', 'leather_layer_2.png'),
                                  os.path.join(b + '/armor', str('cloth_2.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/models/armor'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/leather_layer_2_overlay.png', b + '/armor')
                    if 'leather_layer_2_overlay.png' in file_names:
                        os.rename(os.path.join(b + '/armor', 'leather_layer_2_overlay.png'),
                                  os.path.join(b + '/armor', str('cloth_2_b.png')))
                except:
                    pass

                # part of blocks(blocks)
                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/rail_activator_powered.png', b + '/textures/blocks')
                    if 'rail_activator_powered.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'rail_activator_powered.png'),
                                  os.path.join(b + '/textures/blocks', str('activatorRail_powered.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/rail_activator.png', b + '/textures/blocks')
                    if 'rail_activator.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'rail_activator.png'),
                                  os.path.join(b + '/textures/blocks', str('activatorRail.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/anvil_base.png', b + '/textures/blocks')
                    if 'anvil_base.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'anvil_base.png'),
                                  os.path.join(b + '/textures/blocks', str('anvil_base.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/anvil_top_damaged_0.png', b + '/textures/blocks')
                    if 'anvil_top_damaged_0.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'anvil_top_damaged_0.png'),
                                  os.path.join(b + '/textures/blocks', str('anvil_top.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/anvil_top_damaged_1.png', b + '/textures/blocks')
                    if 'anvil_top_damaged_1.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'anvil_top_damaged_1.png'),
                                  os.path.join(b + '/textures/blocks', str('anvil_top_damaged_1.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/anvil_top_damaged_2.png', b + '/textures/blocks')
                    if 'anvil_top_damaged_2.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'anvil_top_damaged_2.png'),
                                  os.path.join(b + '/textures/blocks', str('anvil_top_damaged_2.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/beacon.png', b + '/textures/blocks')
                    if 'beacon.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'beacon.png'),
                                  os.path.join(b + '/textures/blocks', str('beacon.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/bed_feet_end.png', b + '/textures/blocks')
                    if 'bed_feet_end.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'bed_feet_end.png'),
                                  os.path.join(b + '/textures/blocks', str('bed_feet_end.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/bed_feet_side.png', b + '/textures/blocks')
                    if 'bed_feet_side.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'bed_feet_side.png'),
                                  os.path.join(b + '/textures/blocks', str('bed_feet_side.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/bed_feet_top.png', b + '/textures/blocks')
                    if 'bed_feet_top.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'bed_feet_top.png'),
                                  os.path.join(b + '/textures/blocks', str('bed_feet_top.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/bed_head_end.png', b + '/textures/blocks')
                    if 'bed_head_end.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'bed_head_end.png'),
                                  os.path.join(b + '/textures/blocks', str('bed_head_end.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/bed_head_side.png', b + '/textures/blocks')
                    if 'bed_head_side.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'bed_head_side.png'),
                                  os.path.join(b + '/textures/blocks', str('bed_head_side.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/bed_head_top.png', b + '/textures/blocks')
                    if 'bed_head_top.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'bed_head_top.png'),
                                  os.path.join(b + '/textures/blocks', str('bed_head_top.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/bedrock.png', b + '/textures/blocks')
                    if 'bedrock.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'bedrock.png'),
                                  os.path.join(b + '/textures/blocks', str('bedrock.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/diamond_block.png', b + '/textures/blocks')
                    if 'diamond_block.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'diamond_block.png'),
                                  os.path.join(b + '/textures/blocks', str('blockDiamond.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/emerald_block.png', b + '/textures/blocks')
                    if 'emerald_block.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'Emerald_block.png'),
                                  os.path.join(b + '/textures/blocks', str('blockEmerald.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/Gold_block.png', b + '/textures/blocks')
                    if 'Gold_block.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'Gold_block.png'),
                                  os.path.join(b + '/textures/blocks', str('blockGold.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/Iron_block.png', b + '/textures/blocks')
                    if 'Iron_block.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'Iron_block.png'),
                                  os.path.join(b + '/textures/blocks', str('blockIron.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/lapis_block.png', b + '/textures/blocks')
                    if 'lapis_block.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'lapis_block.png'),
                                  os.path.join(b + '/textures/blocks', str('blockLapis.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/redstone_block.png', b + '/textures/blocks')
                    if 'redstone_block.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'redstone_block.png'),
                                  os.path.join(b + '/textures/blocks', str('blockRedstone.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/bookshelf.png', b + '/textures/blocks')
                    if 'bookshelf.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'bookshelf.png'),
                                  os.path.join(b + '/textures/blocks', str('bookshelf.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/brick.png', b + '/textures/blocks')
                    if 'brick.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'brick.png'),
                                  os.path.join(b + '/textures/blocks', str('brick.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/cactus_bottom.png', b + '/textures/blocks')
                    if 'cactus_bottom.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'cactus_bottom.png'),
                                  os.path.join(b + '/textures/blocks', str('cactus_bottom.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/cactus_side.png', b + '/textures/blocks')
                    if 'cactus_side.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'cactus_side.png'),
                                  os.path.join(b + '/textures/blocks', str('cactus_side.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/cactus_top.png', b + '/textures/blocks')
                    if 'cactus_top.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'cactus_top.png'),
                                  os.path.join(b + '/textures/blocks', str('cactus_top.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/cake_bottom.png', b + '/textures/blocks')
                    if 'cake_bottom.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'cake_bottom.png'),
                                  os.path.join(b + '/textures/blocks', str('cake_bottom.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/cake_inner.png', b + '/textures/blocks')
                    if 'cake_inner.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'cake_inner.png'),
                                  os.path.join(b + '/textures/blocks', str('cake_inner.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/cake_side.png', b + '/textures/blocks')
                    if 'cake_side.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'cake_side.png'),
                                  os.path.join(b + '/textures/blocks', str('cake_side.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/cake_top.png', b + '/textures/blocks')
                    if 'cake_top.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'cake_top.png'),
                                  os.path.join(b + '/textures/blocks', str('cake_top.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/cauldron_bottom.png', b + '/textures/blocks')
                    if 'cauldron_bottom.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'cauldron_bottom.png'),
                                  os.path.join(b + '/textures/blocks', str('cauldron_bottom.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/cauldron_inner.png', b + '/textures/blocks')
                    if 'cauldron_inner.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'cauldron_inner.png'),
                                  os.path.join(b + '/textures/blocks', str('cauldron_inner.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/cauldron_side.png', b + '/textures/blocks')
                    if 'cauldron_side.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'cauldron_side.png'),
                                  os.path.join(b + '/textures/blocks', str('cauldron_side.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/cauldron_top.png', b + '/textures/blocks')
                    if 'cauldron_top.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'cauldron_top.png'),
                                  os.path.join(b + '/textures/blocks', str('cauldron_top.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/clay.png', b + '/textures/blocks')
                    if 'clay.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'clay.png'),
                                  os.path.join(b + '/textures/blocks', str('clay.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/brewing_stand.png', b + '/textures/blocks')
                    if 'brewing_stand.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'brewing_stand.png'),
                                  os.path.join(b + '/textures/blocks', str('brewingStand.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/deadbush.png', b + '/textures/blocks')
                    if 'deadbush.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'deadbush.png'),
                                  os.path.join(b + '/textures/blocks', str('deadbush.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/pumpkin_stem_disconnected.png', b + '/textures/blocks')
                    if 'pumpkin_stem_disconnected.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'pumpkin_stem_disconnected.png'),
                                  os.path.join(b + '/textures/blocks', str('stem_straight.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/pumpkin_stem_connected.png', b + '/textures/blocks')
                    if 'pumpkin_stem_connected.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'pumpkin_stem_connected.png'),
                                  os.path.join(b + '/textures/blocks', str('stem_bent.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/brewing_stand_base.png', b + '/textures/blocks')
                    if 'brewing_stand_base.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'brewing_stand_base.png'),
                                  os.path.join(b + '/textures/blocks', str('brewingstand_base.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/carrots_stage_0.png', b + '/textures/blocks')
                    if 'carrots_stage_0.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'carrots_stage_0.png'),
                                  os.path.join(b + '/textures/blocks', str('carrots_0.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/carrots_stage_1.png', b + '/textures/blocks')
                    if 'carrots_stage_1.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'carrots_stage_1.png'),
                                  os.path.join(b + '/textures/blocks', str('carrots_1.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/carrots_stage_2.png', b + '/textures/blocks')
                    if 'carrots_stage_2.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'carrots_stage_2.png'),
                                  os.path.join(b + '/textures/blocks', str('carrots_2.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/carrots_stage_3.png', b + '/textures/blocks')
                    if 'carrots_stage_3.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'carrots_stage_3.png'),
                                  os.path.join(b + '/textures/blocks', str('carrots_3.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/wool_colored_white.png', b + '/textures/blocks')
                    if 'wool_colored_white.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'wool_colored_white.png'),
                                  os.path.join(b + '/textures/blocks', str('cloth_0.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/wool_colored_orange.png', b + '/textures/blocks')
                    if 'wool_colored_orange.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'wool_colored_orange.png'),
                                  os.path.join(b + '/textures/blocks', str('cloth_1.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/wool_colored_magenta.png', b + '/textures/blocks')
                    if 'wool_colored_magenta.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'wool_colored_magenta.png'),
                                  os.path.join(b + '/textures/blocks', str('cloth_2.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/wool_colored_light_blue.png', b + '/textures/blocks')
                    if 'wool_colored_light_blue.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'wool_colored_light_blue.png'),
                                  os.path.join(b + '/textures/blocks', str('cloth_3.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/wool_colored_yellow.png', b + '/textures/blocks')
                    if 'wool_colored_yellow.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'wool_colored_yellow.png'),
                                  os.path.join(b + '/textures/blocks', str('cloth_4.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/wool_colored_lime.png', b + '/textures/blocks')
                    if 'wool_colored_lime.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'wool_colored_lime.png'),
                                  os.path.join(b + '/textures/blocks', str('cloth_5.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/wool_colored_pink.png', b + '/textures/blocks')
                    if 'wool_colored_pink.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'wool_colored_pink.png'),
                                  os.path.join(b + '/textures/blocks', str('cloth_6.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/wool_colored_gray.png', b + '/textures/blocks')
                    if 'wool_colored_gray.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'wool_colored_gray.png'),
                                  os.path.join(b + '/textures/blocks', str('cloth_7.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/wool_colored_silver.png', b + '/textures/blocks')
                    if 'wool_colored_silver.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'wool_colored_silver.png'),
                                  os.path.join(b + '/textures/blocks', str('cloth_8.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/wool_colored_cyan.png', b + '/textures/blocks')
                    if 'wool_colored_cyan.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'wool_colored_cyan.png'),
                                  os.path.join(b + '/textures/blocks', str('cloth_9.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/wool_colored_purple.png', b + '/textures/blocks')
                    if 'wool_colored_purple.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'wool_colored_purple.png'),
                                  os.path.join(b + '/textures/blocks', str('cloth_10.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/wool_colored_blue.png', b + '/textures/blocks')
                    if 'wool_colored_blue.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'wool_colored_blue.png'),
                                  os.path.join(b + '/textures/blocks', str('cloth_11.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/wool_colored_brown.png', b + '/textures/blocks')
                    if 'wool_colored_brown.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'wool_colored_brown.png'),
                                  os.path.join(b + '/textures/blocks', str('cloth_12.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/wool_colored_green.png', b + '/textures/blocks')
                    if 'wool_colored_green.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'wool_colored_green.png'),
                                  os.path.join(b + '/textures/blocks', str('cloth_13.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/wool_colored_red.png', b + '/textures/blocks')
                    if 'wool_colored_red.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'wool_colored_red.png'),
                                  os.path.join(b + '/textures/blocks', str('cloth_14.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/wool_colored_black.png', b + '/textures/blocks')
                    if 'wool_colored_black.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'wool_colored_black.png'),
                                  os.path.join(b + '/textures/blocks', str('cloth_15.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/cocoa_stage_0.png', b + '/textures/blocks')
                    if 'cocoa_stage_0.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'cocoa_stage_0.png'),
                                  os.path.join(b + '/textures/blocks', str('cocoa_0.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/cocoa_stage_1.png', b + '/textures/blocks')
                    if 'cocoa_stage_1.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'cocoa_stage_1.png'),
                                  os.path.join(b + '/textures/blocks', str('cocoa_1.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/cocoa_stage_2.png', b + '/textures/blocks')
                    if 'cocoa_stage_2.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'cocoa_stage_2.png'),
                                  os.path.join(b + '/textures/blocks', str('cocoa_2.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/command_block.png', b + '/textures/blocks')
                    if 'command_block.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'command_block.png'),
                                  os.path.join(b + '/textures/blocks', str('commandblock.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/comparator_off.png', b + '/textures/blocks')
                    if 'comparator_off.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'comparator_off.png'),
                                  os.path.join(b + '/textures/blocks', str('comparator.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/comparator_on.png', b + '/textures/blocks')
                    if 'comparator_on.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'comparator_on.png'),
                                  os.path.join(b + '/textures/blocks', str('comparator_lit.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/wheat_stage_0.png', b + '/textures/blocks')
                    if 'wheat_stage_0.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'wheat_stage_0.png'),
                                  os.path.join(b + '/textures/blocks', str('crops_0.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/wheat_stage_1.png', b + '/textures/blocks')
                    if 'wheat_stage_1.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'wheat_stage_1.png'),
                                  os.path.join(b + '/textures/blocks', str('crops_1.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/wheat_stage_2.png', b + '/textures/blocks')
                    if 'wheat_stage_2.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'wheat_stage_2.png'),
                                  os.path.join(b + '/textures/blocks', str('crops_2.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/wheat_stage_3.png', b + '/textures/blocks')
                    if 'wheat_stage_3.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'wheat_stage_3.png'),
                                  os.path.join(b + '/textures/blocks', str('crops_3.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/wheat_stage_4.png', b + '/textures/blocks')
                    if 'wheat_stage_4.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'wheat_stage_4.png'),
                                  os.path.join(b + '/textures/blocks', str('crops_4.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/wheat_stage_5.png', b + '/textures/blocks')
                    if 'wheat_stage_5.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'wheat_stage_5.png'),
                                  os.path.join(b + '/textures/blocks', str('crops_5.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/wheat_stage_6.png', b + '/textures/blocks')
                    if 'wheat_stage_6.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'wheat_stage_6.png'),
                                  os.path.join(b + '/textures/blocks', str('crops_06.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/wheat_stage_7.png', b + '/textures/blocks')
                    if 'wheat_stage_7.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'wheat_stage_7.png'),
                                  os.path.join(b + '/textures/blocks', str('crops_7.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/daylight_detector_side.png', b + '/textures/blocks')
                    if 'daylight_detector_side.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'daylight_detector_side.png'),
                                  os.path.join(b + '/textures/blocks', str('daylightdetector_side.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/daylight_detector_top.png', b + '/textures/blocks')
                    if 'daylight_detector_top.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'daylight_detector_top.png'),
                                  os.path.join(b + '/textures/blocks', str('daylightdetector_top.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/destroy_stage_0.png', b + '/textures/blocks')
                    if 'destroy_stage_0.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'destroy_stage_0.png'),
                                  os.path.join(b + '/textures/blocks', str('destroy_0.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/destroy_stage_1.png', b + '/textures/blocks')
                    if 'destroy_stage_1.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'destroy_stage_1.png'),
                                  os.path.join(b + '/textures/blocks', str('destroy_1.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/destroy_stage_2.png', b + '/textures/blocks')
                    if 'destroy_stage_2.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'destroy_stage_2.png'),
                                  os.path.join(b + '/textures/blocks', str('destroy_2.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/destroy_stage_3.png', b + '/textures/blocks')
                    if 'destroy_stage_3.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'destroy_stage_3.png'),
                                  os.path.join(b + '/textures/blocks', str('destroy_3.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/destroy_stage_4.png', b + '/textures/blocks')
                    if 'destroy_stage_4.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'destroy_stage_4.png'),
                                  os.path.join(b + '/textures/blocks', str('destroy_4.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/destroy_stage_5.png', b + '/textures/blocks')
                    if 'destroy_stage_5.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'destroy_stage_5.png'),
                                  os.path.join(b + '/textures/blocks', str('destroy_5.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/destroy_stage_6.png', b + '/textures/blocks')
                    if 'destroy_stage_6.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'destroy_stage_6.png'),
                                  os.path.join(b + '/textures/blocks', str('destroy_6.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/destroy_stage_7.png', b + '/textures/blocks')
                    if 'destroy_stage_7.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'destroy_stage_7.png'),
                                  os.path.join(b + '/textures/blocks', str('destroy_7.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/destroy_stage_8.png', b + '/textures/blocks')
                    if 'destroy_stage_8.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'destroy_stage_8.png'),
                                  os.path.join(b + '/textures/blocks', str('destroy_8.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/destroy_stage_9.png', b + '/textures/blocks')
                    if 'destroy_stage_9.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'destroy_stage_9.png'),
                                  os.path.join(b + '/textures/blocks', str('destroy_9.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/rail_detector.png', b + '/textures/blocks')
                    if 'rail_detector.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'rail_detector.png'),
                                  os.path.join(b + '/textures/blocks', str('detectorRail.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/rail_detector_powered.png', b + '/textures/blocks')
                    if 'rail_detector_powered.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'rail_detector_powered.png'),
                                  os.path.join(b + '/textures/blocks', str('detectorRail_on.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/dirt.png', b + '/textures/blocks')
                    if 'dirt.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'dirt.png'),
                                  os.path.join(b + '/textures/blocks', str('dirt.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/dispenser_front_horizontal.png', b + '/textures/blocks')
                    if 'dispenser_front_horizontal.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'dispenser_front_horizontal.png'),
                                  os.path.join(b + '/textures/blocks', str('dispenser_front.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/dispenser_front_vertical.png', b + '/textures/blocks')
                    if 'dispenser_front_vertical.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'dispenser_front_vertical.png'),
                                  os.path.join(b + '/textures/blocks', str('dispenser_front_vertical.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/door_iron_lower.png', b + '/textures/blocks')
                    if 'door_iron_lower.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'door_iron_lower.png'),
                                  os.path.join(b + '/textures/blocks', str('doorIron_lower.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/door_iron_upper.png', b + '/textures/blocks')
                    if 'door_iron_upper.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'door_iron_upper.png'),
                                  os.path.join(b + '/textures/blocks', str('doorIron_upper.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/door_wood_lower.png', b + '/textures/blocks')
                    if 'door_wood_lower.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'door_wood_lower.png'),
                                  os.path.join(b + '/textures/blocks', str('doorWood_lower.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/door_wood_upper.png', b + '/textures/blocks')
                    if 'door_wood_upper.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'door_wood_upper.png'),
                                  os.path.join(b + '/textures/blocks', str('doorWood_upper.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/dragon_egg.png', b + '/textures/blocks')
                    if 'dragon_egg.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'dragon_egg.png'),
                                  os.path.join(b + '/textures/blocks', str('drangonEgg.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/dropper_front_horizontal.png', b + '/textures/blocks')
                    if 'dropper_front_horizontal.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'dropper_front_horizontal.png'),
                                  os.path.join(b + '/textures/blocks', str('dropper_front.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/dropper_front_vertical.png', b + '/textures/blocks')
                    if 'dropper_front_vertical.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'dropper_front_vertical.png'),
                                  os.path.join(b + '/textures/blocks', str('dropper_front_vertical.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/enchanting_table_bottom.png', b + '/textures/blocks')
                    if 'enchanting_table_bottom.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'enchanting_table_bottom.png'),
                                  os.path.join(b + '/textures/blocks', str('enchantment_bottom.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/enchanting_table_side.png', b + '/textures/blocks')
                    if 'enchanting_table_side.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'enchanting_table_side.png'),
                                  os.path.join(b + '/textures/blocks', str('enchantment_side.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/enchanting_table_top.png', b + '/textures/blocks')
                    if 'enchanting_table_top.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'enchanting_table_top.png'),
                                  os.path.join(b + '/textures/blocks', str('enchantment_top.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/endframe_eye.png', b + '/textures/blocks')
                    if 'endframe_eye.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'endframe_eye.png'),
                                  os.path.join(b + '/textures/blocks', str('endframe_eye.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/endframe_side.png', b + '/textures/blocks')
                    if 'endframe_side.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'endframe_side.png'),
                                  os.path.join(b + '/textures/blocks', str('endframe_side.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/endframe_top.png', b + '/textures/blocks')
                    if 'endframe_top.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'endframe_top.png'),
                                  os.path.join(b + '/textures/blocks', str('endframe_top.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/farmland_dry.png', b + '/textures/blocks')
                    if 'farmland_dry.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'farmland_dry.png'),
                                  os.path.join(b + '/textures/blocks', str('farmland_dry.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/farmland_wet.png', b + '/textures/blocks')
                    if 'farmland_wet.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'farmland_wet.png'),
                                  os.path.join(b + '/textures/blocks', str('farmland_wet.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/iron_bars.png', b + '/textures/blocks')
                    if 'iron_bars.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'iron_bars.png'),
                                  os.path.join(b + '/textures/blocks', str('fenceIron.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/fern.png', b + '/textures/blocks')
                    if 'fern.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'fern.png'),
                                  os.path.join(b + '/textures/blocks', str('fern.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/fire_layer_0.png', b + '/textures/blocks')
                    if 'fire_layer_0.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'fire_layer_0.png'),
                                  os.path.join(b + '/textures/blocks', str('fire_0.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/fire_layer_1.png', b + '/textures/blocks')
                    if 'fire_layer_1.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'fire_layer_1.png'),
                                  os.path.join(b + '/textures/blocks', str('fire_1.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/flower_dandelion.png', b + '/textures/blocks')
                    if 'flower_dandelion.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'flower_dandelion.png'),
                                  os.path.join(b + '/textures/blocks', str('flower.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/flower_pot.png', b + '/textures/blocks')
                    if 'flower_pot.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'flower_pot.png'),
                                  os.path.join(b + '/textures/blocks', str('flowerpot.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/furnace_front_off.png', b + '/textures/blocks')
                    if 'furnace_front_off.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'furnace_front_off.png'),
                                  os.path.join(b + '/textures/blocks', str('furnace_front.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/furnace_front_on.png', b + '/textures/blocks')
                    if 'furnace_front_on.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'furnace_front_on.png'),
                                  os.path.join(b + '/textures/blocks', str('furnace_front_lit.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/furnace_side.png', b + '/textures/blocks')
                    if 'furnace_side.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'furnace_side.png'),
                                  os.path.join(b + '/textures/blocks', str('furnace_side.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/furnace_top.png', b + '/textures/blocks')
                    if 'furnace_top.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'furnace_top.png'),
                                  os.path.join(b + '/textures/blocks', str('furnace_top.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/glass.png', b + '/textures/blocks')
                    if 'glass.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'glass.png'),
                                  os.path.join(b + '/textures/blocks', str('glass.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/rail_golden.png', b + '/textures/blocks')
                    if 'rail_golden.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'rail_golden.png'),
                                  os.path.join(b + '/textures/blocks', str('goldenRail.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/rail_golden_powered.png', b + '/textures/blocks')
                    if 'rail_golden_powered.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'rail_golden_powered.png'),
                                  os.path.join(b + '/textures/blocks', str('goldenRail_powered.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/grass_side.png', b + '/textures/blocks')
                    if 'grass_side.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'grass_side.png'),
                                  os.path.join(b + '/textures/blocks', str('grass_side.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/grass_side_overlay.png', b + '/textures/blocks')
                    if 'grass_side_overlay.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'grass_side_overlay.png'),
                                  os.path.join(b + '/textures/blocks', str('grass_side_overlay.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/grass_top.png', b + '/textures/blocks')
                    if 'grass_top.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'grass_top.png'),
                                  os.path.join(b + '/textures/blocks', str('grass_top.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/gravel.png', b + '/textures/blocks')
                    if 'gravel.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'gravel.png'),
                                  os.path.join(b + '/textures/blocks', str('gravel.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/netherrack.png', b + '/textures/blocks')
                    if 'netherrack.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'netherrack.png'),
                                  os.path.join(b + '/textures/blocks', str('hellrock.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/soul_sand.png', b + '/textures/blocks')
                    if 'soul_sand.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'soul_sand.png'),
                                  os.path.join(b + '/textures/blocks', str('hellsand.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/hopper_outside.png', b + '/textures/blocks')
                    if 'hopper_outside.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'hopper_outside.png'),
                                  os.path.join(b + '/textures/blocks', str('hopper.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/hopper_inside.png', b + '/textures/blocks')
                    if 'hopper_inside.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'hopper_inside.png'),
                                  os.path.join(b + '/textures/blocks', str('hopper_inside.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/hopper_top.png', b + '/textures/blocks')
                    if 'hopper_top.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'hopper_top.png'),
                                  os.path.join(b + '/textures/blocks', str('hopper_top.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/ice.png', b + '/textures/blocks')
                    if 'ice.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'ice.png'),
                                  os.path.join(b + '/textures/blocks', str('ice.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/itemframe_background.png', b + '/textures/blocks')
                    if 'itemframe_background.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'itemframe_background.png'),
                                  os.path.join(b + '/textures/blocks', str('itemframe_back.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/jukebox_top.png', b + '/textures/blocks')
                    if 'jukebox_top.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'jukebox_top.png'),
                                  os.path.join(b + '/textures/blocks', str('jukebox_top.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/ladder.png', b + '/textures/blocks')
                    if 'ladder.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'ladder.png'),
                                  os.path.join(b + '/textures/blocks', str('ladder.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/lava_still.png', b + '/textures/blocks')
                    if 'lava_still.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'lava_still.png'),
                                  os.path.join(b + '/textures/blocks', str('lava.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/lava_flow.png', b + '/textures/blocks')
                    if 'lava_flow.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'lava_flow.png'),
                                  os.path.join(b + '/textures/blocks', str('lava_flow.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/leaves_birch.png', b + '/textures/blocks')
                    if 'leaves_birch.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'leaves_birch.png'),
                                  os.path.join(b + '/textures/blocks', str('leaves.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/leaves_jungle.png', b + '/textures/blocks')
                    if 'leaves_jungle.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'leaves_jungle.png'),
                                  os.path.join(b + '/textures/blocks', str('leaves_jungle.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/leaves_jungle_opaque.png', b + '/textures/blocks')
                    if 'leaves_jungle_opaque.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'leaves_jungle_opaque.png'),
                                  os.path.join(b + '/textures/blocks', str('leaves_jungle_opaque.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/leaves_birch_opaque.png', b + '/textures/blocks')
                    if 'leaves_birch_opaque.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'leaves_birch_opaque.png'),
                                  os.path.join(b + '/textures/blocks', str('leaves_opaque.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/leaves_spruce.png', b + '/textures/blocks')
                    if 'leaves_spruce.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'leaves_spruce.png'),
                                  os.path.join(b + '/textures/blocks', str('leaves_spruce.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/leaves_spruce_opaque.png', b + '/textures/blocks')
                    if 'leaves_spruce_opaque.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'leaves_spruce_opaque.png'),
                                  os.path.join(b + '/textures/blocks', str('leaves_spruce_opaque.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/lever.png', b + '/textures/blocks')
                    if 'lever.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'lever.png'),
                                  os.path.join(b + '/textures/blocks', str('lever.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/glowstone.png', b + '/textures/blocks')
                    if 'glowstone.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'glowstone.png'),
                                  os.path.join(b + '/textures/blocks', str('lightgem.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/melon_side.png', b + '/textures/blocks')
                    if 'melon_side.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'melon_side.png'),
                                  os.path.join(b + '/textures/blocks', str('melon_side.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/melon_top.png', b + '/textures/blocks')
                    if 'melon_top.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'melon_top.png'),
                                  os.path.join(b + '/textures/blocks', str('melon_top.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/mob_spawner.png', b + '/textures/blocks')
                    if 'mob_spawner.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'mob_spawner.png'),
                                  os.path.join(b + '/textures/blocks', str('mobspawner.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/mushroom_brown.png', b + '/textures/blocks')
                    if 'mushroom_brown.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'mushroom_brown.png'),
                                  os.path.join(b + '/textures/blocks', str('mushroom_brown.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/mushroom_block_inside.png', b + '/textures/blocks')
                    if 'mushroom_block_inside.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'mushroom_block_inside.png'),
                                  os.path.join(b + '/textures/blocks', str('mushroom_inside.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/mushroom_red.png', b + '/textures/blocks')
                    if 'mushroom_red.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'mushroom_red.png'),
                                  os.path.join(b + '/textures/blocks', str('mushroom_red.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/mushroom_block_skin_brown.png', b + '/textures/blocks')
                    if 'mushroom_block_skin_brown.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'mushroom_block_skin_brown.png'),
                                  os.path.join(b + '/textures/blocks', str('mushroom_skin_brown.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/mushroom_block_skin_red.png', b + '/textures/blocks')
                    if 'mushroom_block_skin_red.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'mushroom_block_skin_red.png'),
                                  os.path.join(b + '/textures/blocks', str('mushroom_skin_red.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/mushroom_block_skin_stem.png', b + '/textures/blocks')
                    if 'mushroom_block_skin_stem.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'mushroom_block_skin_stem.png'),
                                  os.path.join(b + '/textures/blocks', str('mushroom_skin_stem.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/noteblock.png', b + '/textures/blocks')
                    if 'noteblock.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'noteblock.png'),
                                  os.path.join(b + '/textures/blocks', str('musicblock.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/mycelium_side.png', b + '/textures/blocks')
                    if 'mycelium_side.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'mycelium_side.png'),
                                  os.path.join(b + '/textures/blocks', str('mycel_side.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/mycelium_top.png', b + '/textures/blocks')
                    if 'mycelium_top.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'mycelium_top.png'),
                                  os.path.join(b + '/textures/blocks', str('mycel_top.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/nether_brick.png', b + '/textures/blocks')
                    if 'nether_brick.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'nether_brick.png'),
                                  os.path.join(b + '/textures/blocks', str('netherBrick.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/quartz_ore.png', b + '/textures/blocks')
                    if 'quartz_ore.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'quartz_ore.png'),
                                  os.path.join(b + '/textures/blocks', str('netherquartz.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/nether_wart_stage_0.png', b + '/textures/blocks')
                    if 'nether_wart_stage_0.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'nether_wart_stage_0.png'),
                                  os.path.join(b + '/textures/blocks', str('netherStalk_0.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/nether_wart_stage_1.png', b + '/textures/blocks')
                    if 'nether_wart_stage_1.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'nether_wart_stage_1.png'),
                                  os.path.join(b + '/textures/blocks', str('netherStalk_1.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/nether_wart_stage_2.png', b + '/textures/blocks')
                    if 'nether_wart_stage_2.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'nether_wart_stage_2.png'),
                                  os.path.join(b + '/textures/blocks', str('netherStalk_2.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/obsidian.png', b + '/textures/blocks')
                    if 'obsidian.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'obsidian.png'),
                                  os.path.join(b + '/textures/blocks', str('obsidian.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/coal_ore.png', b + '/textures/blocks')
                    if 'coal_ore.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'coal_ore.png'),
                                  os.path.join(b + '/textures/blocks', str('oreCoal.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/diamond_ore.png', b + '/textures/blocks')
                    if 'diamond_ore.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'diamond_ore.png'),
                                  os.path.join(b + '/textures/blocks', str('oreDiamond.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/emerald_ore.png', b + '/textures/blocks')
                    if 'emerald_ore.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'emerald_ore.png'),
                                  os.path.join(b + '/textures/blocks', str('oreEmerald.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/gold_ore.png', b + '/textures/blocks')
                    if 'gold_ore.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'gold_ore.png'),
                                  os.path.join(b + '/textures/blocks', str('oreGold.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/iron_ore.png', b + '/textures/blocks')
                    if 'iron_ore.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'iron_ore.png'),
                                  os.path.join(b + '/textures/blocks', str('oreIron.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/lapis_ore.png', b + '/textures/blocks')
                    if 'lapis_ore.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'lapis_ore.png'),
                                  os.path.join(b + '/textures/blocks', str('oreLapis.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/redstone_ore.png', b + '/textures/blocks')
                    if 'redstone_ore.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'redstone_ore.png'),
                                  os.path.join(b + '/textures/blocks', str('oreRedstone.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/piston_bottom.png', b + '/textures/blocks')
                    if 'piston_bottom.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'piston_bottom.png'),
                                  os.path.join(b + '/textures/blocks', str('piston_bottom.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/piston_inner.png', b + '/textures/blocks')
                    if 'piston_inner.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'piston_inner.png'),
                                  os.path.join(b + '/textures/blocks', str('piston_inner_top.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/piston_side.png', b + '/textures/blocks')
                    if 'piston_side.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'piston_side.png'),
                                  os.path.join(b + '/textures/blocks', str('piston_side.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/piston_top_normal.png', b + '/textures/blocks')
                    if 'piston_top_normal.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'piston_top_normal.png'),
                                  os.path.join(b + '/textures/blocks', str('piston_top.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/piston_top_sticky.png', b + '/textures/blocks')
                    if 'piston_top_sticky.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'piston_top_sticky.png'),
                                  os.path.join(b + '/textures/blocks', str('piston_top_sticky.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/portal.png', b + '/textures/blocks')
                    if 'portal.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'portal.png'),
                                  os.path.join(b + '/textures/blocks', str('portal.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/potatoes_stage_0.png', b + '/textures/blocks')
                    if 'potatoes_stage_0.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'potatoes_stage_0.png'),
                                  os.path.join(b + '/textures/blocks', str('potatoes_0.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/potatoes_stage_1.png', b + '/textures/blocks')
                    if 'potatoes_stage_1.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'potatoes_stage_1.png'),
                                  os.path.join(b + '/textures/blocks', str('potatoes_1.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/potatoes_stage_2.png', b + '/textures/blocks')
                    if 'potatoes_stage_2.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'potatoes_stage_2.png'),
                                  os.path.join(b + '/textures/blocks', str('potatoes_2.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/potatoes_stage_3.png', b + '/textures/blocks')
                    if 'potatoes_stage_3.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'potatoes_stage_3.png'),
                                  os.path.join(b + '/textures/blocks', str('potatoes_3.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/pumpkin_face_off.png', b + '/textures/blocks')
                    if 'pumpkin_face_off.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'pumpkin_face_off.png'),
                                  os.path.join(b + '/textures/blocks', str('pumpkin_face.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/pumpkin_face_on.png', b + '/textures/blocks')
                    if 'pumpkin_face_on.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'pumpkin_face_on.png'),
                                  os.path.join(b + '/textures/blocks', str('pumpkin_jack.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/pumpkin_side.png', b + '/textures/blocks')
                    if 'pumpkin_side.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'pumpkin_side.png'),
                                  os.path.join(b + '/textures/blocks', str('pumpkin_side.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/pumpkin_top.png', b + '/textures/blocks')
                    if 'pumpkin_top.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'pumpkin_top.png'),
                                  os.path.join(b + '/textures/blocks', str('pumpkin_top.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/quartz_block_bottom.png', b + '/textures/blocks')
                    if 'quartz_block_bottom.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'quartz_block_bottom.png'),
                                  os.path.join(b + '/textures/blocks', str('quartzblock_bottom.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/quartz_block_chiseled.png', b + '/textures/blocks')
                    if 'quartz_block_chiseled.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'quartz_block_chiseled.png'),
                                  os.path.join(b + '/textures/blocks', str('quartzblock_chiseled.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/quartz_block_chiseled_top.png', b + '/textures/blocks')
                    if 'quartz_block_chiseled_top.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'quartz_block_chiseled_top.png'),
                                  os.path.join(b + '/textures/blocks', str('quartzblock_chiseled_top.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/quartz_block_lines.png', b + '/textures/blocks')
                    if 'quartz_block_lines.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'quartz_block_lines.png'),
                                  os.path.join(b + '/textures/blocks', str('quartzblock_lines.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/quartz_block_lines_top.png', b + '/textures/blocks')
                    if 'quartz_block_lines_top.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'quartz_block_lines_top.png'),
                                  os.path.join(b + '/textures/blocks', str('quartzblock_lines_top.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/quartz_block_side.png', b + '/textures/blocks')
                    if 'quartz_block_side.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'quartz_block_side.png'),
                                  os.path.join(b + '/textures/blocks', str('quartzblock_side.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/quartz_block_top.png', b + '/textures/blocks')
                    if 'quartz_block_top.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'quartz_block_top.png'),
                                  os.path.join(b + '/textures/blocks', str('quartzblock_top.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/rail_normal.png', b + '/textures/blocks')
                    if 'rail_normal.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'rail_normal.png'),
                                  os.path.join(b + '/textures/blocks', str('rail.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/rail_normal_turned.png', b + '/textures/blocks')
                    if 'rail_normal_turned.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'rail_normal_turned.png'),
                                  os.path.join(b + '/textures/blocks', str('rail_turn.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/redstone_dust_cross.png', b + '/textures/blocks')
                    if 'redstone_dust_cross.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'redstone_dust_cross.png'),
                                  os.path.join(b + '/textures/blocks', str('redstoneDust_cross.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/redstone_dust_line.png', b + '/textures/blocks')
                    if 'redstone_dust_line.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'redstone_dust_line.png'),
                                  os.path.join(b + '/textures/blocks', str('redstoneDust_line.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/redstone_lamp_off.png', b + '/textures/blocks')
                    if 'redstone_lamp_off.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'redstone_lamp_off.png'),
                                  os.path.join(b + '/textures/blocks', str('redstoneLight.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/redstone_lamp_on.png', b + '/textures/blocks')
                    if 'redstone_lamp_on.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'redstone_lamp_on.png'),
                                  os.path.join(b + '/textures/blocks', str('redstoneLight_lit.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/redstone_torch_off.png', b + '/textures/blocks')
                    if 'redstone_torch_off.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'redstone_torch_off.png'),
                                  os.path.join(b + '/textures/blocks', str('redtorch.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/redstone_torch_on.png', b + '/textures/blocks')
                    if 'redstone_torch_on.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'redstone_torch_on.png'),
                                  os.path.join(b + '/textures/blocks', str('redtorch_lit.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/reeds.png', b + '/textures/blocks')
                    if 'reeds.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'reeds.png'),
                                  os.path.join(b + '/textures/blocks', str('reeds.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/repeater_off.png', b + '/textures/blocks')
                    if 'repeater_off.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'repeater_off.png'),
                                  os.path.join(b + '/textures/blocks', str('repeater.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/repeater_on.png', b + '/textures/blocks')
                    if 'repeater_on.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'repeater_on.png'),
                                  os.path.join(b + '/textures/blocks', str('repeater_lit.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/flower_rose.png', b + '/textures/blocks')
                    if 'flower_rose.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'flower_rose.png'),
                                  os.path.join(b + '/textures/blocks', str('rose.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/sand.png', b + '/textures/blocks')
                    if 'sand.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'sand.png'),
                                  os.path.join(b + '/textures/blocks', str('sand.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/sandstone_bottom.png', b + '/textures/blocks')
                    if 'sandstone_bottom.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'sandstone_bottom.png'),
                                  os.path.join(b + '/textures/blocks', str('sandstone_bottom.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/sandstone_carved.png', b + '/textures/blocks')
                    if 'sandstone_carved.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'sandstone_carved.png'),
                                  os.path.join(b + '/textures/blocks', str('sandstone_carved.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/sandstone_normal.png', b + '/textures/blocks')
                    if 'sandstone_normal.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'sandstone_normal.png'),
                                  os.path.join(b + '/textures/blocks', str('sandstone_side.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/sandstone_smooth.png', b + '/textures/blocks')
                    if 'sandstone_smooth.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'sandstone_smooth.png'),
                                  os.path.join(b + '/textures/blocks', str('sandstone_smooth.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/sandstone_top.png', b + '/textures/blocks')
                    if 'sandstone_top.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'sandstone_top.png'),
                                  os.path.join(b + '/textures/blocks', str('sandstone_top.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/sapling_oak.png', b + '/textures/blocks')
                    if 'sapling_oak.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'sapling_oak.png'),
                                  os.path.join(b + '/textures/blocks', str('sapling.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/sapling_birch.png', b + '/textures/blocks')
                    if 'sapling_birch.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'sapling_birch.png'),
                                  os.path.join(b + '/textures/blocks', str('sapling_birch.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/sapling_jungle.png', b + '/textures/blocks')
                    if 'sapling_jungle.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'sapling_jungle.png'),
                                  os.path.join(b + '/textures/blocks', str('sapling_jungle.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/sapling_spruce.png', b + '/textures/blocks')
                    if 'sapling_spruce.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'sapling_spruce.png'),
                                  os.path.join(b + '/textures/blocks', str('sapling_spruce.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/snow.png', b + '/textures/blocks')
                    if 'snow.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'snow.png'),
                                  os.path.join(b + '/textures/blocks', str('snow.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/grass_side_snowed.png', b + '/textures/blocks')
                    if 'grass_side_snowed.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'grass_side_snowed.png'),
                                  os.path.join(b + '/textures/blocks', str('snow_side.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/sponge.png', b + '/textures/blocks')
                    if 'sponge.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'sponge.png'),
                                  os.path.join(b + '/textures/blocks', str('sponge.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/stone.png', b + '/textures/blocks')
                    if 'stone.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'stone.png'),
                                  os.path.join(b + '/textures/blocks', str('stone.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/cobblestone.png', b + '/textures/blocks')
                    if 'cobblestone.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'cobblestone.png'),
                                  os.path.join(b + '/textures/blocks', str('stonebrick.png')))

                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/stonebrick.png', b + '/textures/blocks')
                    if 'stonebrick.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'stonebrick.png'),
                                  os.path.join(b + '/textures/blocks', str('stonebricksmooth.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/stonebrick_carved.png', b + '/textures/blocks')
                    if 'stonebrick_carved.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'stonebrick_carved.png'),
                                  os.path.join(b + '/textures/blocks', str('stonebricksmooth_carved.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/stonebrick_cracked.png', b + '/textures/blocks')
                    if 'stonebrick_cracked.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'stonebrick_cracked.png'),
                                  os.path.join(b + '/textures/blocks', str('stonebricksmooth_cracked.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/stonebrick_mossy.png', b + '/textures/blocks')
                    if 'stonebrick_mossy.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'stonebrick_mossy.png'),
                                  os.path.join(b + '/textures/blocks', str('stonebricksmooth_mossy.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/cobblestone_mossy.png', b + '/textures/blocks')
                    if 'cobblestone_mossy.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'cobblestone_mossy.png'),
                                  os.path.join(b + '/textures/blocks', str('stoneMoss.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/stone_slab_side.png', b + '/textures/blocks')
                    if 'stone_slab_side.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'stone_slab_side.png'),
                                  os.path.join(b + '/textures/blocks', str('stoneslab_side.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/stone_slab_top.png', b + '/textures/blocks')
                    if 'stone_slab_top.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'stone_slab_top.png'),
                                  os.path.join(b + '/textures/blocks', str('stoneslab_top.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/tallgrass.png', b + '/textures/blocks')
                    if 'tallgrass.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'tallgrass.png'),
                                  os.path.join(b + '/textures/blocks', str('tallgrass.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/glass_pane_top.png', b + '/textures/blocks')
                    if 'glass_pane_top.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'glass_pane_top.png'),
                                  os.path.join(b + '/textures/blocks', str('thinglass_top.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/tnt_bottom.png', b + '/textures/blocks')
                    if 'tnt_bottom.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'tnt_bottom.png'),
                                  os.path.join(b + '/textures/blocks', str('tnt_bottom.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/tnt_side.png', b + '/textures/blocks')
                    if 'tnt_side.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'tnt_side.png'),
                                  os.path.join(b + '/textures/blocks', str('tnt_side.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/tnt_top.png', b + '/textures/blocks')
                    if 'tnt_top.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'tnt_top.png'),
                                  os.path.join(b + '/textures/blocks', str('tnt_top.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/torch_on.png', b + '/textures/blocks')
                    if 'torch_on.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'torch_on.png'),
                                  os.path.join(b + '/textures/blocks', str('torch.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/trapdoor.png', b + '/textures/blocks')
                    if 'trapdoor.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'trapdoor.png'),
                                  os.path.join(b + '/textures/blocks', str('trapdoor.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/log_birch.png', b + '/textures/blocks')
                    if 'log_birch.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'log_birch.png'),
                                  os.path.join(b + '/textures/blocks', str('tree_birch.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/log_jungle.png', b + '/textures/blocks')
                    if 'log_jungle.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'log_jungle.png'),
                                  os.path.join(b + '/textures/blocks', str('tree_jungle.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/log_oak.png', b + '/textures/blocks')
                    if 'log_oak.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'log_oak.png'),
                                  os.path.join(b + '/textures/blocks', str('tree_side.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/log_spruce.png', b + '/textures/blocks')
                    if 'log_spruce.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'log_spruce.png'),
                                  os.path.join(b + '/textures/blocks', str('tree_spruce.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/log_oak_top.png', b + '/textures/blocks')
                    if 'log_oak_top.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'log_oak_top.png'),
                                  os.path.join(b + '/textures/blocks', str('tree_top.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/trip_wire.png', b + '/textures/blocks')
                    if 'trip_wire.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'trip_wire.png'),
                                  os.path.join(b + '/textures/blocks', str('tripwire.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/trip_wire_source.png', b + '/textures/blocks')
                    if 'trip_wire_source.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'trip_wire_source.png'),
                                  os.path.join(b + '/textures/blocks', str('tripwireSource.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/water_still.png', b + '/textures/blocks')
                    if 'water_still.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'water_still.png'),
                                  os.path.join(b + '/textures/blocks', str('water.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/water_flow.png', b + '/textures/blocks')
                    if 'water_flow.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'water_flow.png'),
                                  os.path.join(b + '/textures/blocks', str('water_flow.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/waterlily.png', b + '/textures/blocks')
                    if 'waterlily.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'waterlily.png'),
                                  os.path.join(b + '/textures/blocks', str('waterlily.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/web.png', b + '/textures/blocks')
                    if 'web.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'web.png'),
                                  os.path.join(b + '/textures/blocks', str('web.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/end_stone.png', b + '/textures/blocks')
                    if 'end_stone.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'end_stone.png'),
                                  os.path.join(b + '/textures/blocks', str('whitestone.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/planks_oak.png', b + '/textures/blocks')
                    if 'planks_oak.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'planks_oak.png'),
                                  os.path.join(b + '/textures/blocks', str('wood.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/planks_birch.png', b + '/textures/blocks')
                    if 'planks_birch.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'planks_birch.png'),
                                  os.path.join(b + '/textures/blocks', str('wood_birch.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/planks_jungle.png', b + '/textures/blocks')
                    if 'planks_jungle.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'planks_jungle.png'),
                                  os.path.join(b + '/textures/blocks', str('wood_jungle.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/planks_spruce.png', b + '/textures/blocks')
                    if 'planks_spruce.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'planks_spruce.png'),
                                  os.path.join(b + '/textures/blocks', str('wood_spruce.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/crafting_table_front.png', b + '/textures/blocks')
                    if 'crafting_table_front.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'crafting_table_front.png'),
                                  os.path.join(b + '/textures/blocks', str('workbench_front.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/blocks'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/crafting_table_side.png', b + '/textures/blocks')
                    if 'crafting_table_side.png' in file_names:
                        os.rename(os.path.join(b + '/textures/blocks', 'crafting_table_side.png'),
                                  os.path.join(b + '/textures/blocks', str('workbench_side.png')))
                except:
                    pass

                # 드디어.. items 부분..

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/apple.png', b + '/textures/items')
                    if 'apple.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'apple.png'),
                                  os.path.join(b + '/textures/items', str('apple.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/apple_golden.png', b + '/textures/items')
                    if 'apple_golden.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'apple_Golden.png'),
                                  os.path.join(b + '/textures/items', str('appleGold.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/arrow.png', b + '/textures/items')
                    if 'arrow.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'arrow.png'),
                                  os.path.join(b + '/textures/items', str('arrow.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/bed.png', b + '/textures/items')
                    if 'bed.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'bed.png'),
                                  os.path.join(b + '/textures/items', str('bed.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/beef_cooked.png', b + '/textures/items')
                    if 'beef_cooked.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'beef_cooked.png'),
                                  os.path.join(b + '/textures/items', str('beefcooked.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/beef_raw.png', b + '/textures/items')
                    if 'beef_raw.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'beef_raw.png'),
                                  os.path.join(b + '/textures/items', str('beefraw.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/blaze_powder.png', b + '/textures/items')
                    if 'blaze_powder.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'blaze_powder.png'),
                                  os.path.join(b + '/textures/items', str('blazepowder.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/blaze_rod.png', b + '/textures/items')
                    if 'blaze_rod.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'blaze_rod.png'),
                                  os.path.join(b + '/textures/items', str('blazerod.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/boat.png', b + '/textures/items')
                    if 'boat.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'boat.png'),
                                  os.path.join(b + '/textures/items', str('boat.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/bone.png', b + '/textures/items')
                    if 'bone.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'bone.png'),
                                  os.path.join(b + '/textures/items', str('bone.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/book_normal.png', b + '/textures/items')
                    if 'book_normal.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'book_normal.png'),
                                  os.path.join(b + '/textures/items', str('book.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/chainmail_boots.png', b + '/textures/items')
                    if 'chainmail_boots.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'chainmail_boots.png'),
                                  os.path.join(b + '/textures/items', str('bootschain.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/leather_boots.png', b + '/textures/items')
                    if 'leather_boots.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'leather_boots.png'),
                                  os.path.join(b + '/textures/items', str('bootsCloth.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/leather_boots_overlay.png', b + '/textures/items')
                    if 'leather_boots_overlay.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'leather_boots_overlay.png'),
                                  os.path.join(b + '/textures/items', str('bootsCloth_overlay.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/diamond_boots.png', b + '/textures/items')
                    if 'diamond_boots.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'diamond_boots.png'),
                                  os.path.join(b + '/textures/items', str('bootsDiamond.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/gold_boots.png', b + '/textures/items')
                    if 'gold_boots.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'gold_boots.png'),
                                  os.path.join(b + '/textures/items', str('bootsgold.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/iron_boots.png', b + '/textures/items')
                    if 'iron_boots.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'iron_boots.png'),
                                  os.path.join(b + '/textures/items', str('bootsiron.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/bow_standby.png', b + '/textures/items')
                    if 'bow_standby.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'bow_standby.png'),
                                  os.path.join(b + '/textures/items', str('bow.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/bow_pulling_0.png', b + '/textures/items')
                    if 'bow_pulling_0.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'bow_pulling_0.png'),
                                  os.path.join(b + '/textures/items', str('bow_pull_0.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/bow_pulling_1.png', b + '/textures/items')
                    if 'bow_pulling_1.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'bow_pulling_1.png'),
                                  os.path.join(b + '/textures/items', str('bow_pull_1.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/bow_pulling_2.png', b + '/textures/items')
                    if 'bow_pulling_2.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'bow_pulling_2.png'),
                                  os.path.join(b + '/textures/items', str('bow_pull_2.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/bowl.png', b + '/textures/items')
                    if 'bowl.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'bowl.png'),
                                  os.path.join(b + '/textures/items', str('bowl.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/bread.png', b + '/textures/items')
                    if 'bread.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'bread.png'),
                                  os.path.join(b + '/textures/items', str('bread.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/brewing_stand.png', b + '/textures/items')
                    if 'brewing_stand.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'brewing_stand.png'),
                                  os.path.join(b + '/textures/items', str('brewingStand.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/brick.png', b + '/textures/items')
                    if 'brick.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'brick.png'),
                                  os.path.join(b + '/textures/items', str('brick.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/bucket_empty.png', b + '/textures/items')
                    if 'bucket_empty.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'bucket_empty.png'),
                                  os.path.join(b + '/textures/items', str('bucket.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/bucket_lava.png', b + '/textures/items')
                    if 'bucket_lava.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'bucket_lava.png'),
                                  os.path.join(b + '/textures/items', str('bucketLava.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/bucket_water.png', b + '/textures/items')
                    if 'bucket_water.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'bucket_water.png'),
                                  os.path.join(b + '/textures/items', str('bucketwater.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/cake.png', b + '/textures/items')
                    if 'cake.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'cake.png'),
                                  os.path.join(b + '/textures/items', str('cake.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/carrot_golden.png', b + '/textures/items')
                    if 'carrot_golden.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'carrot_golden.png'),
                                  os.path.join(b + '/textures/items', str('carrotGolden.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/carrot_on_a_stick.png', b + '/textures/items')
                    if 'carrot_on_a_stick.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'carrot_on_a_stick.png'),
                                  os.path.join(b + '/textures/items', str('carrotOnAStick.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/carrot.png', b + '/textures/items')
                    if 'carrot.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'carrot.png'),
                                  os.path.join(b + '/textures/items', str('carrots.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/cauldron.png', b + '/textures/items')
                    if 'cauldron.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'cauldron.png'),
                                  os.path.join(b + '/textures/items', str('cauldron.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/chainmail_chestplate.png', b + '/textures/items')
                    if 'chainmail_chestplate.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'chainmail_chestplate.png'),
                                  os.path.join(b + '/textures/items', str('chestplateChain.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/leather_chestplate.png', b + '/textures/items')
                    if 'leather_chestplate.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'leather_chestplate.png'),
                                  os.path.join(b + '/textures/items', str('chestplatecloth.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/leather_chestplate_overlay.png', b + '/textures/items')
                    if 'leather_chestplate_overlay.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'leather_chestplate_overlay.png'),
                                  os.path.join(b + '/textures/items', str('chestplateCloth_overlay.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/diamond_chestplate.png', b + '/textures/items')
                    if 'diamond_chestplate.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'diamond_chestplate.png'),
                                  os.path.join(b + '/textures/items', str('chestplateDiamond.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/gold_chestplate.png', b + '/textures/items')
                    if 'gold_chestplate.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'gold_chestplate.png'),
                                  os.path.join(b + '/textures/items', str('chestplategold.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/iron_chestplate.png', b + '/textures/items')
                    if 'iron_chestplate.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'iron_chestplate.png'),
                                  os.path.join(b + '/textures/items', str('chestplateiron.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/chicken_cooked.png', b + '/textures/items')
                    if 'chicken_cooked.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'chicken_cooked.png'),
                                  os.path.join(b + '/textures/items', str('chickenCooked.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/chicken_raw.png', b + '/textures/items')
                    if 'chicken_raw.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'chicken_raw.png'),
                                  os.path.join(b + '/textures/items', str('chickenraw.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/clay_ball.png', b + '/textures/items')
                    if 'clay_ball.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'clay_ball.png'),
                                  os.path.join(b + '/textures/items', str('clay.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/clock.png', b + '/textures/items')
                    if 'clock.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'clock.png'),
                                  os.path.join(b + '/textures/items', str('clock.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/coal.png', b + '/textures/items')
                    if 'coal.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'coal.png'),
                                  os.path.join(b + '/textures/items', str('coal.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/comparator.png', b + '/textures/items')
                    if 'comparator.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'comparator.png'),
                                  os.path.join(b + '/textures/items', str('comparator.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/compass.png', b + '/textures/items')
                    if 'compass.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'compass.png'),
                                  os.path.join(b + '/textures/items', str('compass.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/cookie.png', b + '/textures/items')
                    if 'cookie.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'cookie.png'),
                                  os.path.join(b + '/textures/items', str('cookie.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/diamond.png', b + '/textures/items')
                    if 'diamond.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'diamond.png'),
                                  os.path.join(b + '/textures/items', str('diamond.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/repeater.png', b + '/textures/items')
                    if 'repeater.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'repeater.png'),
                                  os.path.join(b + '/textures/items', str('diode.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/door_iron.png', b + '/textures/items')
                    if 'door_iron.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'door_iron.png'),
                                  os.path.join(b + '/textures/items', str('doorIron.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/door_wood.png', b + '/textures/items')
                    if 'door_wood.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'door_wood.png'),
                                  os.path.join(b + '/textures/items', str('doorWood.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/dye_powder_black.png', b + '/textures/items')
                    if 'dye_powder_black.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'dye_powder_black.png'),
                                  os.path.join(b + '/textures/items', str('dyePowder_black.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/dye_powder_blue.png', b + '/textures/items')
                    if 'dye_powder_blue.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'dye_powder_blue.png'),
                                  os.path.join(b + '/textures/items', str('dyePowder_blue.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/dye_powder_brown.png', b + '/textures/items')
                    if 'dye_powder_brown.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'dye_powder_brown.png'),
                                  os.path.join(b + '/textures/items', str('dyePowder_brown.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/dye_powder_cyan.png', b + '/textures/items')
                    if 'dye_powder_cyan.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'dye_powder_cyan.png'),
                                  os.path.join(b + '/textures/items', str('dyePowder_cyan.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/dye_powder_gray.png', b + '/textures/items')
                    if 'dye_powder_gray.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'dye_powder_gray.png'),
                                  os.path.join(b + '/textures/items', str('dyePowder_gray.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/dye_powder_green.png', b + '/textures/items')
                    if 'dye_powder_green.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'dye_powder_green.png'),
                                  os.path.join(b + '/textures/items', str('dyePowder_green.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/dye_powder_light_blue.png', b + '/textures/items')
                    if 'dye_powder_light_blue.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'dye_powder_light_blue.png'),
                                  os.path.join(b + '/textures/items', str('dyePowder_lightBlue.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/dye_powder_lime.png', b + '/textures/items')
                    if 'dye_powder_lime.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'dye_powder_lime.png'),
                                  os.path.join(b + '/textures/items', str('dyePowder_lime.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/dye_powder_magenta.png', b + '/textures/items')
                    if 'dye_powder_magenta.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'dye_powder_magenta.png'),
                                  os.path.join(b + '/textures/items', str('dyePowder_magenta.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/dye_powder_orange.png', b + '/textures/items')
                    if 'dye_powder_orange.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'dye_powder_orange.png'),
                                  os.path.join(b + '/textures/items', str('dyePowder_orange.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/dye_powder_pink.png', b + '/textures/items')
                    if 'dye_powder_pink.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'dye_powder_pink.png'),
                                  os.path.join(b + '/textures/items', str('dyePowder_pink.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/dye_powder_purple.png', b + '/textures/items')
                    if 'dye_powder_purple.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'dye_powder_purple.png'),
                                  os.path.join(b + '/textures/items', str('dyePowder_purple.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/dye_powder_red.png', b + '/textures/items')
                    if 'dye_powder_red.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'dye_powder_red.png'),
                                  os.path.join(b + '/textures/items', str('dyePowder_red.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/dye_powder_silver.png', b + '/textures/items')
                    if 'dye_powder_silver.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'dye_powder_silver.png'),
                                  os.path.join(b + '/textures/items', str('dyePowder_silver.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/dye_powder_white.png', b + '/textures/items')
                    if 'dye_powder_white.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'dye_powder_white.png'),
                                  os.path.join(b + '/textures/items', str('dyePowder_white.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/dye_powder_yellow.png', b + '/textures/items')
                    if 'dye_powder_yellow.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'dye_powder_yellow.png'),
                                  os.path.join(b + '/textures/items', str('dyePowder_yellow.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/egg.png', b + '/textures/items')
                    if 'egg.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'egg.png'),
                                  os.path.join(b + '/textures/items', str('egg.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/emerald.png', b + '/textures/items')
                    if 'emerald.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'emerald.png'),
                                  os.path.join(b + '/textures/items', str('emerald.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/map_empty.png', b + '/textures/items')
                    if 'map_empty.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'map_empty.png'),
                                  os.path.join(b + '/textures/items', str('emptymap.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/book_enchanted.png', b + '/textures/items')
                    if 'book_enchanted.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'book_enchanted.png'),
                                  os.path.join(b + '/textures/items', str('enchantedBook.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/ender_pearl.png', b + '/textures/items')
                    if 'ender_pearl.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'ender_pearl.png'),
                                  os.path.join(b + '/textures/items', str('enderpearl.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/experience_bottle.png', b + '/textures/items')
                    if 'experience_bottle.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'experience_bottle.png'),
                                  os.path.join(b + '/textures/items', str('expbottle.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/ender_eye.png', b + '/textures/items')
                    if 'ender_eye.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'ender_eye.png'),
                                  os.path.join(b + '/textures/items', str('eyeofender.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/feather.png', b + '/textures/items')
                    if 'feather.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'feather.png'),
                                  os.path.join(b + '/textures/items', str('feather.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/spider_eye_fermented.png', b + '/textures/items')
                    if 'spider_eye_fermented.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'spider_eye_fermented.png'),
                                  os.path.join(b + '/textures/items', str('fermentedSpiderEye.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/fireball.png', b + '/textures/items')
                    if 'fireball.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'fireball.png'),
                                  os.path.join(b + '/textures/items', str('fireball.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/fireworks.png', b + '/textures/items')
                    if 'fireworks.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'fireworks.png'),
                                  os.path.join(b + '/textures/items', str('fireworks.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/fireworks_charge.png', b + '/textures/items')
                    if 'fireworks_charge.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'fireworks_charge.png'),
                                  os.path.join(b + '/textures/items', str('fireworksCharge.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/fireworks_charge_overlay.png', b + '/textures/items')
                    if 'fireworks_charge_overlay.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'fireworks_charge_overlay.png'),
                                  os.path.join(b + '/textures/items', str('fireworksCharge_overlay.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/fish_cod_cooked.png', b + '/textures/items')
                    if 'fish_cod_cooked.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'fish_cod_cooked.png'),
                                  os.path.join(b + '/textures/items', str('fishCooked.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/fish_cod_raw.png', b + '/textures/items')
                    if 'fish_cod_raw.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'fish_cod_raw.png'),
                                  os.path.join(b + '/textures/items', str('fishraw.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/fishing_rod_uncast.png', b + '/textures/items')
                    if 'fishing_rod_uncast.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'fishing_rod_uncast.png'),
                                  os.path.join(b + '/textures/items', str('fishingRod.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/fishing_rod_cast.png', b + '/textures/items')
                    if 'fishing_rod_cast.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'fishing_rod_cast.png'),
                                  os.path.join(b + '/textures/items', str('fishingRod_empty.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/flint.png', b + '/textures/items')
                    if 'flint.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'flint.png'),
                                  os.path.join(b + '/textures/items', str('flint.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/flint_and_steel.png', b + '/textures/items')
                    if 'flint_and_steel.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'flint_and_steel.png'),
                                  os.path.join(b + '/textures/items', str('flintAndSteel.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/flower_pot.png', b + '/textures/items')
                    if 'flower_pot.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'flower_pot.png'),
                                  os.path.join(b + '/textures/items', str('flowerpot.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/item_frame.png', b + '/textures/items')
                    if 'item_frame.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'item_frame.png'),
                                  os.path.join(b + '/textures/items', str('frame.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/ghast_tear.png', b + '/textures/items')
                    if 'ghast_tear.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'ghast_tear.png'),
                                  os.path.join(b + '/textures/items', str('ghastTear.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/potion_bottle_empty.png', b + '/textures/items')
                    if 'potion_bottle_empty.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'potion_bottle_empty.png'),
                                  os.path.join(b + '/textures/items', str('glassBottle.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/gold_nugget.png', b + '/textures/items')
                    if 'gold_nugget.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'gold_nugget.png'),
                                  os.path.join(b + '/textures/items', str('goldnugget.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/diamond_axe.png', b + '/textures/items')
                    if 'diamond_axe.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'diamond_axe.png'),
                                  os.path.join(b + '/textures/items', str('hatchetDiamond.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/gold_axe.png', b + '/textures/items')
                    if 'gold_axe.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'gold_axe.png'),
                                  os.path.join(b + '/textures/items', str('hatchetGold.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/iron_axe.png', b + '/textures/items')
                    if 'iron_axe.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'iron_axe.png'),
                                  os.path.join(b + '/textures/items', str('hatchetIron.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/stone_axe.png', b + '/textures/items')
                    if 'stone_axe.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'stone_axe.png'),
                                  os.path.join(b + '/textures/items', str('hatchetStone.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/wood_axe.png', b + '/textures/items')
                    if 'wood_axe.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'wood_axe.png'),
                                  os.path.join(b + '/textures/items', str('hatchetWood.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/chainmail_helmet.png', b + '/textures/items')
                    if 'chainmail_helmet.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'chainmail_helmet.png'),
                                  os.path.join(b + '/textures/items', str('helmetChain.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/leather_helmet.png', b + '/textures/items')
                    if 'leather_helmet.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'leather_helmet.png'),
                                  os.path.join(b + '/textures/items', str('helmetCloth.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/leather_helmet_overlay.png', b + '/textures/items')
                    if 'leather_helmet_overlay.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'leather_helmet_overlay.png'),
                                  os.path.join(b + '/textures/items', str('helmetCloth_overlay.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/diamond_helmet.png', b + '/textures/items')
                    if 'diamond_helmet.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'diamond_helmet.png'),
                                  os.path.join(b + '/textures/items', str('helmetDiamond.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/gold_helmet.png', b + '/textures/items')
                    if 'gold_helmet.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'gold_helmet.png'),
                                  os.path.join(b + '/textures/items', str('helmetGold.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/iron_helmet.png', b + '/textures/items')
                    if 'iron_helmet.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'iron_helmet.png'),
                                  os.path.join(b + '/textures/items', str('helmetIron.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/diamond_hoe.png', b + '/textures/items')
                    if 'diamond_hoe.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'diamond_hoe.png'),
                                  os.path.join(b + '/textures/items', str('hoeDiamond.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/gold_hoe.png', b + '/textures/items')
                    if 'gold_hoe.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'gold_hoe.png'),
                                  os.path.join(b + '/textures/items', str('hoeGold.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/iron_hoe.png', b + '/textures/items')
                    if 'iron_hoe.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'iron_hoe.png'),
                                  os.path.join(b + '/textures/items', str('hoeiron.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/stone_hoe.png', b + '/textures/items')
                    if 'stone_hoe.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'stone_hoe.png'),
                                  os.path.join(b + '/textures/items', str('hoeStone.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/wood_hoe.png', b + '/textures/items')
                    if 'wood_hoe.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'wood_hoe.png'),
                                  os.path.join(b + '/textures/items', str('hoeWood.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/hopper.png', b + '/textures/items')
                    if 'hopper.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'hopper.png'),
                                  os.path.join(b + '/textures/items', str('hopper.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/gold_ingot.png', b + '/textures/items')
                    if 'gold_ingot.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'gold_ingot.png'),
                                  os.path.join(b + '/textures/items', str('ingotGold.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/iron_ingot.png', b + '/textures/items')
                    if 'iron_ingot.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'iron_ingot.png'),
                                  os.path.join(b + '/textures/items', str('ingotIron.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/leather.png', b + '/textures/items')
                    if 'leather.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'leather.png'),
                                  os.path.join(b + '/textures/items', str('leather.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/chainmail_leggings.png', b + '/textures/items')
                    if 'chainmail_leggings.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'chainmail_leggings.png'),
                                  os.path.join(b + '/textures/items', str('leggingsChain.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/leather_leggings.png', b + '/textures/items')
                    if 'leather_leggings.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'leather_leggings.png'),
                                  os.path.join(b + '/textures/items', str('leggingsCloth.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/leather_leggings_overlay.png', b + '/textures/items')
                    if 'leather_leggings_overlay.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'leather_leggings_overlay.png'),
                                  os.path.join(b + '/textures/items', str('leggingsCloth_overlay.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/diamond_leggings.png', b + '/textures/items')
                    if 'diamond_leggings.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'diamond_leggings.png'),
                                  os.path.join(b + '/textures/items', str('leggingsDiamond.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/gold_leggings.png', b + '/textures/items')
                    if 'gold_leggings.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'gold_leggings.png'),
                                  os.path.join(b + '/textures/items', str('leggingsGold.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/iron_leggings.png', b + '/textures/items')
                    if 'iron_leggings.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'iron_leggings.png'),
                                  os.path.join(b + '/textures/items', str('leggingsIron.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/magma_cream.png', b + '/textures/items')
                    if 'magma_cream.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'magma_cream.png'),
                                  os.path.join(b + '/textures/items', str('magmaCream.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/map_filled.png', b + '/textures/items')
                    if 'map_filled.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'map_filled.png'),
                                  os.path.join(b + '/textures/items', str('map.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/melon.png', b + '/textures/items')
                    if 'melon.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'melon.png'),
                                  os.path.join(b + '/textures/items', str('melon.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/bucket_milk.png', b + '/textures/items')
                    if 'bucket_milk.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'bucket_milk.png'),
                                  os.path.join(b + '/textures/items', str('milk.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/minecart_normal.png', b + '/textures/items')
                    if 'minecart_normal.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'minecart_normal.png'),
                                  os.path.join(b + '/textures/items', str('minecart.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/minecart_chest.png', b + '/textures/items')
                    if 'minecart_chest.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'minecart_chest.png'),
                                  os.path.join(b + '/textures/items', str('minecartChest.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/minecart_furnace.png', b + '/textures/items')
                    if 'minecart_furnace.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'minecart_furnace.png'),
                                  os.path.join(b + '/textures/items', str('minecartFurnace.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/minecart_hopper.png', b + '/textures/items')
                    if 'minecart_hopper.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'minecart_hopper.png'),
                                  os.path.join(b + '/textures/items', str('minecartHopper.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/minecart_tnt.png', b + '/textures/items')
                    if 'minecart_tnt.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'minecart_tnt.png'),
                                  os.path.join(b + '/textures/items', str('minecartTnt.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/spawn_egg.png', b + '/textures/items')
                    if 'spawn_egg.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'spawn_egg.png'),
                                  os.path.join(b + '/textures/items', str('monsterPlacer.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/spawn_egg_overlay.png', b + '/textures/items')
                    if 'spawn_egg_overlay.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'spawn_egg_overlay.png'),
                                  os.path.join(b + '/textures/items', str('monsterPlacer_overlay.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/mushroom_stew.png', b + '/textures/items')
                    if 'mushroom_stew.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'mushroom_stew.png'),
                                  os.path.join(b + '/textures/items', str('mushroomStew.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/netherbrick.png', b + '/textures/items')
                    if 'netherbrick.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'netherbrick.png'),
                                  os.path.join(b + '/textures/items', str('netherbrick.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/quartz.png', b + '/textures/items')
                    if 'quartz.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'quartz.png'),
                                  os.path.join(b + '/textures/items', str('netherquartz.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/nether_wart.png', b + '/textures/items')
                    if 'nether_wart.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'nether_wart.png'),
                                  os.path.join(b + '/textures/items', str('netherStalkSeeds.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/nether_star.png', b + '/textures/items')
                    if 'nether_star.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'nether_star.png'),
                                  os.path.join(b + '/textures/items', str('netherStar.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/painting.png', b + '/textures/items')
                    if 'painting.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'painting.png'),
                                  os.path.join(b + '/textures/items', str('painting.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/paper.png', b + '/textures/items')
                    if 'paper.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'paper.png'),
                                  os.path.join(b + '/textures/items', str('paper.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/diamond_pickaxe.png', b + '/textures/items')
                    if 'diamond_pickaxe.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'diamond_pickaxe.png'),
                                  os.path.join(b + '/textures/items', str('pickaxeDiamond.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/gold_pickaxe.png', b + '/textures/items')
                    if 'gold_pickaxe.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'gold_pickaxe.png'),
                                  os.path.join(b + '/textures/items', str('pickaxeGold.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/iron_pickaxe.png', b + '/textures/items')
                    if 'iron_pickaxe.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'iron_pickaxe.png'),
                                  os.path.join(b + '/textures/items', str('pickaxeIron.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/stone_pickaxe.png', b + '/textures/items')
                    if 'stone_pickaxe.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'stone_pickaxe.png'),
                                  os.path.join(b + '/textures/items', str('pickaxeStone.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/wood_pickaxe.png', b + '/textures/items')
                    if 'wood_pickaxe.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'wood_pickaxe.png'),
                                  os.path.join(b + '/textures/items', str('pickaxeWood.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/porkchop_cooked.png', b + '/textures/items')
                    if 'porkchop_cooked.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'porkchop_cooked.png'),
                                  os.path.join(b + '/textures/items', str('porkchopCooked.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/porkchop_raw.png', b + '/textures/items')
                    if 'porkchop_raw.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'porkchop_raw.png'),
                                  os.path.join(b + '/textures/items', str('porkchopraw.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/potato.png', b + '/textures/items')
                    if 'potato.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'potato.png'),
                                  os.path.join(b + '/textures/items', str('potato.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/potato_baked.png', b + '/textures/items')
                    if 'potato_baked.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'potato_baked.png'),
                                  os.path.join(b + '/textures/items', str('potatoBaked.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/potato_poisonous.png', b + '/textures/items')
                    if 'potato_poisonous.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'potato_poisonous.png'),
                                  os.path.join(b + '/textures/items', str('potatoPoisonous.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/potion_bottle_drinkable.png', b + '/textures/items')
                    if 'potion_bottle_drinkable.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'potion_bottle_drinkable.png'),
                                  os.path.join(b + '/textures/items', str('potion.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/potion_contents.png', b + '/textures/items')
                    if 'potion_contents.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'potion_contents.png'),
                                  os.path.join(b + '/textures/items', str('potion_contents.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/potion_bottle_splash.png', b + '/textures/items')
                    if 'potion_bottle_splash.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'potion_bottle_splash.png'),
                                  os.path.join(b + '/textures/items', str('potion_splash.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/record_11.png', b + '/textures/items')
                    if 'record_11.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'record_11.png'),
                                  os.path.join(b + '/textures/items', str('record_11.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/record_13.png', b + '/textures/items')
                    if 'record_13.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'record_13.png'),
                                  os.path.join(b + '/textures/items', str('record_13.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/record_blocks.png', b + '/textures/items')
                    if 'record_blocks.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'record_blocks.png'),
                                  os.path.join(b + '/textures/items', str('record_blocks.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/record_cat.png', b + '/textures/items')
                    if 'record_cat.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'record_cat.png'),
                                  os.path.join(b + '/textures/items', str('record_cat.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/record_chirp.png', b + '/textures/items')
                    if 'record_chirp.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'record_chirp.png'),
                                  os.path.join(b + '/textures/items', str('record_chirp.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/record_far.png', b + '/textures/items')
                    if 'record_far.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'record_far.png'),
                                  os.path.join(b + '/textures/items', str('record_far.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/record_mall.png', b + '/textures/items')
                    if 'record_mall.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'record_mall.png'),
                                  os.path.join(b + '/textures/items', str('record_mall.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/record_mellohi.png', b + '/textures/items')
                    if 'record_mellohi.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'record_mellohi.png'),
                                  os.path.join(b + '/textures/items', str('record_mellohi.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/record_stal.png', b + '/textures/items')
                    if 'record_stal.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'record_stal.png'),
                                  os.path.join(b + '/textures/items', str('record_stal.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/record_strad.png', b + '/textures/items')
                    if 'record_strad.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'record_strad.png'),
                                  os.path.join(b + '/textures/items', str('record_strad.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/record_wait.png', b + '/textures/items')
                    if 'record_wait.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'record_wait.png'),
                                  os.path.join(b + '/textures/items', str('record_wait.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/record_ward.png', b + '/textures/items')
                    if 'record_ward.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'record_ward.png'),
                                  os.path.join(b + '/textures/items', str('record_ward.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/redstone_dust.png', b + '/textures/items')
                    if 'redstone_dust.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'redstone_dust.png'),
                                  os.path.join(b + '/textures/items', str('redstone.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/reeds.png', b + '/textures/items')
                    if 'reeds.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'reeds.png'),
                                  os.path.join(b + '/textures/items', str('reeds.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/rotten_flesh.png', b + '/textures/items')
                    if 'rotten_flesh.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'rotten_flesh.png'),
                                  os.path.join(b + '/textures/items', str('rottenFlesh.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/saddle.png', b + '/textures/items')
                    if 'saddle.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'saddle.png'),
                                  os.path.join(b + '/textures/items', str('saddle.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/seeds_wheat.png', b + '/textures/items')
                    if 'seeds_wheat.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'seeds_wheat.png'),
                                  os.path.join(b + '/textures/items', str('seeds.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/seeds_melon.png', b + '/textures/items')
                    if 'seeds_melon.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'seeds_melon.png'),
                                  os.path.join(b + '/textures/items', str('seeds_melon.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/seeds_pumpkin.png', b + '/textures/items')
                    if 'seeds_pumpkin.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'seeds_pumpkin.png'),
                                  os.path.join(b + '/textures/items', str('seeds_pumpkin.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/shears.png', b + '/textures/items')
                    if 'shears.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'shears.png'),
                                  os.path.join(b + '/textures/items', str('shears.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/diamond_shovel.png', b + '/textures/items')
                    if 'diamond_shovel.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'diamond_shovel.png'),
                                  os.path.join(b + '/textures/items', str('shovelDiamond.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/gold_shovel.png', b + '/textures/items')
                    if 'gold_shovel.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'gold_shovel.png'),
                                  os.path.join(b + '/textures/items', str('shovelGold.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/iron_shovel.png', b + '/textures/items')
                    if 'iron_shovel.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'iron_shovel.png'),
                                  os.path.join(b + '/textures/items', str('shovelIron.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/stone_shovel.png', b + '/textures/items')
                    if 'stone_shovel.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'stone_shovel.png'),
                                  os.path.join(b + '/textures/items', str('shovelStone.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/wood_shovel.png', b + '/textures/items')
                    if 'wood_shovel.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'wood_shovel.png'),
                                  os.path.join(b + '/textures/items', str('shovelWood.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/sign.png', b + '/textures/items')
                    if 'sign.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'sign.png'),
                                  os.path.join(b + '/textures/items', str('sign.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/slimeball.png', b + '/textures/items')
                    if 'slimeball.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'slimeball.png'),
                                  os.path.join(b + '/textures/items', str('slimeball.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/empty_armor_slot_boots.png', b + '/textures/items')
                    if 'empty_armor_slot_boots.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'empty_armor_slot_boots.png'),
                                  os.path.join(b + '/textures/items', str('slot_empty_boots.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/empty_armor_slot_chestplate.png', b + '/textures/items')
                    if 'empty_armor_slot_chestplate.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'empty_armor_slot_chestplate.png'),
                                  os.path.join(b + '/textures/items', str('slot_empty_chestplate.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/empty_armor_slot_helmet.png', b + '/textures/items')
                    if 'empty_armor_slot_helmet.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'empty_armor_slot_helmet.png'),
                                  os.path.join(b + '/textures/items', str('slot_empty_helmet.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/empty_armor_slot_leggings.png', b + '/textures/items')
                    if 'empty_armor_slot_leggings.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'empty_armor_slot_leggings.png'),
                                  os.path.join(b + '/textures/items', str('slot_empty_leggings.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/snowball.png', b + '/textures/items')
                    if 'snowball.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'snowball.png'),
                                  os.path.join(b + '/textures/items', str('snowball.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/melon_speckled.png', b + '/textures/items')
                    if 'melon_speckled.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'melon_speckled.png'),
                                  os.path.join(b + '/textures/items', str('speckledMelon.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/spider_eye.png', b + '/textures/items')
                    if 'spider_eye.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'spider_eye.png'),
                                  os.path.join(b + '/textures/items', str('spiderEYE.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/stick.png', b + '/textures/items')
                    if 'stick.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'stick.png'),
                                  os.path.join(b + '/textures/items', str('stick.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/string.png', b + '/textures/items')
                    if 'string.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'string.png'),
                                  os.path.join(b + '/textures/items', str('string.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/sugar.png', b + '/textures/items')
                    if 'sugar.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'sugar.png'),
                                  os.path.join(b + '/textures/items', str('sugar.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/gunpowder.png', b + '/textures/items')
                    if 'gunpowder.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'gunpowder.png'),
                                  os.path.join(b + '/textures/items', str('sulphur.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/diamond_sword.png', b + '/textures/items')
                    if 'diamond_sword.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'diamond_sword.png'),
                                  os.path.join(b + '/textures/items', str('swordDiamond.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/gold_sword.png', b + '/textures/items')
                    if 'gold_sword.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'gold_sword.png'),
                                  os.path.join(b + '/textures/items', str('swordGold.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/iron_sword.png', b + '/textures/items')
                    if 'iron_sword.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'iron_sword.png'),
                                  os.path.join(b + '/textures/items', str('swordIron.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/stone_sword.png', b + '/textures/items')
                    if 'stone_sword.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'stone_sword.png'),
                                  os.path.join(b + '/textures/items', str('swordStone.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/wood_sword.png', b + '/textures/items')
                    if 'wood_sword.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'wood_sword.png'),
                                  os.path.join(b + '/textures/items', str('swordWood.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/wheat.png', b + '/textures/items')
                    if 'wheat.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'wheat.png'),
                                  os.path.join(b + '/textures/items', str('wheat.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/book_writable.png', b + '/textures/items')
                    if 'book_writable.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'book_writable.png'),
                                  os.path.join(b + '/textures/items', str('writingBook.png')))
                except:
                    pass

                try:
                    file_path = a + '/assets/minecraft/textures/items'
                    file_names = os.listdir(file_path)
                    shutil.copy(file_path + '/book_written.png', b + '/textures/items')
                    if 'book_written.png' in file_names:
                        os.rename(os.path.join(b + '/textures/items', 'book_written.png'),
                                  os.path.join(b + '/textures/items', str('writtenBook.png')))
                except:
                    pass
                messagebox.showinfo("Successful", "자유지정에 폴더 생성완료")
            else:
                root.quit()
        else:
            if my_pw == getCurrentStrDate():
                my_pw = pwent.get()
                if my_pw == getCurrentStrDate():
                    os.chdir('C:/Users/wydyx/AppData/Roaming/.minecraft/texturepacks')
                    os.mkdir(name.get())

                    b ='C:/Users/wydyx/AppData/Roaming/.minecraft/texturepacks/' + name.get()
                    os.chdir(b)
                    os.mkdir('achievement')
                    os.mkdir('armor')
                    os.mkdir('art')
                    os.mkdir('environment')
                    os.mkdir('gui')
                    os.mkdir('item')
                    os.mkdir('misc')
                    os.mkdir('mob')
                    os.mkdir('terrain')
                    os.mkdir('textures')
                    os.mkdir('title')

                    os.chdir(b + '/textures')
                    os.mkdir('blocks')
                    os.mkdir('items')

                    os.chdir(b + '/gui')
                    os.mkdir('creative_inv')

                    os.chdir(b + '/mob')
                    os.mkdir('enderdragon')
                    os.mkdir('villager')

                    os.chdir(b)

                    f = open(b + '/pack.txt', "w")
                    f.write('§41.8.9 §f-> §41.5.2§f로 변경된 텍스쳐팩')
                    f.write('\n')
                    f.write('§6모든문의 §f: 김준희#5870')
                    f.close()

                    # part of 상위표기(하위표기)

                    # part of TexturePack(Pack)
                    try:
                        file_path = a
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/pack.png', b)
                        if 'pack.png' in file_names:
                            os.rename(os.path.join(b, 'pack.png'), os.path.join(b, str('pack.png')))
                    except:
                        pass

                        # part of gui_achieve(achievement)
                    try:
                        file_path = a + '/assets/minecraft/textures/gui/achievement'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/achievement_background.png', b + '/achievement')
                        if 'achievement_background.png' in file_names:
                            os.rename(os.path.join(b + '/achievement', 'achievement_background.png'),
                                      os.path.join(b + '/achievement', str('bg.png')))
                    except:
                        pass

                        # Part of Gui_container(GUI)
                    try:
                        file_path = a + '/assets/minecraft/textures/gui/container'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/anvil.png', b + '/gui')
                        if 'anvil.png' in file_names:
                            os.rename(os.path.join(b + '/gui', 'anvil.png'),
                                      os.path.join(b + '/gui', str('repair.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/gui/container'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/brewing_stand.png', b + '/gui')
                        if 'brewing_stand.png' in file_names:
                            os.rename(os.path.join(b + '/gui', 'brewing_stand.png'),
                                      os.path.join(b + '/gui', str('alchemy.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/gui/container'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/crafting_table.png', b + '/gui')
                        if 'crafting_table.png' in file_names:
                            os.rename(os.path.join(b + '/gui', 'crafting_table.png'),
                                      os.path.join(b + '/gui', str('crafting.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/gui/container'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/dispenser.png', b + '/gui')
                        if 'dispenser.png' in file_names:
                            os.rename(os.path.join(b + '/gui', 'dispenser.png'),
                                      os.path.join(b + '/gui', str('trap.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/gui/container'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/enchanting_table.png', b + '/gui')
                        if 'enchanting_table.png' in file_names:
                            os.rename(os.path.join(b + '/gui', 'enchanting_table.png'),
                                      os.path.join(b + '/gui', str('enchant.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/gui/container'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/stats_icons.png', b + '/gui')
                        if 'stats_icons.png' in file_names:
                            os.rename(os.path.join(b + '/gui', 'stats_icons.png'),
                                      os.path.join(b + '/gui', str('icons.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/gui/container'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/villager.png', b + '/gui')
                        if 'villager.png' in file_names:
                            os.rename(os.path.join(b + '/gui', 'villager.png'),
                                      os.path.join(b + '/gui', str('trading.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/gui/container'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/beacon.png', b + '/gui')
                        if 'beacon.png' in file_names:
                            os.rename(os.path.join(b + '/gui', 'beacon.png'),
                                      os.path.join(b + '/gui', str('beacon.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/gui/container'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/furnace.png', b + '/gui')
                        if 'furnace.png' in file_names:
                            os.rename(os.path.join(b + '/gui', 'furnace.png'),
                                      os.path.join(b + '/gui', str('furnace.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/gui/container'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/hopper.png', b + '/gui')
                        if 'hopper.png' in file_names:
                            os.rename(os.path.join(b + '/gui', 'hopper.png'),
                                      os.path.join(b + '/gui', str('hopper.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/gui/container'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/inventory.png', b + '/gui')
                        if 'inventory.png' in file_names:
                            os.rename(os.path.join(b + '/gui', 'inventory.png'),
                                      os.path.join(b + '/gui', str('inventory.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/gui/container'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/generic_54.png', b + '/gui')
                        if 'generic_54.png' in file_names:
                            os.rename(os.path.join(b + '/gui', 'generic_54.png'),
                                      os.path.join(b + '/gui', str('container.png')))
                    except:
                        pass

                        # part of creative_inventory(gui_gminv)
                    try:
                        file_path = a + '/assets/minecraft/textures/gui/container/creative_inventory'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/tab_inventory.png', b + '/gui/creative_inv')
                        if 'tab_inventory.png' in file_names:
                            os.rename(os.path.join(b + '/gui/creative_inv', 'tab_inventory.png'),
                                      os.path.join(b + '/gui/creative_inv', str('survival_inv.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/gui/container/creative_inventory'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/tab_item_search.png', b + '/gui/creative_inv')
                        if 'tab_item_search.png' in file_names:
                            os.rename(os.path.join(b + '/gui/creative_inv', 'tab_item_search.png'),
                                      os.path.join(b + '/gui/creative_inv', str('search.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/gui/container/creative_inventory'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/tab_items.png', b + '/gui/creative_inv')
                        if 'tab_items.png' in file_names:
                            os.rename(os.path.join(b + '/gui/creative_inv', 'tab_items.png'),
                                      os.path.join(b + '/gui/creative_inv', str('list_items.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/gui/container/creative_inventory'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/tabs.png', b + '/gui')
                        if 'tabs.png' in file_names:
                            os.rename(os.path.join(b + '/gui', 'tabs.png'),
                                      os.path.join(b + '/gui', str('allitems.png')))  # GUI위치로 변경
                    except:
                        pass

                    # part of GUI(GUI)
                    try:
                        file_path = a + '/assets/minecraft/textures/gui'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/book.png', b + '/gui')
                        if 'book.png' in file_names:
                            os.rename(os.path.join(b + '/gui', 'book.png'), os.path.join(b + '/gui', str('book.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/gui'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/demo_background.png', b + '/gui')
                        if 'demo_background.png' in file_names:
                            os.rename(os.path.join(b + '/gui', 'demo_background.png'),
                                      os.path.join(b + '/gui', str('demo_bg.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/gui'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/options_background.png', b + '/gui')
                        if 'options_background.png' in file_names:
                            os.rename(os.path.join(b + '/gui', 'options_background.png'),
                                      os.path.join(b + '/gui', str('background.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/gui'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/widgets.png', b + '/gui')
                        if 'widgets.png' in file_names:
                            os.rename(os.path.join(b + '/gui', 'widgets.png'), os.path.join(b + '/gui', str('gui.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/gui'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/icons.png', b + '/gui')
                        if 'icons.png' in file_names:
                            os.rename(os.path.join(b + '/gui', 'icons.png'), os.path.join(b + '/gui', str('icons.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/gui'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/saturationicons.png', b + '/gui')
                        if 'saturationicons.png' in file_names:
                            os.rename(os.path.join(b + '/gui', 'saturationicons.png'),
                                      os.path.join(b + '/gui', str('icons1.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/gui'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/resource_packs.png', b + '/gui')
                        if 'resource_packs.png' in file_names:
                            os.rename(os.path.join(b + '/gui', 'resource_packs.png'),
                                      os.path.join(b + '/gui', str('slot.png')))
                    except:
                        pass

                        # part of Entity(item)
                    try:
                        file_path = a + '/assets/minecraft/textures/entity'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/arrow.png', b + '/item')
                        if 'arrow.png' in file_names:
                            os.rename(os.path.join(b + '/item', 'arrow.png'),
                                      os.path.join(b + '/item', str('arrows.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/entity'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/enchanting_table_book.png', b + '/item')
                        if 'enchanting_table_book.png' in file_names:
                            os.rename(os.path.join(b + '/item', 'enchanting_table_book.png'),
                                      os.path.join(b + '/item', str('book.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/entity'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/minecart.png', b + '/item')
                        if 'minecart.png' in file_names:
                            os.rename(os.path.join(b + '/item', 'minecart.png'),
                                      os.path.join(b + '/item', str('cart.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/entity'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/experience_orb.png', b + '/item')
                        if 'experience_orb.png' in file_names:
                            os.rename(os.path.join(b + '/item', 'experience_orb.png'),
                                      os.path.join(b + '/item', str('xporb.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/entity'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/boat.png', b + '/item')
                        if 'boat.png' in file_names:
                            os.rename(os.path.join(b + '/item', 'boat.png'), os.path.join(b + '/item', str('boat.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/entity'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/sign.png', b + '/item')
                        if 'sign.png' in file_names:
                            os.rename(os.path.join(b + '/item', 'sign.png'), os.path.join(b + '/item', str('sign.png')))
                    except:
                        pass

                        # part of Entity_chest(item)
                    try:
                        file_path = a + '/assets/minecraft/textures/entity/chest'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/trapped_double.png', b + '/item')
                        if 'trapped_double.png' in file_names:
                            os.rename(os.path.join(b + '/item', 'trapped_double.png'),
                                      os.path.join(b + '/item', str('trap_large.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/entity/chest'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/trapped.png', b + '/item')
                        if 'trapped.png' in file_names:
                            os.rename(os.path.join(b + '/item', 'trapped.png'),
                                      os.path.join(b + '/item', str('trap_small.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/entity/chest'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/normal.png', b + '/item')
                        if 'normal.png' in file_names:
                            os.rename(os.path.join(b + '/item', 'normal.png'),
                                      os.path.join(b + '/item', str('chest.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/entity/chest'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/ender.png', b + '/item')
                        if 'ender.png' in file_names:
                            os.rename(os.path.join(b + '/item', 'ender.png'),
                                      os.path.join(b + '/item', str('enderchest.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/entity/chest'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/normal_double.png', b + '/item')
                        if 'normal_double.png' in file_names:
                            os.rename(os.path.join(b + '/item', 'normal_double.png'),
                                      os.path.join(b + '/item', str('largechest.png')))
                    except:
                        pass

                        # part of Entity_chest(mob)

                    try:
                        file_path = a + '/assets/minecraft/textures/entity'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/steve.png', b + '/mob')
                        if 'steve.png' in file_names:
                            os.rename(os.path.join(b + '/mob', 'steve.png'), os.path.join(b + '/mob', str('char.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/entity'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/chicken.png', b + '/mob')
                        if 'chicken.png' in file_names:
                            os.rename(os.path.join(b + '/mob', 'chicken.png'),
                                      os.path.join(b + '/mob', str('chicken.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/entity'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/blaze.png', b + '/mob')
                        if 'blaze.png' in file_names:
                            os.rename(os.path.join(b + '/mob', 'blaze.png'), os.path.join(b + '/mob', str('fire.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/entity'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/zombie_pigman.png', b + '/mob')
                        if 'zombie_pigman.png' in file_names:
                            os.rename(os.path.join(b + '/mob', 'zombie_pigman.png'),
                                      os.path.join(b + '/mob', str('pigzombie.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/entity'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/snowman.png', b + '/mob')
                        if 'snowman.png' in file_names:
                            os.rename(os.path.join(b + '/mob', 'snowman.png'),
                                      os.path.join(b + '/mob', str('snowman.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/entity'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/spider_eyes.png', b + '/mob')
                        if 'spider_eyes.png' in file_names:
                            os.rename(os.path.join(b + '/mob', 'spider_eyes.png'),
                                      os.path.join(b + '/mob', str('spider_eyes.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/entity'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/squid.png', b + '/mob')
                        if 'squid.png' in file_names:
                            os.rename(os.path.join(b + '/mob', 'squid.png'), os.path.join(b + '/mob', str('squid.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/entity'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/iron_golem.png', b + '/mob')
                        if 'iron_golem.png' in file_names:
                            os.rename(os.path.join(b + '/mob', 'iron_golem.png'),
                                      os.path.join(b + '/mob', str('villager_golem.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/entity'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/witch.png', b + '/mob')
                        if 'witch.png' in file_names:
                            os.rename(os.path.join(b + '/mob', 'witch.png'), os.path.join(b + '/mob', str('witch.png')))
                    except:
                        pass

                        # part of Entity_Cow(mob)

                    try:
                        file_path = a + '/assets/minecraft/textures/entity/cow'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/cow.png', b + '/mob')
                        if 'cow.png' in file_names:
                            os.rename(os.path.join(b + '/mob', 'cow.png'), os.path.join(b + '/mob', str('cow.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/entity/cow'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/mooshroom.png', b + '/mob')
                        if 'mooshroom.png' in file_names:
                            os.rename(os.path.join(b + '/mob', 'mooshroom.png'),
                                      os.path.join(b + '/mob', str('redcow.png')))
                    except:
                        pass

                        # part of Entity_Creeper(mob)

                    try:
                        file_path = a + '/assets/minecraft/textures/entity/creeper'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/creeper.png', b + '/mob')
                        if 'creeper.png' in file_names:
                            os.rename(os.path.join(b + '/mob', 'creeper.png'),
                                      os.path.join(b + '/mob', str('creeper.png')))
                    except:
                        pass

                        # part of Entity_endercrystal(mob/enderdragon)

                    try:
                        file_path = a + '/assets/minecraft/textures/entity/endercrystal'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/endercrystal.png', b + '/mob/enderdragon')
                        if 'endercrystal.png' in file_names:
                            os.rename(os.path.join(b + '/mob/enderdragon', 'endercrystal.png'),
                                      os.path.join(b + '/mob/enderdragon', str('crystal.png')))
                    except:
                        pass

                        # part of Entity_enderdragon(mob/enderdragon)

                    try:
                        file_path = a + '/assets/minecraft/textures/entity/enderdragon'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/dragon.png', b + '/mob/enderdragon')
                        if 'dragon.png' in file_names:
                            os.rename(os.path.join(b + '/mob/enderdragon', 'dragon.png'),
                                      os.path.join(b + '/mob/enderdragon', str('ender.png')))
                    except:
                        pass

                        # part of Entity_villager(mob/villager)

                    try:
                        file_path = a + '/assets/minecraft/textures/entity/villager'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/butcher.png', b + '/mob/villager')
                        if 'butcher.png' in file_names:
                            os.rename(os.path.join(b + '/mob/villager', 'butcher.png'),
                                      os.path.join(b + '/mob/villager', str('butcher.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/entity/villager'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/farmer.png', b + '/mob/villager')
                        if 'farmer.png' in file_names:
                            os.rename(os.path.join(b + '/mob/villager', 'farmer.png'),
                                      os.path.join(b + '/mob/villager', str('farmer.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/entity/villager'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/librarian.png', b + '/mob/villager')
                        if 'librarian.png' in file_names:
                            os.rename(os.path.join(b + '/mob/villager', 'librarian.png'),
                                      os.path.join(b + '/mob/villager', str('librarian.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/entity/villager'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/priest.png', b + '/mob/villager')
                        if 'priest.png' in file_names:
                            os.rename(os.path.join(b + '/mob/villager', 'priest.png'),
                                      os.path.join(b + '/mob/villager', str('priest.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/entity/villager'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/smith.png', b + '/mob/villager')
                        if 'smith.png' in file_names:
                            os.rename(os.path.join(b + '/mob/villager', 'smith.png'),
                                      os.path.join(b + '/mob/villager', str('smith.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/entity/villager'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/villager.png', b + '/mob/villager')
                        if 'villager.png' in file_names:
                            os.rename(os.path.join(b + '/mob/villager', 'villager.png'),
                                      os.path.join(b + '/mob/villager', str('villager.png')))
                    except:
                        pass

                        # part of Entity_enderman(mob)

                    try:
                        file_path = a + '/assets/minecraft/textures/entity/enderman'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/enderman.png', b + '/mob')
                        if 'enderman.png' in file_names:
                            os.rename(os.path.join(b + '/mob', 'enderman.png'),
                                      os.path.join(b + '/mob', str('enderman.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/entity/enderman'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/enderman_eyes.png', b + '/mob')
                        if 'enderman_eyes.png' in file_names:
                            os.rename(os.path.join(b + '/mob', 'enderman_eyes.png'),
                                      os.path.join(b + '/mob', str('enderman_eyes.png')))
                    except:
                        pass

                        # part of Entity_ghast(mob)

                    try:
                        file_path = a + '/assets/minecraft/textures/entity/ghast'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/ghast.png', b + '/mob')
                        if 'ghast.png' in file_names:
                            os.rename(os.path.join(b + '/mob', 'ghast.png'), os.path.join(b + '/mob', str('ghast.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/entity/ghast'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/ghast_shooting.png', b + '/mob')
                        if 'ghast_shooting.png' in file_names:
                            os.rename(os.path.join(b + '/mob', 'ghast_shooting.png'),
                                      os.path.join(b + '/mob', str('ghast_fire.png')))
                    except:
                        pass

                        # part of Entity_pig(mob)

                    try:
                        file_path = a + '/assets/minecraft/textures/entity/pig'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/pig.png', b + '/mob')
                        if 'pig.png' in file_names:
                            os.rename(os.path.join(b + '/mob', 'pig.png'), os.path.join(b + '/mob', str('pig.png')))
                    except:
                        pass

                        # part of Entity_sheep(mob)

                    try:
                        file_path = a + '/assets/minecraft/textures/entity/sheep'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/sheep.png', b + '/mob')
                        if 'sheep.png' in file_names:
                            os.rename(os.path.join(b + '/mob', 'sheep.png'), os.path.join(b + '/mob', str('sheep.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/entity/sheep'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/sheep_fur.png', b + '/mob')
                        if 'sheep_fur.png' in file_names:
                            os.rename(os.path.join(b + '/mob', 'sheep_fur.png'),
                                      os.path.join(b + '/mob', str('sheep_fur.png')))
                    except:
                        pass

                        # part of Entity_skeleton(mob)

                    try:
                        file_path = a + '/assets/minecraft/textures/entity/skeleton'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/skeleton.png', b + '/mob')
                        if 'skeleton.png' in file_names:
                            os.rename(os.path.join(b + '/mob', 'skeleton.png'),
                                      os.path.join(b + '/mob', str('skeleton.png')))
                    except:
                        pass

                        # part of Entity_slime(mob)

                    try:
                        file_path = a + '/assets/minecraft/textures/entity/slime'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/slime.png', b + '/mob')
                        if 'slime.png' in file_names:
                            os.rename(os.path.join(b + '/mob', 'slime.png'), os.path.join(b + '/mob', str('slime.png')))
                    except:
                        pass

                        # part of Entity_spider(mob)

                    try:
                        file_path = a + '/assets/minecraft/textures/entity/spider'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/spider.png', b + '/mob')
                        if 'spider.png' in file_names:
                            os.rename(os.path.join(b + '/mob', 'spider.png'),
                                      os.path.join(b + '/mob', str('spider.png')))
                    except:
                        pass

                        # part of Entity_wolf(mob)

                    try:
                        file_path = a + '/assets/minecraft/textures/entity/wolf'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/wolf.png', b + '/mob')
                        if 'wolf.png' in file_names:
                            os.rename(os.path.join(b + '/mob', 'wolf.png'), os.path.join(b + '/mob', str('wolf.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/entity/wolf'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/wolf_angry.png', b + '/mob')
                        if 'wolf_angry.png' in file_names:
                            os.rename(os.path.join(b + '/mob', 'wolf_angry.png'),
                                      os.path.join(b + '/mob', str('wolf_angry.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/entity/wolf'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/wolf_tame.png', b + '/mob')
                        if 'wolf_tame.png' in file_names:
                            os.rename(os.path.join(b + '/mob', 'wolf_tame.png'),
                                      os.path.join(b + '/mob', str('wolf_tame.png')))
                    except:
                        pass

                        # part of Entity_zombie(mob)

                    try:
                        file_path = a + '/assets/minecraft/textures/entity/zombie'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/zombie.png', b + '/mob')
                        if 'zombie.png' in file_names:
                            os.rename(os.path.join(b + '/mob', 'zombie.png'),
                                      os.path.join(b + '/mob', str('zombie.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/entity/zombie'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/zombie_villager.png', b + '/mob')
                        if 'zombie_villager.png' in file_names:
                            os.rename(os.path.join(b + '/mob', 'zombie_villager.png'),
                                      os.path.join(b + '/mob', str('zombie_villager.png')))
                    except:
                        pass

                        # part of environment(environment)

                    try:
                        file_path = a + '/assets/minecraft/textures/environment'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/rain.png', b + '/environment')
                        if 'rain.png' in file_names:
                            os.rename(os.path.join(b + '/environment', 'rain.png'),
                                      os.path.join(b + '/environment', str('rain.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/mcpatcher/sky/world0'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/clouds.png', b + '/environment')
                        if 'clouds.png' in file_names:
                            os.rename(os.path.join(b + '/environment', 'clouds.png'),
                                      os.path.join(b + '/environment', str('clouds.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/mcpatcher/sky/world0'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/clouds2.png', b + '/environment')
                        if 'clouds2.png' in file_names:
                            os.rename(os.path.join(b + '/environment', 'clouds2.png'),
                                      os.path.join(b + '/environment', str('clouds2.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/mcpatcher/sky/world0'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/clouds1.png', b + '/environment')
                        if 'clouds1.png' in file_names:
                            os.rename(os.path.join(b + '/environment', 'clouds1.png'),
                                      os.path.join(b + '/environment', str('clouds1.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/mcpatcher/sky/world0'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/moon.png', b + '/environment')
                        if 'moon.png' in file_names:
                            os.rename(os.path.join(b + '/environment', 'moon.png'),
                                      os.path.join(b + '/environment', str('rain.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/mcpatcher/sky/world0'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/moon_phases.png', b + '/environment')
                        if 'moon_phases.png' in file_names:
                            os.rename(os.path.join(b + '/environment', 'moon_phases.png'),
                                      os.path.join(b + '/environment', str('moon_phases.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/mcpatcher/sky/world0'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/sun.png', b + '/environment')
                        if 'sun.png' in file_names:
                            os.rename(os.path.join(b + '/environment', 'sun.png'),
                                      os.path.join(b + '/environment', str('sun.png')))
                    except:
                        pass

                    # part of misc(misc)
                    try:
                        file_path = a + '/assets/minecraft/textures/misc'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/enchanted_item_glint.png', b + '/misc')
                        if 'enchanted_item_glint.png' in file_names:
                            os.rename(os.path.join(b, 'enchanted_item_glint.png'), os.path.join(b, str('glint.png')))
                    except:
                        pass

                        # part of particle(misc / texturePack)

                    try:
                        file_path = a + '/assets/minecraft/textures/particle'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/particles.png', b)
                        if 'particles.png' in file_names:
                            os.rename(os.path.join(b, 'particles.png'), os.path.join(b, str('particles.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/particle'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/particles2.png', b)
                        if 'particles2.png' in file_names:
                            os.rename(os.path.join(b, 'particles2.png'), os.path.join(b, str('particles2.png')))
                    except:
                        pass

                        # part of armor(armor)

                    try:
                        file_path = a + '/assets/minecraft/textures/models/armor'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/chainmail_layer_1.png', b + '/armor')
                        if 'chainmail_layer_1.png' in file_names:
                            os.rename(os.path.join(b + '/armor', 'chainmail_layer_1.png'),
                                      os.path.join(b + '/armor', str('chain_1.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/models/armor'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/chainmail_layer_2.png', b + '/armor')
                        if 'chainmail_layer_2.png' in file_names:
                            os.rename(os.path.join(b + '/armor', 'chainmail_layer_2.png'),
                                      os.path.join(b + '/armor', str('chain_2.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/models/armor'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/diamond_layer_1.png', b + '/armor')
                        if 'diamond_layer_1.png' in file_names:
                            os.rename(os.path.join(b + '/armor', 'diamond_layer_1.png'),
                                      os.path.join(b + '/armor', str('diamond_1.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/models/armor'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/diamond_layer_2.png', b + '/armor')
                        if 'diamond_layer_2.png' in file_names:
                            os.rename(os.path.join(b + '/armor', 'diamond_layer_2.png'),
                                      os.path.join(b + '/armor', str('diamond_2.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/models/armor'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/gold_layer_1.png', b + '/armor')
                        if 'gold_layer_1.png' in file_names:
                            os.rename(os.path.join(b + '/armor', 'gold_layer_1.png'),
                                      os.path.join(b + '/armor', str('gold_1.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/models/armor'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/gold_layer_2.png', b + '/armor')
                        if 'gold_layer_2.png' in file_names:
                            os.rename(os.path.join(b + '/armor', 'gold_layer_2.png'),
                                      os.path.join(b + '/armor', str('gold_2.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/models/armor'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/iron_layer_1.png', b + '/armor')
                        if 'iron_layer_1.png' in file_names:
                            os.rename(os.path.join(b + '/armor', 'iron_layer_1.png'),
                                      os.path.join(b + '/armor', str('iron_1.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/models/armor'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/iron_layer_2.png', b + '/armor')
                        if 'iron_layer_2.png' in file_names:
                            os.rename(os.path.join(b + '/armor', 'iron_layer_2.png'),
                                      os.path.join(b + '/armor', str('iron_2.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/models/armor'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/leather_layer_1.png', b + '/armor')
                        if 'leather_layer_1.png' in file_names:
                            os.rename(os.path.join(b + '/armor', 'leather_layer_1.png'),
                                      os.path.join(b + '/armor', str('cloth_1.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/models/armor'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/leather_layer_1_overlay.png', b + '/armor')
                        if 'leather_layer_1_overlay.png' in file_names:
                            os.rename(os.path.join(b + '/armor', 'leather_layer_1_overlay.png'),
                                      os.path.join(b + '/armor', str('cloth_1_b.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/models/armor'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/leather_layer_2.png', b + '/armor')
                        if 'leather_layer_2.png' in file_names:
                            os.rename(os.path.join(b + '/armor', 'leather_layer_2.png'),
                                      os.path.join(b + '/armor', str('cloth_2.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/models/armor'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/leather_layer_2_overlay.png', b + '/armor')
                        if 'leather_layer_2_overlay.png' in file_names:
                            os.rename(os.path.join(b + '/armor', 'leather_layer_2_overlay.png'),
                                      os.path.join(b + '/armor', str('cloth_2_b.png')))
                    except:
                        pass

                    # part of blocks(blocks)
                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/rail_activator_powered.png', b + '/textures/blocks')
                        if 'rail_activator_powered.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'rail_activator_powered.png'),
                                      os.path.join(b + '/textures/blocks', str('activatorRail_powered.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/rail_activator.png', b + '/textures/blocks')
                        if 'rail_activator.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'rail_activator.png'),
                                      os.path.join(b + '/textures/blocks', str('activatorRail.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/anvil_base.png', b + '/textures/blocks')
                        if 'anvil_base.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'anvil_base.png'),
                                      os.path.join(b + '/textures/blocks', str('anvil_base.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/anvil_top_damaged_0.png', b + '/textures/blocks')
                        if 'anvil_top_damaged_0.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'anvil_top_damaged_0.png'),
                                      os.path.join(b + '/textures/blocks', str('anvil_top.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/anvil_top_damaged_1.png', b + '/textures/blocks')
                        if 'anvil_top_damaged_1.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'anvil_top_damaged_1.png'),
                                      os.path.join(b + '/textures/blocks', str('anvil_top_damaged_1.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/anvil_top_damaged_2.png', b + '/textures/blocks')
                        if 'anvil_top_damaged_2.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'anvil_top_damaged_2.png'),
                                      os.path.join(b + '/textures/blocks', str('anvil_top_damaged_2.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/beacon.png', b + '/textures/blocks')
                        if 'beacon.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'beacon.png'),
                                      os.path.join(b + '/textures/blocks', str('beacon.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/bed_feet_end.png', b + '/textures/blocks')
                        if 'bed_feet_end.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'bed_feet_end.png'),
                                      os.path.join(b + '/textures/blocks', str('bed_feet_end.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/bed_feet_side.png', b + '/textures/blocks')
                        if 'bed_feet_side.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'bed_feet_side.png'),
                                      os.path.join(b + '/textures/blocks', str('bed_feet_side.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/bed_feet_top.png', b + '/textures/blocks')
                        if 'bed_feet_top.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'bed_feet_top.png'),
                                      os.path.join(b + '/textures/blocks', str('bed_feet_top.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/bed_head_end.png', b + '/textures/blocks')
                        if 'bed_head_end.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'bed_head_end.png'),
                                      os.path.join(b + '/textures/blocks', str('bed_head_end.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/bed_head_side.png', b + '/textures/blocks')
                        if 'bed_head_side.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'bed_head_side.png'),
                                      os.path.join(b + '/textures/blocks', str('bed_head_side.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/bed_head_top.png', b + '/textures/blocks')
                        if 'bed_head_top.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'bed_head_top.png'),
                                      os.path.join(b + '/textures/blocks', str('bed_head_top.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/bedrock.png', b + '/textures/blocks')
                        if 'bedrock.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'bedrock.png'),
                                      os.path.join(b + '/textures/blocks', str('bedrock.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/diamond_block.png', b + '/textures/blocks')
                        if 'diamond_block.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'diamond_block.png'),
                                      os.path.join(b + '/textures/blocks', str('blockDiamond.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/emerald_block.png', b + '/textures/blocks')
                        if 'emerald_block.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'Emerald_block.png'),
                                      os.path.join(b + '/textures/blocks', str('blockEmerald.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/Gold_block.png', b + '/textures/blocks')
                        if 'Gold_block.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'Gold_block.png'),
                                      os.path.join(b + '/textures/blocks', str('blockGold.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/Iron_block.png', b + '/textures/blocks')
                        if 'Iron_block.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'Iron_block.png'),
                                      os.path.join(b + '/textures/blocks', str('blockIron.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/lapis_block.png', b + '/textures/blocks')
                        if 'lapis_block.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'lapis_block.png'),
                                      os.path.join(b + '/textures/blocks', str('blockLapis.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/redstone_block.png', b + '/textures/blocks')
                        if 'redstone_block.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'redstone_block.png'),
                                      os.path.join(b + '/textures/blocks', str('blockRedstone.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/bookshelf.png', b + '/textures/blocks')
                        if 'bookshelf.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'bookshelf.png'),
                                      os.path.join(b + '/textures/blocks', str('bookshelf.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/brick.png', b + '/textures/blocks')
                        if 'brick.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'brick.png'),
                                      os.path.join(b + '/textures/blocks', str('brick.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/cactus_bottom.png', b + '/textures/blocks')
                        if 'cactus_bottom.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'cactus_bottom.png'),
                                      os.path.join(b + '/textures/blocks', str('cactus_bottom.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/cactus_side.png', b + '/textures/blocks')
                        if 'cactus_side.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'cactus_side.png'),
                                      os.path.join(b + '/textures/blocks', str('cactus_side.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/cactus_top.png', b + '/textures/blocks')
                        if 'cactus_top.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'cactus_top.png'),
                                      os.path.join(b + '/textures/blocks', str('cactus_top.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/cake_bottom.png', b + '/textures/blocks')
                        if 'cake_bottom.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'cake_bottom.png'),
                                      os.path.join(b + '/textures/blocks', str('cake_bottom.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/cake_inner.png', b + '/textures/blocks')
                        if 'cake_inner.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'cake_inner.png'),
                                      os.path.join(b + '/textures/blocks', str('cake_inner.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/cake_side.png', b + '/textures/blocks')
                        if 'cake_side.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'cake_side.png'),
                                      os.path.join(b + '/textures/blocks', str('cake_side.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/cake_top.png', b + '/textures/blocks')
                        if 'cake_top.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'cake_top.png'),
                                      os.path.join(b + '/textures/blocks', str('cake_top.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/cauldron_bottom.png', b + '/textures/blocks')
                        if 'cauldron_bottom.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'cauldron_bottom.png'),
                                      os.path.join(b + '/textures/blocks', str('cauldron_bottom.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/cauldron_inner.png', b + '/textures/blocks')
                        if 'cauldron_inner.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'cauldron_inner.png'),
                                      os.path.join(b + '/textures/blocks', str('cauldron_inner.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/cauldron_side.png', b + '/textures/blocks')
                        if 'cauldron_side.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'cauldron_side.png'),
                                      os.path.join(b + '/textures/blocks', str('cauldron_side.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/cauldron_top.png', b + '/textures/blocks')
                        if 'cauldron_top.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'cauldron_top.png'),
                                      os.path.join(b + '/textures/blocks', str('cauldron_top.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/clay.png', b + '/textures/blocks')
                        if 'clay.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'clay.png'),
                                      os.path.join(b + '/textures/blocks', str('clay.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/brewing_stand.png', b + '/textures/blocks')
                        if 'brewing_stand.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'brewing_stand.png'),
                                      os.path.join(b + '/textures/blocks', str('brewingStand.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/deadbush.png', b + '/textures/blocks')
                        if 'deadbush.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'deadbush.png'),
                                      os.path.join(b + '/textures/blocks', str('deadbush.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/pumpkin_stem_disconnected.png', b + '/textures/blocks')
                        if 'pumpkin_stem_disconnected.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'pumpkin_stem_disconnected.png'),
                                      os.path.join(b + '/textures/blocks', str('stem_straight.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/pumpkin_stem_connected.png', b + '/textures/blocks')
                        if 'pumpkin_stem_connected.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'pumpkin_stem_connected.png'),
                                      os.path.join(b + '/textures/blocks', str('stem_bent.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/brewing_stand_base.png', b + '/textures/blocks')
                        if 'brewing_stand_base.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'brewing_stand_base.png'),
                                      os.path.join(b + '/textures/blocks', str('brewingstand_base.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/carrots_stage_0.png', b + '/textures/blocks')
                        if 'carrots_stage_0.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'carrots_stage_0.png'),
                                      os.path.join(b + '/textures/blocks', str('carrots_0.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/carrots_stage_1.png', b + '/textures/blocks')
                        if 'carrots_stage_1.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'carrots_stage_1.png'),
                                      os.path.join(b + '/textures/blocks', str('carrots_1.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/carrots_stage_2.png', b + '/textures/blocks')
                        if 'carrots_stage_2.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'carrots_stage_2.png'),
                                      os.path.join(b + '/textures/blocks', str('carrots_2.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/carrots_stage_3.png', b + '/textures/blocks')
                        if 'carrots_stage_3.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'carrots_stage_3.png'),
                                      os.path.join(b + '/textures/blocks', str('carrots_3.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/wool_colored_white.png', b + '/textures/blocks')
                        if 'wool_colored_white.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'wool_colored_white.png'),
                                      os.path.join(b + '/textures/blocks', str('cloth_0.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/wool_colored_orange.png', b + '/textures/blocks')
                        if 'wool_colored_orange.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'wool_colored_orange.png'),
                                      os.path.join(b + '/textures/blocks', str('cloth_1.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/wool_colored_magenta.png', b + '/textures/blocks')
                        if 'wool_colored_magenta.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'wool_colored_magenta.png'),
                                      os.path.join(b + '/textures/blocks', str('cloth_2.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/wool_colored_light_blue.png', b + '/textures/blocks')
                        if 'wool_colored_light_blue.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'wool_colored_light_blue.png'),
                                      os.path.join(b + '/textures/blocks', str('cloth_3.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/wool_colored_yellow.png', b + '/textures/blocks')
                        if 'wool_colored_yellow.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'wool_colored_yellow.png'),
                                      os.path.join(b + '/textures/blocks', str('cloth_4.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/wool_colored_lime.png', b + '/textures/blocks')
                        if 'wool_colored_lime.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'wool_colored_lime.png'),
                                      os.path.join(b + '/textures/blocks', str('cloth_5.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/wool_colored_pink.png', b + '/textures/blocks')
                        if 'wool_colored_pink.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'wool_colored_pink.png'),
                                      os.path.join(b + '/textures/blocks', str('cloth_6.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/wool_colored_gray.png', b + '/textures/blocks')
                        if 'wool_colored_gray.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'wool_colored_gray.png'),
                                      os.path.join(b + '/textures/blocks', str('cloth_7.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/wool_colored_silver.png', b + '/textures/blocks')
                        if 'wool_colored_silver.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'wool_colored_silver.png'),
                                      os.path.join(b + '/textures/blocks', str('cloth_8.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/wool_colored_cyan.png', b + '/textures/blocks')
                        if 'wool_colored_cyan.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'wool_colored_cyan.png'),
                                      os.path.join(b + '/textures/blocks', str('cloth_9.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/wool_colored_purple.png', b + '/textures/blocks')
                        if 'wool_colored_purple.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'wool_colored_purple.png'),
                                      os.path.join(b + '/textures/blocks', str('cloth_10.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/wool_colored_blue.png', b + '/textures/blocks')
                        if 'wool_colored_blue.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'wool_colored_blue.png'),
                                      os.path.join(b + '/textures/blocks', str('cloth_11.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/wool_colored_brown.png', b + '/textures/blocks')
                        if 'wool_colored_brown.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'wool_colored_brown.png'),
                                      os.path.join(b + '/textures/blocks', str('cloth_12.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/wool_colored_green.png', b + '/textures/blocks')
                        if 'wool_colored_green.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'wool_colored_green.png'),
                                      os.path.join(b + '/textures/blocks', str('cloth_13.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/wool_colored_red.png', b + '/textures/blocks')
                        if 'wool_colored_red.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'wool_colored_red.png'),
                                      os.path.join(b + '/textures/blocks', str('cloth_14.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/wool_colored_black.png', b + '/textures/blocks')
                        if 'wool_colored_black.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'wool_colored_black.png'),
                                      os.path.join(b + '/textures/blocks', str('cloth_15.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/cocoa_stage_0.png', b + '/textures/blocks')
                        if 'cocoa_stage_0.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'cocoa_stage_0.png'),
                                      os.path.join(b + '/textures/blocks', str('cocoa_0.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/cocoa_stage_1.png', b + '/textures/blocks')
                        if 'cocoa_stage_1.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'cocoa_stage_1.png'),
                                      os.path.join(b + '/textures/blocks', str('cocoa_1.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/cocoa_stage_2.png', b + '/textures/blocks')
                        if 'cocoa_stage_2.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'cocoa_stage_2.png'),
                                      os.path.join(b + '/textures/blocks', str('cocoa_2.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/command_block.png', b + '/textures/blocks')
                        if 'command_block.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'command_block.png'),
                                      os.path.join(b + '/textures/blocks', str('commandblock.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/comparator_off.png', b + '/textures/blocks')
                        if 'comparator_off.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'comparator_off.png'),
                                      os.path.join(b + '/textures/blocks', str('comparator.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/comparator_on.png', b + '/textures/blocks')
                        if 'comparator_on.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'comparator_on.png'),
                                      os.path.join(b + '/textures/blocks', str('comparator_lit.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/wheat_stage_0.png', b + '/textures/blocks')
                        if 'wheat_stage_0.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'wheat_stage_0.png'),
                                      os.path.join(b + '/textures/blocks', str('crops_0.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/wheat_stage_1.png', b + '/textures/blocks')
                        if 'wheat_stage_1.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'wheat_stage_1.png'),
                                      os.path.join(b + '/textures/blocks', str('crops_1.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/wheat_stage_2.png', b + '/textures/blocks')
                        if 'wheat_stage_2.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'wheat_stage_2.png'),
                                      os.path.join(b + '/textures/blocks', str('crops_2.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/wheat_stage_3.png', b + '/textures/blocks')
                        if 'wheat_stage_3.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'wheat_stage_3.png'),
                                      os.path.join(b + '/textures/blocks', str('crops_3.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/wheat_stage_4.png', b + '/textures/blocks')
                        if 'wheat_stage_4.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'wheat_stage_4.png'),
                                      os.path.join(b + '/textures/blocks', str('crops_4.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/wheat_stage_5.png', b + '/textures/blocks')
                        if 'wheat_stage_5.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'wheat_stage_5.png'),
                                      os.path.join(b + '/textures/blocks', str('crops_5.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/wheat_stage_6.png', b + '/textures/blocks')
                        if 'wheat_stage_6.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'wheat_stage_6.png'),
                                      os.path.join(b + '/textures/blocks', str('crops_06.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/wheat_stage_7.png', b + '/textures/blocks')
                        if 'wheat_stage_7.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'wheat_stage_7.png'),
                                      os.path.join(b + '/textures/blocks', str('crops_7.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/daylight_detector_side.png', b + '/textures/blocks')
                        if 'daylight_detector_side.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'daylight_detector_side.png'),
                                      os.path.join(b + '/textures/blocks', str('daylightdetector_side.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/daylight_detector_top.png', b + '/textures/blocks')
                        if 'daylight_detector_top.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'daylight_detector_top.png'),
                                      os.path.join(b + '/textures/blocks', str('daylightdetector_top.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/destroy_stage_0.png', b + '/textures/blocks')
                        if 'destroy_stage_0.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'destroy_stage_0.png'),
                                      os.path.join(b + '/textures/blocks', str('destroy_0.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/destroy_stage_1.png', b + '/textures/blocks')
                        if 'destroy_stage_1.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'destroy_stage_1.png'),
                                      os.path.join(b + '/textures/blocks', str('destroy_1.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/destroy_stage_2.png', b + '/textures/blocks')
                        if 'destroy_stage_2.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'destroy_stage_2.png'),
                                      os.path.join(b + '/textures/blocks', str('destroy_2.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/destroy_stage_3.png', b + '/textures/blocks')
                        if 'destroy_stage_3.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'destroy_stage_3.png'),
                                      os.path.join(b + '/textures/blocks', str('destroy_3.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/destroy_stage_4.png', b + '/textures/blocks')
                        if 'destroy_stage_4.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'destroy_stage_4.png'),
                                      os.path.join(b + '/textures/blocks', str('destroy_4.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/destroy_stage_5.png', b + '/textures/blocks')
                        if 'destroy_stage_5.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'destroy_stage_5.png'),
                                      os.path.join(b + '/textures/blocks', str('destroy_5.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/destroy_stage_6.png', b + '/textures/blocks')
                        if 'destroy_stage_6.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'destroy_stage_6.png'),
                                      os.path.join(b + '/textures/blocks', str('destroy_6.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/destroy_stage_7.png', b + '/textures/blocks')
                        if 'destroy_stage_7.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'destroy_stage_7.png'),
                                      os.path.join(b + '/textures/blocks', str('destroy_7.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/destroy_stage_8.png', b + '/textures/blocks')
                        if 'destroy_stage_8.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'destroy_stage_8.png'),
                                      os.path.join(b + '/textures/blocks', str('destroy_8.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/destroy_stage_9.png', b + '/textures/blocks')
                        if 'destroy_stage_9.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'destroy_stage_9.png'),
                                      os.path.join(b + '/textures/blocks', str('destroy_9.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/rail_detector.png', b + '/textures/blocks')
                        if 'rail_detector.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'rail_detector.png'),
                                      os.path.join(b + '/textures/blocks', str('detectorRail.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/rail_detector_powered.png', b + '/textures/blocks')
                        if 'rail_detector_powered.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'rail_detector_powered.png'),
                                      os.path.join(b + '/textures/blocks', str('detectorRail_on.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/dirt.png', b + '/textures/blocks')
                        if 'dirt.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'dirt.png'),
                                      os.path.join(b + '/textures/blocks', str('dirt.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/dispenser_front_horizontal.png', b + '/textures/blocks')
                        if 'dispenser_front_horizontal.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'dispenser_front_horizontal.png'),
                                      os.path.join(b + '/textures/blocks', str('dispenser_front.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/dispenser_front_vertical.png', b + '/textures/blocks')
                        if 'dispenser_front_vertical.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'dispenser_front_vertical.png'),
                                      os.path.join(b + '/textures/blocks', str('dispenser_front_vertical.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/door_iron_lower.png', b + '/textures/blocks')
                        if 'door_iron_lower.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'door_iron_lower.png'),
                                      os.path.join(b + '/textures/blocks', str('doorIron_lower.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/door_iron_upper.png', b + '/textures/blocks')
                        if 'door_iron_upper.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'door_iron_upper.png'),
                                      os.path.join(b + '/textures/blocks', str('doorIron_upper.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/door_wood_lower.png', b + '/textures/blocks')
                        if 'door_wood_lower.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'door_wood_lower.png'),
                                      os.path.join(b + '/textures/blocks', str('doorWood_lower.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/door_wood_upper.png', b + '/textures/blocks')
                        if 'door_wood_upper.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'door_wood_upper.png'),
                                      os.path.join(b + '/textures/blocks', str('doorWood_upper.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/dragon_egg.png', b + '/textures/blocks')
                        if 'dragon_egg.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'dragon_egg.png'),
                                      os.path.join(b + '/textures/blocks', str('drangonEgg.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/dropper_front_horizontal.png', b + '/textures/blocks')
                        if 'dropper_front_horizontal.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'dropper_front_horizontal.png'),
                                      os.path.join(b + '/textures/blocks', str('dropper_front.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/dropper_front_vertical.png', b + '/textures/blocks')
                        if 'dropper_front_vertical.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'dropper_front_vertical.png'),
                                      os.path.join(b + '/textures/blocks', str('dropper_front_vertical.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/enchanting_table_bottom.png', b + '/textures/blocks')
                        if 'enchanting_table_bottom.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'enchanting_table_bottom.png'),
                                      os.path.join(b + '/textures/blocks', str('enchantment_bottom.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/enchanting_table_side.png', b + '/textures/blocks')
                        if 'enchanting_table_side.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'enchanting_table_side.png'),
                                      os.path.join(b + '/textures/blocks', str('enchantment_side.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/enchanting_table_top.png', b + '/textures/blocks')
                        if 'enchanting_table_top.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'enchanting_table_top.png'),
                                      os.path.join(b + '/textures/blocks', str('enchantment_top.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/endframe_eye.png', b + '/textures/blocks')
                        if 'endframe_eye.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'endframe_eye.png'),
                                      os.path.join(b + '/textures/blocks', str('endframe_eye.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/endframe_side.png', b + '/textures/blocks')
                        if 'endframe_side.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'endframe_side.png'),
                                      os.path.join(b + '/textures/blocks', str('endframe_side.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/endframe_top.png', b + '/textures/blocks')
                        if 'endframe_top.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'endframe_top.png'),
                                      os.path.join(b + '/textures/blocks', str('endframe_top.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/farmland_dry.png', b + '/textures/blocks')
                        if 'farmland_dry.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'farmland_dry.png'),
                                      os.path.join(b + '/textures/blocks', str('farmland_dry.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/farmland_wet.png', b + '/textures/blocks')
                        if 'farmland_wet.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'farmland_wet.png'),
                                      os.path.join(b + '/textures/blocks', str('farmland_wet.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/iron_bars.png', b + '/textures/blocks')
                        if 'iron_bars.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'iron_bars.png'),
                                      os.path.join(b + '/textures/blocks', str('fenceIron.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/fern.png', b + '/textures/blocks')
                        if 'fern.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'fern.png'),
                                      os.path.join(b + '/textures/blocks', str('fern.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/fire_layer_0.png', b + '/textures/blocks')
                        if 'fire_layer_0.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'fire_layer_0.png'),
                                      os.path.join(b + '/textures/blocks', str('fire_0.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/fire_layer_1.png', b + '/textures/blocks')
                        if 'fire_layer_1.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'fire_layer_1.png'),
                                      os.path.join(b + '/textures/blocks', str('fire_1.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/flower_dandelion.png', b + '/textures/blocks')
                        if 'flower_dandelion.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'flower_dandelion.png'),
                                      os.path.join(b + '/textures/blocks', str('flower.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/flower_pot.png', b + '/textures/blocks')
                        if 'flower_pot.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'flower_pot.png'),
                                      os.path.join(b + '/textures/blocks', str('flowerpot.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/furnace_front_off.png', b + '/textures/blocks')
                        if 'furnace_front_off.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'furnace_front_off.png'),
                                      os.path.join(b + '/textures/blocks', str('furnace_front.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/furnace_front_on.png', b + '/textures/blocks')
                        if 'furnace_front_on.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'furnace_front_on.png'),
                                      os.path.join(b + '/textures/blocks', str('furnace_front_lit.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/furnace_side.png', b + '/textures/blocks')
                        if 'furnace_side.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'furnace_side.png'),
                                      os.path.join(b + '/textures/blocks', str('furnace_side.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/furnace_top.png', b + '/textures/blocks')
                        if 'furnace_top.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'furnace_top.png'),
                                      os.path.join(b + '/textures/blocks', str('furnace_top.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/glass.png', b + '/textures/blocks')
                        if 'glass.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'glass.png'),
                                      os.path.join(b + '/textures/blocks', str('glass.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/rail_golden.png', b + '/textures/blocks')
                        if 'rail_golden.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'rail_golden.png'),
                                      os.path.join(b + '/textures/blocks', str('goldenRail.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/rail_golden_powered.png', b + '/textures/blocks')
                        if 'rail_golden_powered.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'rail_golden_powered.png'),
                                      os.path.join(b + '/textures/blocks', str('goldenRail_powered.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/grass_side.png', b + '/textures/blocks')
                        if 'grass_side.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'grass_side.png'),
                                      os.path.join(b + '/textures/blocks', str('grass_side.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/grass_side_overlay.png', b + '/textures/blocks')
                        if 'grass_side_overlay.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'grass_side_overlay.png'),
                                      os.path.join(b + '/textures/blocks', str('grass_side_overlay.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/grass_top.png', b + '/textures/blocks')
                        if 'grass_top.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'grass_top.png'),
                                      os.path.join(b + '/textures/blocks', str('grass_top.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/gravel.png', b + '/textures/blocks')
                        if 'gravel.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'gravel.png'),
                                      os.path.join(b + '/textures/blocks', str('gravel.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/netherrack.png', b + '/textures/blocks')
                        if 'netherrack.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'netherrack.png'),
                                      os.path.join(b + '/textures/blocks', str('hellrock.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/soul_sand.png', b + '/textures/blocks')
                        if 'soul_sand.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'soul_sand.png'),
                                      os.path.join(b + '/textures/blocks', str('hellsand.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/hopper_outside.png', b + '/textures/blocks')
                        if 'hopper_outside.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'hopper_outside.png'),
                                      os.path.join(b + '/textures/blocks', str('hopper.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/hopper_inside.png', b + '/textures/blocks')
                        if 'hopper_inside.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'hopper_inside.png'),
                                      os.path.join(b + '/textures/blocks', str('hopper_inside.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/hopper_top.png', b + '/textures/blocks')
                        if 'hopper_top.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'hopper_top.png'),
                                      os.path.join(b + '/textures/blocks', str('hopper_top.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/ice.png', b + '/textures/blocks')
                        if 'ice.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'ice.png'),
                                      os.path.join(b + '/textures/blocks', str('ice.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/itemframe_background.png', b + '/textures/blocks')
                        if 'itemframe_background.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'itemframe_background.png'),
                                      os.path.join(b + '/textures/blocks', str('itemframe_back.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/jukebox_top.png', b + '/textures/blocks')
                        if 'jukebox_top.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'jukebox_top.png'),
                                      os.path.join(b + '/textures/blocks', str('jukebox_top.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/ladder.png', b + '/textures/blocks')
                        if 'ladder.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'ladder.png'),
                                      os.path.join(b + '/textures/blocks', str('ladder.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/lava_still.png', b + '/textures/blocks')
                        if 'lava_still.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'lava_still.png'),
                                      os.path.join(b + '/textures/blocks', str('lava.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/lava_flow.png', b + '/textures/blocks')
                        if 'lava_flow.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'lava_flow.png'),
                                      os.path.join(b + '/textures/blocks', str('lava_flow.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/leaves_birch.png', b + '/textures/blocks')
                        if 'leaves_birch.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'leaves_birch.png'),
                                      os.path.join(b + '/textures/blocks', str('leaves.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/leaves_jungle.png', b + '/textures/blocks')
                        if 'leaves_jungle.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'leaves_jungle.png'),
                                      os.path.join(b + '/textures/blocks', str('leaves_jungle.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/leaves_jungle_opaque.png', b + '/textures/blocks')
                        if 'leaves_jungle_opaque.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'leaves_jungle_opaque.png'),
                                      os.path.join(b + '/textures/blocks', str('leaves_jungle_opaque.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/leaves_birch_opaque.png', b + '/textures/blocks')
                        if 'leaves_birch_opaque.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'leaves_birch_opaque.png'),
                                      os.path.join(b + '/textures/blocks', str('leaves_opaque.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/leaves_spruce.png', b + '/textures/blocks')
                        if 'leaves_spruce.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'leaves_spruce.png'),
                                      os.path.join(b + '/textures/blocks', str('leaves_spruce.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/leaves_spruce_opaque.png', b + '/textures/blocks')
                        if 'leaves_spruce_opaque.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'leaves_spruce_opaque.png'),
                                      os.path.join(b + '/textures/blocks', str('leaves_spruce_opaque.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/lever.png', b + '/textures/blocks')
                        if 'lever.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'lever.png'),
                                      os.path.join(b + '/textures/blocks', str('lever.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/glowstone.png', b + '/textures/blocks')
                        if 'glowstone.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'glowstone.png'),
                                      os.path.join(b + '/textures/blocks', str('lightgem.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/melon_side.png', b + '/textures/blocks')
                        if 'melon_side.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'melon_side.png'),
                                      os.path.join(b + '/textures/blocks', str('melon_side.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/melon_top.png', b + '/textures/blocks')
                        if 'melon_top.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'melon_top.png'),
                                      os.path.join(b + '/textures/blocks', str('melon_top.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/mob_spawner.png', b + '/textures/blocks')
                        if 'mob_spawner.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'mob_spawner.png'),
                                      os.path.join(b + '/textures/blocks', str('mobspawner.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/mushroom_brown.png', b + '/textures/blocks')
                        if 'mushroom_brown.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'mushroom_brown.png'),
                                      os.path.join(b + '/textures/blocks', str('mushroom_brown.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/mushroom_block_inside.png', b + '/textures/blocks')
                        if 'mushroom_block_inside.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'mushroom_block_inside.png'),
                                      os.path.join(b + '/textures/blocks', str('mushroom_inside.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/mushroom_red.png', b + '/textures/blocks')
                        if 'mushroom_red.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'mushroom_red.png'),
                                      os.path.join(b + '/textures/blocks', str('mushroom_red.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/mushroom_block_skin_brown.png', b + '/textures/blocks')
                        if 'mushroom_block_skin_brown.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'mushroom_block_skin_brown.png'),
                                      os.path.join(b + '/textures/blocks', str('mushroom_skin_brown.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/mushroom_block_skin_red.png', b + '/textures/blocks')
                        if 'mushroom_block_skin_red.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'mushroom_block_skin_red.png'),
                                      os.path.join(b + '/textures/blocks', str('mushroom_skin_red.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/mushroom_block_skin_stem.png', b + '/textures/blocks')
                        if 'mushroom_block_skin_stem.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'mushroom_block_skin_stem.png'),
                                      os.path.join(b + '/textures/blocks', str('mushroom_skin_stem.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/noteblock.png', b + '/textures/blocks')
                        if 'noteblock.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'noteblock.png'),
                                      os.path.join(b + '/textures/blocks', str('musicblock.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/mycelium_side.png', b + '/textures/blocks')
                        if 'mycelium_side.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'mycelium_side.png'),
                                      os.path.join(b + '/textures/blocks', str('mycel_side.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/mycelium_top.png', b + '/textures/blocks')
                        if 'mycelium_top.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'mycelium_top.png'),
                                      os.path.join(b + '/textures/blocks', str('mycel_top.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/nether_brick.png', b + '/textures/blocks')
                        if 'nether_brick.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'nether_brick.png'),
                                      os.path.join(b + '/textures/blocks', str('netherBrick.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/quartz_ore.png', b + '/textures/blocks')
                        if 'quartz_ore.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'quartz_ore.png'),
                                      os.path.join(b + '/textures/blocks', str('netherquartz.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/nether_wart_stage_0.png', b + '/textures/blocks')
                        if 'nether_wart_stage_0.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'nether_wart_stage_0.png'),
                                      os.path.join(b + '/textures/blocks', str('netherStalk_0.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/nether_wart_stage_1.png', b + '/textures/blocks')
                        if 'nether_wart_stage_1.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'nether_wart_stage_1.png'),
                                      os.path.join(b + '/textures/blocks', str('netherStalk_1.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/nether_wart_stage_2.png', b + '/textures/blocks')
                        if 'nether_wart_stage_2.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'nether_wart_stage_2.png'),
                                      os.path.join(b + '/textures/blocks', str('netherStalk_2.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/obsidian.png', b + '/textures/blocks')
                        if 'obsidian.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'obsidian.png'),
                                      os.path.join(b + '/textures/blocks', str('obsidian.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/coal_ore.png', b + '/textures/blocks')
                        if 'coal_ore.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'coal_ore.png'),
                                      os.path.join(b + '/textures/blocks', str('oreCoal.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/diamond_ore.png', b + '/textures/blocks')
                        if 'diamond_ore.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'diamond_ore.png'),
                                      os.path.join(b + '/textures/blocks', str('oreDiamond.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/emerald_ore.png', b + '/textures/blocks')
                        if 'emerald_ore.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'emerald_ore.png'),
                                      os.path.join(b + '/textures/blocks', str('oreEmerald.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/gold_ore.png', b + '/textures/blocks')
                        if 'gold_ore.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'gold_ore.png'),
                                      os.path.join(b + '/textures/blocks', str('oreGold.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/iron_ore.png', b + '/textures/blocks')
                        if 'iron_ore.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'iron_ore.png'),
                                      os.path.join(b + '/textures/blocks', str('oreIron.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/lapis_ore.png', b + '/textures/blocks')
                        if 'lapis_ore.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'lapis_ore.png'),
                                      os.path.join(b + '/textures/blocks', str('oreLapis.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/redstone_ore.png', b + '/textures/blocks')
                        if 'redstone_ore.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'redstone_ore.png'),
                                      os.path.join(b + '/textures/blocks', str('oreRedstone.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/piston_bottom.png', b + '/textures/blocks')
                        if 'piston_bottom.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'piston_bottom.png'),
                                      os.path.join(b + '/textures/blocks', str('piston_bottom.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/piston_inner.png', b + '/textures/blocks')
                        if 'piston_inner.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'piston_inner.png'),
                                      os.path.join(b + '/textures/blocks', str('piston_inner_top.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/piston_side.png', b + '/textures/blocks')
                        if 'piston_side.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'piston_side.png'),
                                      os.path.join(b + '/textures/blocks', str('piston_side.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/piston_top_normal.png', b + '/textures/blocks')
                        if 'piston_top_normal.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'piston_top_normal.png'),
                                      os.path.join(b + '/textures/blocks', str('piston_top.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/piston_top_sticky.png', b + '/textures/blocks')
                        if 'piston_top_sticky.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'piston_top_sticky.png'),
                                      os.path.join(b + '/textures/blocks', str('piston_top_sticky.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/portal.png', b + '/textures/blocks')
                        if 'portal.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'portal.png'),
                                      os.path.join(b + '/textures/blocks', str('portal.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/potatoes_stage_0.png', b + '/textures/blocks')
                        if 'potatoes_stage_0.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'potatoes_stage_0.png'),
                                      os.path.join(b + '/textures/blocks', str('potatoes_0.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/potatoes_stage_1.png', b + '/textures/blocks')
                        if 'potatoes_stage_1.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'potatoes_stage_1.png'),
                                      os.path.join(b + '/textures/blocks', str('potatoes_1.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/potatoes_stage_2.png', b + '/textures/blocks')
                        if 'potatoes_stage_2.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'potatoes_stage_2.png'),
                                      os.path.join(b + '/textures/blocks', str('potatoes_2.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/potatoes_stage_3.png', b + '/textures/blocks')
                        if 'potatoes_stage_3.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'potatoes_stage_3.png'),
                                      os.path.join(b + '/textures/blocks', str('potatoes_3.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/pumpkin_face_off.png', b + '/textures/blocks')
                        if 'pumpkin_face_off.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'pumpkin_face_off.png'),
                                      os.path.join(b + '/textures/blocks', str('pumpkin_face.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/pumpkin_face_on.png', b + '/textures/blocks')
                        if 'pumpkin_face_on.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'pumpkin_face_on.png'),
                                      os.path.join(b + '/textures/blocks', str('pumpkin_jack.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/pumpkin_side.png', b + '/textures/blocks')
                        if 'pumpkin_side.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'pumpkin_side.png'),
                                      os.path.join(b + '/textures/blocks', str('pumpkin_side.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/pumpkin_top.png', b + '/textures/blocks')
                        if 'pumpkin_top.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'pumpkin_top.png'),
                                      os.path.join(b + '/textures/blocks', str('pumpkin_top.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/quartz_block_bottom.png', b + '/textures/blocks')
                        if 'quartz_block_bottom.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'quartz_block_bottom.png'),
                                      os.path.join(b + '/textures/blocks', str('quartzblock_bottom.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/quartz_block_chiseled.png', b + '/textures/blocks')
                        if 'quartz_block_chiseled.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'quartz_block_chiseled.png'),
                                      os.path.join(b + '/textures/blocks', str('quartzblock_chiseled.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/quartz_block_chiseled_top.png', b + '/textures/blocks')
                        if 'quartz_block_chiseled_top.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'quartz_block_chiseled_top.png'),
                                      os.path.join(b + '/textures/blocks', str('quartzblock_chiseled_top.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/quartz_block_lines.png', b + '/textures/blocks')
                        if 'quartz_block_lines.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'quartz_block_lines.png'),
                                      os.path.join(b + '/textures/blocks', str('quartzblock_lines.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/quartz_block_lines_top.png', b + '/textures/blocks')
                        if 'quartz_block_lines_top.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'quartz_block_lines_top.png'),
                                      os.path.join(b + '/textures/blocks', str('quartzblock_lines_top.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/quartz_block_side.png', b + '/textures/blocks')
                        if 'quartz_block_side.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'quartz_block_side.png'),
                                      os.path.join(b + '/textures/blocks', str('quartzblock_side.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/quartz_block_top.png', b + '/textures/blocks')
                        if 'quartz_block_top.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'quartz_block_top.png'),
                                      os.path.join(b + '/textures/blocks', str('quartzblock_top.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/rail_normal.png', b + '/textures/blocks')
                        if 'rail_normal.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'rail_normal.png'),
                                      os.path.join(b + '/textures/blocks', str('rail.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/rail_normal_turned.png', b + '/textures/blocks')
                        if 'rail_normal_turned.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'rail_normal_turned.png'),
                                      os.path.join(b + '/textures/blocks', str('rail_turn.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/redstone_dust_cross.png', b + '/textures/blocks')
                        if 'redstone_dust_cross.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'redstone_dust_cross.png'),
                                      os.path.join(b + '/textures/blocks', str('redstoneDust_cross.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/redstone_dust_line.png', b + '/textures/blocks')
                        if 'redstone_dust_line.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'redstone_dust_line.png'),
                                      os.path.join(b + '/textures/blocks', str('redstoneDust_line.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/redstone_lamp_off.png', b + '/textures/blocks')
                        if 'redstone_lamp_off.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'redstone_lamp_off.png'),
                                      os.path.join(b + '/textures/blocks', str('redstoneLight.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/redstone_lamp_on.png', b + '/textures/blocks')
                        if 'redstone_lamp_on.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'redstone_lamp_on.png'),
                                      os.path.join(b + '/textures/blocks', str('redstoneLight_lit.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/redstone_torch_off.png', b + '/textures/blocks')
                        if 'redstone_torch_off.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'redstone_torch_off.png'),
                                      os.path.join(b + '/textures/blocks', str('redtorch.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/redstone_torch_on.png', b + '/textures/blocks')
                        if 'redstone_torch_on.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'redstone_torch_on.png'),
                                      os.path.join(b + '/textures/blocks', str('redtorch_lit.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/reeds.png', b + '/textures/blocks')
                        if 'reeds.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'reeds.png'),
                                      os.path.join(b + '/textures/blocks', str('reeds.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/repeater_off.png', b + '/textures/blocks')
                        if 'repeater_off.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'repeater_off.png'),
                                      os.path.join(b + '/textures/blocks', str('repeater.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/repeater_on.png', b + '/textures/blocks')
                        if 'repeater_on.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'repeater_on.png'),
                                      os.path.join(b + '/textures/blocks', str('repeater_lit.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/flower_rose.png', b + '/textures/blocks')
                        if 'flower_rose.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'flower_rose.png'),
                                      os.path.join(b + '/textures/blocks', str('rose.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/sand.png', b + '/textures/blocks')
                        if 'sand.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'sand.png'),
                                      os.path.join(b + '/textures/blocks', str('sand.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/sandstone_bottom.png', b + '/textures/blocks')
                        if 'sandstone_bottom.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'sandstone_bottom.png'),
                                      os.path.join(b + '/textures/blocks', str('sandstone_bottom.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/sandstone_carved.png', b + '/textures/blocks')
                        if 'sandstone_carved.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'sandstone_carved.png'),
                                      os.path.join(b + '/textures/blocks', str('sandstone_carved.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/sandstone_normal.png', b + '/textures/blocks')
                        if 'sandstone_normal.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'sandstone_normal.png'),
                                      os.path.join(b + '/textures/blocks', str('sandstone_side.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/sandstone_smooth.png', b + '/textures/blocks')
                        if 'sandstone_smooth.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'sandstone_smooth.png'),
                                      os.path.join(b + '/textures/blocks', str('sandstone_smooth.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/sandstone_top.png', b + '/textures/blocks')
                        if 'sandstone_top.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'sandstone_top.png'),
                                      os.path.join(b + '/textures/blocks', str('sandstone_top.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/sapling_oak.png', b + '/textures/blocks')
                        if 'sapling_oak.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'sapling_oak.png'),
                                      os.path.join(b + '/textures/blocks', str('sapling.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/sapling_birch.png', b + '/textures/blocks')
                        if 'sapling_birch.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'sapling_birch.png'),
                                      os.path.join(b + '/textures/blocks', str('sapling_birch.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/sapling_jungle.png', b + '/textures/blocks')
                        if 'sapling_jungle.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'sapling_jungle.png'),
                                      os.path.join(b + '/textures/blocks', str('sapling_jungle.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/sapling_spruce.png', b + '/textures/blocks')
                        if 'sapling_spruce.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'sapling_spruce.png'),
                                      os.path.join(b + '/textures/blocks', str('sapling_spruce.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/snow.png', b + '/textures/blocks')
                        if 'snow.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'snow.png'),
                                      os.path.join(b + '/textures/blocks', str('snow.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/grass_side_snowed.png', b + '/textures/blocks')
                        if 'grass_side_snowed.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'grass_side_snowed.png'),
                                      os.path.join(b + '/textures/blocks', str('snow_side.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/sponge.png', b + '/textures/blocks')
                        if 'sponge.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'sponge.png'),
                                      os.path.join(b + '/textures/blocks', str('sponge.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/stone.png', b + '/textures/blocks')
                        if 'stone.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'stone.png'),
                                      os.path.join(b + '/textures/blocks', str('stone.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/cobblestone.png', b + '/textures/blocks')
                        if 'cobblestone.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'cobblestone.png'),
                                      os.path.join(b + '/textures/blocks', str('stonebrick.png')))

                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/stonebrick.png', b + '/textures/blocks')
                        if 'stonebrick.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'stonebrick.png'),
                                      os.path.join(b + '/textures/blocks', str('stonebricksmooth.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/stonebrick_carved.png', b + '/textures/blocks')
                        if 'stonebrick_carved.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'stonebrick_carved.png'),
                                      os.path.join(b + '/textures/blocks', str('stonebricksmooth_carved.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/stonebrick_cracked.png', b + '/textures/blocks')
                        if 'stonebrick_cracked.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'stonebrick_cracked.png'),
                                      os.path.join(b + '/textures/blocks', str('stonebricksmooth_cracked.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/stonebrick_mossy.png', b + '/textures/blocks')
                        if 'stonebrick_mossy.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'stonebrick_mossy.png'),
                                      os.path.join(b + '/textures/blocks', str('stonebricksmooth_mossy.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/cobblestone_mossy.png', b + '/textures/blocks')
                        if 'cobblestone_mossy.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'cobblestone_mossy.png'),
                                      os.path.join(b + '/textures/blocks', str('stoneMoss.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/stone_slab_side.png', b + '/textures/blocks')
                        if 'stone_slab_side.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'stone_slab_side.png'),
                                      os.path.join(b + '/textures/blocks', str('stoneslab_side.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/stone_slab_top.png', b + '/textures/blocks')
                        if 'stone_slab_top.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'stone_slab_top.png'),
                                      os.path.join(b + '/textures/blocks', str('stoneslab_top.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/tallgrass.png', b + '/textures/blocks')
                        if 'tallgrass.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'tallgrass.png'),
                                      os.path.join(b + '/textures/blocks', str('tallgrass.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/glass_pane_top.png', b + '/textures/blocks')
                        if 'glass_pane_top.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'glass_pane_top.png'),
                                      os.path.join(b + '/textures/blocks', str('thinglass_top.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/tnt_bottom.png', b + '/textures/blocks')
                        if 'tnt_bottom.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'tnt_bottom.png'),
                                      os.path.join(b + '/textures/blocks', str('tnt_bottom.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/tnt_side.png', b + '/textures/blocks')
                        if 'tnt_side.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'tnt_side.png'),
                                      os.path.join(b + '/textures/blocks', str('tnt_side.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/tnt_top.png', b + '/textures/blocks')
                        if 'tnt_top.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'tnt_top.png'),
                                      os.path.join(b + '/textures/blocks', str('tnt_top.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/torch_on.png', b + '/textures/blocks')
                        if 'torch_on.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'torch_on.png'),
                                      os.path.join(b + '/textures/blocks', str('torch.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/trapdoor.png', b + '/textures/blocks')
                        if 'trapdoor.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'trapdoor.png'),
                                      os.path.join(b + '/textures/blocks', str('trapdoor.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/log_birch.png', b + '/textures/blocks')
                        if 'log_birch.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'log_birch.png'),
                                      os.path.join(b + '/textures/blocks', str('tree_birch.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/log_jungle.png', b + '/textures/blocks')
                        if 'log_jungle.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'log_jungle.png'),
                                      os.path.join(b + '/textures/blocks', str('tree_jungle.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/log_oak.png', b + '/textures/blocks')
                        if 'log_oak.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'log_oak.png'),
                                      os.path.join(b + '/textures/blocks', str('tree_side.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/log_spruce.png', b + '/textures/blocks')
                        if 'log_spruce.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'log_spruce.png'),
                                      os.path.join(b + '/textures/blocks', str('tree_spruce.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/log_oak_top.png', b + '/textures/blocks')
                        if 'log_oak_top.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'log_oak_top.png'),
                                      os.path.join(b + '/textures/blocks', str('tree_top.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/trip_wire.png', b + '/textures/blocks')
                        if 'trip_wire.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'trip_wire.png'),
                                      os.path.join(b + '/textures/blocks', str('tripwire.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/trip_wire_source.png', b + '/textures/blocks')
                        if 'trip_wire_source.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'trip_wire_source.png'),
                                      os.path.join(b + '/textures/blocks', str('tripwireSource.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/water_still.png', b + '/textures/blocks')
                        if 'water_still.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'water_still.png'),
                                      os.path.join(b + '/textures/blocks', str('water.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/water_flow.png', b + '/textures/blocks')
                        if 'water_flow.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'water_flow.png'),
                                      os.path.join(b + '/textures/blocks', str('water_flow.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/waterlily.png', b + '/textures/blocks')
                        if 'waterlily.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'waterlily.png'),
                                      os.path.join(b + '/textures/blocks', str('waterlily.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/web.png', b + '/textures/blocks')
                        if 'web.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'web.png'),
                                      os.path.join(b + '/textures/blocks', str('web.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/end_stone.png', b + '/textures/blocks')
                        if 'end_stone.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'end_stone.png'),
                                      os.path.join(b + '/textures/blocks', str('whitestone.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/planks_oak.png', b + '/textures/blocks')
                        if 'planks_oak.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'planks_oak.png'),
                                      os.path.join(b + '/textures/blocks', str('wood.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/planks_birch.png', b + '/textures/blocks')
                        if 'planks_birch.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'planks_birch.png'),
                                      os.path.join(b + '/textures/blocks', str('wood_birch.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/planks_jungle.png', b + '/textures/blocks')
                        if 'planks_jungle.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'planks_jungle.png'),
                                      os.path.join(b + '/textures/blocks', str('wood_jungle.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/planks_spruce.png', b + '/textures/blocks')
                        if 'planks_spruce.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'planks_spruce.png'),
                                      os.path.join(b + '/textures/blocks', str('wood_spruce.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/crafting_table_front.png', b + '/textures/blocks')
                        if 'crafting_table_front.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'crafting_table_front.png'),
                                      os.path.join(b + '/textures/blocks', str('workbench_front.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/blocks'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/crafting_table_side.png', b + '/textures/blocks')
                        if 'crafting_table_side.png' in file_names:
                            os.rename(os.path.join(b + '/textures/blocks', 'crafting_table_side.png'),
                                      os.path.join(b + '/textures/blocks', str('workbench_side.png')))
                    except:
                        pass

                    # 드디어.. items 부분..

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/apple.png', b + '/textures/items')
                        if 'apple.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'apple.png'),
                                      os.path.join(b + '/textures/items', str('apple.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/apple_golden.png', b + '/textures/items')
                        if 'apple_golden.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'apple_Golden.png'),
                                      os.path.join(b + '/textures/items', str('appleGold.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/arrow.png', b + '/textures/items')
                        if 'arrow.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'arrow.png'),
                                      os.path.join(b + '/textures/items', str('arrow.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/bed.png', b + '/textures/items')
                        if 'bed.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'bed.png'),
                                      os.path.join(b + '/textures/items', str('bed.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/beef_cooked.png', b + '/textures/items')
                        if 'beef_cooked.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'beef_cooked.png'),
                                      os.path.join(b + '/textures/items', str('beefcooked.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/beef_raw.png', b + '/textures/items')
                        if 'beef_raw.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'beef_raw.png'),
                                      os.path.join(b + '/textures/items', str('beefraw.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/blaze_powder.png', b + '/textures/items')
                        if 'blaze_powder.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'blaze_powder.png'),
                                      os.path.join(b + '/textures/items', str('blazepowder.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/blaze_rod.png', b + '/textures/items')
                        if 'blaze_rod.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'blaze_rod.png'),
                                      os.path.join(b + '/textures/items', str('blazerod.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/boat.png', b + '/textures/items')
                        if 'boat.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'boat.png'),
                                      os.path.join(b + '/textures/items', str('boat.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/bone.png', b + '/textures/items')
                        if 'bone.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'bone.png'),
                                      os.path.join(b + '/textures/items', str('bone.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/book_normal.png', b + '/textures/items')
                        if 'book_normal.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'book_normal.png'),
                                      os.path.join(b + '/textures/items', str('book.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/chainmail_boots.png', b + '/textures/items')
                        if 'chainmail_boots.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'chainmail_boots.png'),
                                      os.path.join(b + '/textures/items', str('bootschain.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/leather_boots.png', b + '/textures/items')
                        if 'leather_boots.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'leather_boots.png'),
                                      os.path.join(b + '/textures/items', str('bootsCloth.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/leather_boots_overlay.png', b + '/textures/items')
                        if 'leather_boots_overlay.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'leather_boots_overlay.png'),
                                      os.path.join(b + '/textures/items', str('bootsCloth_overlay.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/diamond_boots.png', b + '/textures/items')
                        if 'diamond_boots.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'diamond_boots.png'),
                                      os.path.join(b + '/textures/items', str('bootsDiamond.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/gold_boots.png', b + '/textures/items')
                        if 'gold_boots.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'gold_boots.png'),
                                      os.path.join(b + '/textures/items', str('bootsgold.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/iron_boots.png', b + '/textures/items')
                        if 'iron_boots.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'iron_boots.png'),
                                      os.path.join(b + '/textures/items', str('bootsiron.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/bow_standby.png', b + '/textures/items')
                        if 'bow_standby.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'bow_standby.png'),
                                      os.path.join(b + '/textures/items', str('bow.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/bow_pulling_0.png', b + '/textures/items')
                        if 'bow_pulling_0.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'bow_pulling_0.png'),
                                      os.path.join(b + '/textures/items', str('bow_pull_0.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/bow_pulling_1.png', b + '/textures/items')
                        if 'bow_pulling_1.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'bow_pulling_1.png'),
                                      os.path.join(b + '/textures/items', str('bow_pull_1.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/bow_pulling_2.png', b + '/textures/items')
                        if 'bow_pulling_2.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'bow_pulling_2.png'),
                                      os.path.join(b + '/textures/items', str('bow_pull_2.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/bowl.png', b + '/textures/items')
                        if 'bowl.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'bowl.png'),
                                      os.path.join(b + '/textures/items', str('bowl.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/bread.png', b + '/textures/items')
                        if 'bread.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'bread.png'),
                                      os.path.join(b + '/textures/items', str('bread.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/brewing_stand.png', b + '/textures/items')
                        if 'brewing_stand.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'brewing_stand.png'),
                                      os.path.join(b + '/textures/items', str('brewingStand.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/brick.png', b + '/textures/items')
                        if 'brick.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'brick.png'),
                                      os.path.join(b + '/textures/items', str('brick.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/bucket_empty.png', b + '/textures/items')
                        if 'bucket_empty.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'bucket_empty.png'),
                                      os.path.join(b + '/textures/items', str('bucket.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/bucket_lava.png', b + '/textures/items')
                        if 'bucket_lava.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'bucket_lava.png'),
                                      os.path.join(b + '/textures/items', str('bucketLava.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/bucket_water.png', b + '/textures/items')
                        if 'bucket_water.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'bucket_water.png'),
                                      os.path.join(b + '/textures/items', str('bucketwater.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/cake.png', b + '/textures/items')
                        if 'cake.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'cake.png'),
                                      os.path.join(b + '/textures/items', str('cake.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/carrot_golden.png', b + '/textures/items')
                        if 'carrot_golden.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'carrot_golden.png'),
                                      os.path.join(b + '/textures/items', str('carrotGolden.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/carrot_on_a_stick.png', b + '/textures/items')
                        if 'carrot_on_a_stick.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'carrot_on_a_stick.png'),
                                      os.path.join(b + '/textures/items', str('carrotOnAStick.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/carrot.png', b + '/textures/items')
                        if 'carrot.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'carrot.png'),
                                      os.path.join(b + '/textures/items', str('carrots.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/cauldron.png', b + '/textures/items')
                        if 'cauldron.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'cauldron.png'),
                                      os.path.join(b + '/textures/items', str('cauldron.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/chainmail_chestplate.png', b + '/textures/items')
                        if 'chainmail_chestplate.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'chainmail_chestplate.png'),
                                      os.path.join(b + '/textures/items', str('chestplateChain.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/leather_chestplate.png', b + '/textures/items')
                        if 'leather_chestplate.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'leather_chestplate.png'),
                                      os.path.join(b + '/textures/items', str('chestplatecloth.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/leather_chestplate_overlay.png', b + '/textures/items')
                        if 'leather_chestplate_overlay.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'leather_chestplate_overlay.png'),
                                      os.path.join(b + '/textures/items', str('chestplateCloth_overlay.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/diamond_chestplate.png', b + '/textures/items')
                        if 'diamond_chestplate.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'diamond_chestplate.png'),
                                      os.path.join(b + '/textures/items', str('chestplateDiamond.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/gold_chestplate.png', b + '/textures/items')
                        if 'gold_chestplate.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'gold_chestplate.png'),
                                      os.path.join(b + '/textures/items', str('chestplategold.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/iron_chestplate.png', b + '/textures/items')
                        if 'iron_chestplate.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'iron_chestplate.png'),
                                      os.path.join(b + '/textures/items', str('chestplateiron.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/chicken_cooked.png', b + '/textures/items')
                        if 'chicken_cooked.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'chicken_cooked.png'),
                                      os.path.join(b + '/textures/items', str('chickenCooked.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/chicken_raw.png', b + '/textures/items')
                        if 'chicken_raw.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'chicken_raw.png'),
                                      os.path.join(b + '/textures/items', str('chickenraw.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/clay_ball.png', b + '/textures/items')
                        if 'clay_ball.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'clay_ball.png'),
                                      os.path.join(b + '/textures/items', str('clay.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/clock.png', b + '/textures/items')
                        if 'clock.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'clock.png'),
                                      os.path.join(b + '/textures/items', str('clock.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/coal.png', b + '/textures/items')
                        if 'coal.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'coal.png'),
                                      os.path.join(b + '/textures/items', str('coal.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/comparator.png', b + '/textures/items')
                        if 'comparator.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'comparator.png'),
                                      os.path.join(b + '/textures/items', str('comparator.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/compass.png', b + '/textures/items')
                        if 'compass.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'compass.png'),
                                      os.path.join(b + '/textures/items', str('compass.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/cookie.png', b + '/textures/items')
                        if 'cookie.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'cookie.png'),
                                      os.path.join(b + '/textures/items', str('cookie.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/diamond.png', b + '/textures/items')
                        if 'diamond.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'diamond.png'),
                                      os.path.join(b + '/textures/items', str('diamond.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/repeater.png', b + '/textures/items')
                        if 'repeater.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'repeater.png'),
                                      os.path.join(b + '/textures/items', str('diode.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/door_iron.png', b + '/textures/items')
                        if 'door_iron.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'door_iron.png'),
                                      os.path.join(b + '/textures/items', str('doorIron.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/door_wood.png', b + '/textures/items')
                        if 'door_wood.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'door_wood.png'),
                                      os.path.join(b + '/textures/items', str('doorWood.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/dye_powder_black.png', b + '/textures/items')
                        if 'dye_powder_black.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'dye_powder_black.png'),
                                      os.path.join(b + '/textures/items', str('dyePowder_black.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/dye_powder_blue.png', b + '/textures/items')
                        if 'dye_powder_blue.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'dye_powder_blue.png'),
                                      os.path.join(b + '/textures/items', str('dyePowder_blue.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/dye_powder_brown.png', b + '/textures/items')
                        if 'dye_powder_brown.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'dye_powder_brown.png'),
                                      os.path.join(b + '/textures/items', str('dyePowder_brown.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/dye_powder_cyan.png', b + '/textures/items')
                        if 'dye_powder_cyan.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'dye_powder_cyan.png'),
                                      os.path.join(b + '/textures/items', str('dyePowder_cyan.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/dye_powder_gray.png', b + '/textures/items')
                        if 'dye_powder_gray.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'dye_powder_gray.png'),
                                      os.path.join(b + '/textures/items', str('dyePowder_gray.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/dye_powder_green.png', b + '/textures/items')
                        if 'dye_powder_green.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'dye_powder_green.png'),
                                      os.path.join(b + '/textures/items', str('dyePowder_green.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/dye_powder_light_blue.png', b + '/textures/items')
                        if 'dye_powder_light_blue.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'dye_powder_light_blue.png'),
                                      os.path.join(b + '/textures/items', str('dyePowder_lightBlue.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/dye_powder_lime.png', b + '/textures/items')
                        if 'dye_powder_lime.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'dye_powder_lime.png'),
                                      os.path.join(b + '/textures/items', str('dyePowder_lime.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/dye_powder_magenta.png', b + '/textures/items')
                        if 'dye_powder_magenta.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'dye_powder_magenta.png'),
                                      os.path.join(b + '/textures/items', str('dyePowder_magenta.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/dye_powder_orange.png', b + '/textures/items')
                        if 'dye_powder_orange.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'dye_powder_orange.png'),
                                      os.path.join(b + '/textures/items', str('dyePowder_orange.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/dye_powder_pink.png', b + '/textures/items')
                        if 'dye_powder_pink.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'dye_powder_pink.png'),
                                      os.path.join(b + '/textures/items', str('dyePowder_pink.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/dye_powder_purple.png', b + '/textures/items')
                        if 'dye_powder_purple.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'dye_powder_purple.png'),
                                      os.path.join(b + '/textures/items', str('dyePowder_purple.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/dye_powder_red.png', b + '/textures/items')
                        if 'dye_powder_red.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'dye_powder_red.png'),
                                      os.path.join(b + '/textures/items', str('dyePowder_red.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/dye_powder_silver.png', b + '/textures/items')
                        if 'dye_powder_silver.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'dye_powder_silver.png'),
                                      os.path.join(b + '/textures/items', str('dyePowder_silver.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/dye_powder_white.png', b + '/textures/items')
                        if 'dye_powder_white.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'dye_powder_white.png'),
                                      os.path.join(b + '/textures/items', str('dyePowder_white.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/dye_powder_yellow.png', b + '/textures/items')
                        if 'dye_powder_yellow.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'dye_powder_yellow.png'),
                                      os.path.join(b + '/textures/items', str('dyePowder_yellow.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/egg.png', b + '/textures/items')
                        if 'egg.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'egg.png'),
                                      os.path.join(b + '/textures/items', str('egg.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/emerald.png', b + '/textures/items')
                        if 'emerald.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'emerald.png'),
                                      os.path.join(b + '/textures/items', str('emerald.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/map_empty.png', b + '/textures/items')
                        if 'map_empty.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'map_empty.png'),
                                      os.path.join(b + '/textures/items', str('emptymap.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/book_enchanted.png', b + '/textures/items')
                        if 'book_enchanted.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'book_enchanted.png'),
                                      os.path.join(b + '/textures/items', str('enchantedBook.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/ender_pearl.png', b + '/textures/items')
                        if 'ender_pearl.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'ender_pearl.png'),
                                      os.path.join(b + '/textures/items', str('enderpearl.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/experience_bottle.png', b + '/textures/items')
                        if 'experience_bottle.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'experience_bottle.png'),
                                      os.path.join(b + '/textures/items', str('expbottle.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/ender_eye.png', b + '/textures/items')
                        if 'ender_eye.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'ender_eye.png'),
                                      os.path.join(b + '/textures/items', str('eyeofender.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/feather.png', b + '/textures/items')
                        if 'feather.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'feather.png'),
                                      os.path.join(b + '/textures/items', str('feather.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/spider_eye_fermented.png', b + '/textures/items')
                        if 'spider_eye_fermented.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'spider_eye_fermented.png'),
                                      os.path.join(b + '/textures/items', str('fermentedSpiderEye.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/fireball.png', b + '/textures/items')
                        if 'fireball.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'fireball.png'),
                                      os.path.join(b + '/textures/items', str('fireball.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/fireworks.png', b + '/textures/items')
                        if 'fireworks.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'fireworks.png'),
                                      os.path.join(b + '/textures/items', str('fireworks.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/fireworks_charge.png', b + '/textures/items')
                        if 'fireworks_charge.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'fireworks_charge.png'),
                                      os.path.join(b + '/textures/items', str('fireworksCharge.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/fireworks_charge_overlay.png', b + '/textures/items')
                        if 'fireworks_charge_overlay.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'fireworks_charge_overlay.png'),
                                      os.path.join(b + '/textures/items', str('fireworksCharge_overlay.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/fish_cod_cooked.png', b + '/textures/items')
                        if 'fish_cod_cooked.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'fish_cod_cooked.png'),
                                      os.path.join(b + '/textures/items', str('fishCooked.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/fish_cod_raw.png', b + '/textures/items')
                        if 'fish_cod_raw.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'fish_cod_raw.png'),
                                      os.path.join(b + '/textures/items', str('fishraw.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/fishing_rod_uncast.png', b + '/textures/items')
                        if 'fishing_rod_uncast.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'fishing_rod_uncast.png'),
                                      os.path.join(b + '/textures/items', str('fishingRod.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/fishing_rod_cast.png', b + '/textures/items')
                        if 'fishing_rod_cast.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'fishing_rod_cast.png'),
                                      os.path.join(b + '/textures/items', str('fishingRod_empty.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/flint.png', b + '/textures/items')
                        if 'flint.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'flint.png'),
                                      os.path.join(b + '/textures/items', str('flint.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/flint_and_steel.png', b + '/textures/items')
                        if 'flint_and_steel.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'flint_and_steel.png'),
                                      os.path.join(b + '/textures/items', str('flintAndSteel.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/flower_pot.png', b + '/textures/items')
                        if 'flower_pot.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'flower_pot.png'),
                                      os.path.join(b + '/textures/items', str('flowerpot.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/item_frame.png', b + '/textures/items')
                        if 'item_frame.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'item_frame.png'),
                                      os.path.join(b + '/textures/items', str('frame.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/ghast_tear.png', b + '/textures/items')
                        if 'ghast_tear.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'ghast_tear.png'),
                                      os.path.join(b + '/textures/items', str('ghastTear.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/potion_bottle_empty.png', b + '/textures/items')
                        if 'potion_bottle_empty.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'potion_bottle_empty.png'),
                                      os.path.join(b + '/textures/items', str('glassBottle.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/gold_nugget.png', b + '/textures/items')
                        if 'gold_nugget.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'gold_nugget.png'),
                                      os.path.join(b + '/textures/items', str('goldnugget.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/diamond_axe.png', b + '/textures/items')
                        if 'diamond_axe.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'diamond_axe.png'),
                                      os.path.join(b + '/textures/items', str('hatchetDiamond.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/gold_axe.png', b + '/textures/items')
                        if 'gold_axe.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'gold_axe.png'),
                                      os.path.join(b + '/textures/items', str('hatchetGold.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/iron_axe.png', b + '/textures/items')
                        if 'iron_axe.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'iron_axe.png'),
                                      os.path.join(b + '/textures/items', str('hatchetIron.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/stone_axe.png', b + '/textures/items')
                        if 'stone_axe.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'stone_axe.png'),
                                      os.path.join(b + '/textures/items', str('hatchetStone.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/wood_axe.png', b + '/textures/items')
                        if 'wood_axe.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'wood_axe.png'),
                                      os.path.join(b + '/textures/items', str('hatchetWood.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/chainmail_helmet.png', b + '/textures/items')
                        if 'chainmail_helmet.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'chainmail_helmet.png'),
                                      os.path.join(b + '/textures/items', str('helmetChain.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/leather_helmet.png', b + '/textures/items')
                        if 'leather_helmet.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'leather_helmet.png'),
                                      os.path.join(b + '/textures/items', str('helmetCloth.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/leather_helmet_overlay.png', b + '/textures/items')
                        if 'leather_helmet_overlay.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'leather_helmet_overlay.png'),
                                      os.path.join(b + '/textures/items', str('helmetCloth_overlay.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/diamond_helmet.png', b + '/textures/items')
                        if 'diamond_helmet.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'diamond_helmet.png'),
                                      os.path.join(b + '/textures/items', str('helmetDiamond.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/gold_helmet.png', b + '/textures/items')
                        if 'gold_helmet.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'gold_helmet.png'),
                                      os.path.join(b + '/textures/items', str('helmetGold.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/iron_helmet.png', b + '/textures/items')
                        if 'iron_helmet.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'iron_helmet.png'),
                                      os.path.join(b + '/textures/items', str('helmetIron.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/diamond_hoe.png', b + '/textures/items')
                        if 'diamond_hoe.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'diamond_hoe.png'),
                                      os.path.join(b + '/textures/items', str('hoeDiamond.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/gold_hoe.png', b + '/textures/items')
                        if 'gold_hoe.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'gold_hoe.png'),
                                      os.path.join(b + '/textures/items', str('hoeGold.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/iron_hoe.png', b + '/textures/items')
                        if 'iron_hoe.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'iron_hoe.png'),
                                      os.path.join(b + '/textures/items', str('hoeiron.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/stone_hoe.png', b + '/textures/items')
                        if 'stone_hoe.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'stone_hoe.png'),
                                      os.path.join(b + '/textures/items', str('hoeStone.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/wood_hoe.png', b + '/textures/items')
                        if 'wood_hoe.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'wood_hoe.png'),
                                      os.path.join(b + '/textures/items', str('hoeWood.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/hopper.png', b + '/textures/items')
                        if 'hopper.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'hopper.png'),
                                      os.path.join(b + '/textures/items', str('hopper.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/gold_ingot.png', b + '/textures/items')
                        if 'gold_ingot.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'gold_ingot.png'),
                                      os.path.join(b + '/textures/items', str('ingotGold.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/iron_ingot.png', b + '/textures/items')
                        if 'iron_ingot.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'iron_ingot.png'),
                                      os.path.join(b + '/textures/items', str('ingotIron.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/leather.png', b + '/textures/items')
                        if 'leather.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'leather.png'),
                                      os.path.join(b + '/textures/items', str('leather.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/chainmail_leggings.png', b + '/textures/items')
                        if 'chainmail_leggings.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'chainmail_leggings.png'),
                                      os.path.join(b + '/textures/items', str('leggingsChain.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/leather_leggings.png', b + '/textures/items')
                        if 'leather_leggings.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'leather_leggings.png'),
                                      os.path.join(b + '/textures/items', str('leggingsCloth.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/leather_leggings_overlay.png', b + '/textures/items')
                        if 'leather_leggings_overlay.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'leather_leggings_overlay.png'),
                                      os.path.join(b + '/textures/items', str('leggingsCloth_overlay.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/diamond_leggings.png', b + '/textures/items')
                        if 'diamond_leggings.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'diamond_leggings.png'),
                                      os.path.join(b + '/textures/items', str('leggingsDiamond.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/gold_leggings.png', b + '/textures/items')
                        if 'gold_leggings.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'gold_leggings.png'),
                                      os.path.join(b + '/textures/items', str('leggingsGold.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/iron_leggings.png', b + '/textures/items')
                        if 'iron_leggings.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'iron_leggings.png'),
                                      os.path.join(b + '/textures/items', str('leggingsIron.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/magma_cream.png', b + '/textures/items')
                        if 'magma_cream.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'magma_cream.png'),
                                      os.path.join(b + '/textures/items', str('magmaCream.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/map_filled.png', b + '/textures/items')
                        if 'map_filled.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'map_filled.png'),
                                      os.path.join(b + '/textures/items', str('map.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/melon.png', b + '/textures/items')
                        if 'melon.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'melon.png'),
                                      os.path.join(b + '/textures/items', str('melon.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/bucket_milk.png', b + '/textures/items')
                        if 'bucket_milk.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'bucket_milk.png'),
                                      os.path.join(b + '/textures/items', str('milk.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/minecart_normal.png', b + '/textures/items')
                        if 'minecart_normal.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'minecart_normal.png'),
                                      os.path.join(b + '/textures/items', str('minecart.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/minecart_chest.png', b + '/textures/items')
                        if 'minecart_chest.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'minecart_chest.png'),
                                      os.path.join(b + '/textures/items', str('minecartChest.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/minecart_furnace.png', b + '/textures/items')
                        if 'minecart_furnace.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'minecart_furnace.png'),
                                      os.path.join(b + '/textures/items', str('minecartFurnace.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/minecart_hopper.png', b + '/textures/items')
                        if 'minecart_hopper.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'minecart_hopper.png'),
                                      os.path.join(b + '/textures/items', str('minecartHopper.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/minecart_tnt.png', b + '/textures/items')
                        if 'minecart_tnt.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'minecart_tnt.png'),
                                      os.path.join(b + '/textures/items', str('minecartTnt.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/spawn_egg.png', b + '/textures/items')
                        if 'spawn_egg.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'spawn_egg.png'),
                                      os.path.join(b + '/textures/items', str('monsterPlacer.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/spawn_egg_overlay.png', b + '/textures/items')
                        if 'spawn_egg_overlay.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'spawn_egg_overlay.png'),
                                      os.path.join(b + '/textures/items', str('monsterPlacer_overlay.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/mushroom_stew.png', b + '/textures/items')
                        if 'mushroom_stew.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'mushroom_stew.png'),
                                      os.path.join(b + '/textures/items', str('mushroomStew.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/netherbrick.png', b + '/textures/items')
                        if 'netherbrick.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'netherbrick.png'),
                                      os.path.join(b + '/textures/items', str('netherbrick.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/quartz.png', b + '/textures/items')
                        if 'quartz.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'quartz.png'),
                                      os.path.join(b + '/textures/items', str('netherquartz.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/nether_wart.png', b + '/textures/items')
                        if 'nether_wart.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'nether_wart.png'),
                                      os.path.join(b + '/textures/items', str('netherStalkSeeds.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/nether_star.png', b + '/textures/items')
                        if 'nether_star.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'nether_star.png'),
                                      os.path.join(b + '/textures/items', str('netherStar.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/painting.png', b + '/textures/items')
                        if 'painting.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'painting.png'),
                                      os.path.join(b + '/textures/items', str('painting.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/paper.png', b + '/textures/items')
                        if 'paper.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'paper.png'),
                                      os.path.join(b + '/textures/items', str('paper.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/diamond_pickaxe.png', b + '/textures/items')
                        if 'diamond_pickaxe.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'diamond_pickaxe.png'),
                                      os.path.join(b + '/textures/items', str('pickaxeDiamond.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/gold_pickaxe.png', b + '/textures/items')
                        if 'gold_pickaxe.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'gold_pickaxe.png'),
                                      os.path.join(b + '/textures/items', str('pickaxeGold.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/iron_pickaxe.png', b + '/textures/items')
                        if 'iron_pickaxe.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'iron_pickaxe.png'),
                                      os.path.join(b + '/textures/items', str('pickaxeIron.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/stone_pickaxe.png', b + '/textures/items')
                        if 'stone_pickaxe.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'stone_pickaxe.png'),
                                      os.path.join(b + '/textures/items', str('pickaxeStone.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/wood_pickaxe.png', b + '/textures/items')
                        if 'wood_pickaxe.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'wood_pickaxe.png'),
                                      os.path.join(b + '/textures/items', str('pickaxeWood.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/porkchop_cooked.png', b + '/textures/items')
                        if 'porkchop_cooked.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'porkchop_cooked.png'),
                                      os.path.join(b + '/textures/items', str('porkchopCooked.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/porkchop_raw.png', b + '/textures/items')
                        if 'porkchop_raw.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'porkchop_raw.png'),
                                      os.path.join(b + '/textures/items', str('porkchopraw.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/potato.png', b + '/textures/items')
                        if 'potato.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'potato.png'),
                                      os.path.join(b + '/textures/items', str('potato.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/potato_baked.png', b + '/textures/items')
                        if 'potato_baked.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'potato_baked.png'),
                                      os.path.join(b + '/textures/items', str('potatoBaked.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/potato_poisonous.png', b + '/textures/items')
                        if 'potato_poisonous.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'potato_poisonous.png'),
                                      os.path.join(b + '/textures/items', str('potatoPoisonous.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/potion_bottle_drinkable.png', b + '/textures/items')
                        if 'potion_bottle_drinkable.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'potion_bottle_drinkable.png'),
                                      os.path.join(b + '/textures/items', str('potion.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/potion_contents.png', b + '/textures/items')
                        if 'potion_contents.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'potion_contents.png'),
                                      os.path.join(b + '/textures/items', str('potion_contents.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/potion_bottle_splash.png', b + '/textures/items')
                        if 'potion_bottle_splash.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'potion_bottle_splash.png'),
                                      os.path.join(b + '/textures/items', str('potion_splash.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/record_11.png', b + '/textures/items')
                        if 'record_11.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'record_11.png'),
                                      os.path.join(b + '/textures/items', str('record_11.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/record_13.png', b + '/textures/items')
                        if 'record_13.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'record_13.png'),
                                      os.path.join(b + '/textures/items', str('record_13.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/record_blocks.png', b + '/textures/items')
                        if 'record_blocks.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'record_blocks.png'),
                                      os.path.join(b + '/textures/items', str('record_blocks.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/record_cat.png', b + '/textures/items')
                        if 'record_cat.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'record_cat.png'),
                                      os.path.join(b + '/textures/items', str('record_cat.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/record_chirp.png', b + '/textures/items')
                        if 'record_chirp.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'record_chirp.png'),
                                      os.path.join(b + '/textures/items', str('record_chirp.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/record_far.png', b + '/textures/items')
                        if 'record_far.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'record_far.png'),
                                      os.path.join(b + '/textures/items', str('record_far.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/record_mall.png', b + '/textures/items')
                        if 'record_mall.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'record_mall.png'),
                                      os.path.join(b + '/textures/items', str('record_mall.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/record_mellohi.png', b + '/textures/items')
                        if 'record_mellohi.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'record_mellohi.png'),
                                      os.path.join(b + '/textures/items', str('record_mellohi.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/record_stal.png', b + '/textures/items')
                        if 'record_stal.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'record_stal.png'),
                                      os.path.join(b + '/textures/items', str('record_stal.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/record_strad.png', b + '/textures/items')
                        if 'record_strad.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'record_strad.png'),
                                      os.path.join(b + '/textures/items', str('record_strad.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/record_wait.png', b + '/textures/items')
                        if 'record_wait.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'record_wait.png'),
                                      os.path.join(b + '/textures/items', str('record_wait.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/record_ward.png', b + '/textures/items')
                        if 'record_ward.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'record_ward.png'),
                                      os.path.join(b + '/textures/items', str('record_ward.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/redstone_dust.png', b + '/textures/items')
                        if 'redstone_dust.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'redstone_dust.png'),
                                      os.path.join(b + '/textures/items', str('redstone.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/reeds.png', b + '/textures/items')
                        if 'reeds.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'reeds.png'),
                                      os.path.join(b + '/textures/items', str('reeds.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/rotten_flesh.png', b + '/textures/items')
                        if 'rotten_flesh.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'rotten_flesh.png'),
                                      os.path.join(b + '/textures/items', str('rottenFlesh.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/saddle.png', b + '/textures/items')
                        if 'saddle.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'saddle.png'),
                                      os.path.join(b + '/textures/items', str('saddle.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/seeds_wheat.png', b + '/textures/items')
                        if 'seeds_wheat.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'seeds_wheat.png'),
                                      os.path.join(b + '/textures/items', str('seeds.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/seeds_melon.png', b + '/textures/items')
                        if 'seeds_melon.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'seeds_melon.png'),
                                      os.path.join(b + '/textures/items', str('seeds_melon.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/seeds_pumpkin.png', b + '/textures/items')
                        if 'seeds_pumpkin.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'seeds_pumpkin.png'),
                                      os.path.join(b + '/textures/items', str('seeds_pumpkin.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/shears.png', b + '/textures/items')
                        if 'shears.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'shears.png'),
                                      os.path.join(b + '/textures/items', str('shears.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/diamond_shovel.png', b + '/textures/items')
                        if 'diamond_shovel.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'diamond_shovel.png'),
                                      os.path.join(b + '/textures/items', str('shovelDiamond.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/gold_shovel.png', b + '/textures/items')
                        if 'gold_shovel.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'gold_shovel.png'),
                                      os.path.join(b + '/textures/items', str('shovelGold.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/iron_shovel.png', b + '/textures/items')
                        if 'iron_shovel.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'iron_shovel.png'),
                                      os.path.join(b + '/textures/items', str('shovelIron.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/stone_shovel.png', b + '/textures/items')
                        if 'stone_shovel.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'stone_shovel.png'),
                                      os.path.join(b + '/textures/items', str('shovelStone.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/wood_shovel.png', b + '/textures/items')
                        if 'wood_shovel.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'wood_shovel.png'),
                                      os.path.join(b + '/textures/items', str('shovelWood.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/sign.png', b + '/textures/items')
                        if 'sign.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'sign.png'),
                                      os.path.join(b + '/textures/items', str('sign.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/slimeball.png', b + '/textures/items')
                        if 'slimeball.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'slimeball.png'),
                                      os.path.join(b + '/textures/items', str('slimeball.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/empty_armor_slot_boots.png', b + '/textures/items')
                        if 'empty_armor_slot_boots.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'empty_armor_slot_boots.png'),
                                      os.path.join(b + '/textures/items', str('slot_empty_boots.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/empty_armor_slot_chestplate.png', b + '/textures/items')
                        if 'empty_armor_slot_chestplate.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'empty_armor_slot_chestplate.png'),
                                      os.path.join(b + '/textures/items', str('slot_empty_chestplate.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/empty_armor_slot_helmet.png', b + '/textures/items')
                        if 'empty_armor_slot_helmet.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'empty_armor_slot_helmet.png'),
                                      os.path.join(b + '/textures/items', str('slot_empty_helmet.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/empty_armor_slot_leggings.png', b + '/textures/items')
                        if 'empty_armor_slot_leggings.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'empty_armor_slot_leggings.png'),
                                      os.path.join(b + '/textures/items', str('slot_empty_leggings.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/snowball.png', b + '/textures/items')
                        if 'snowball.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'snowball.png'),
                                      os.path.join(b + '/textures/items', str('snowball.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/melon_speckled.png', b + '/textures/items')
                        if 'melon_speckled.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'melon_speckled.png'),
                                      os.path.join(b + '/textures/items', str('speckledMelon.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/spider_eye.png', b + '/textures/items')
                        if 'spider_eye.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'spider_eye.png'),
                                      os.path.join(b + '/textures/items', str('spiderEYE.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/stick.png', b + '/textures/items')
                        if 'stick.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'stick.png'),
                                      os.path.join(b + '/textures/items', str('stick.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/string.png', b + '/textures/items')
                        if 'string.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'string.png'),
                                      os.path.join(b + '/textures/items', str('string.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/sugar.png', b + '/textures/items')
                        if 'sugar.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'sugar.png'),
                                      os.path.join(b + '/textures/items', str('sugar.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/gunpowder.png', b + '/textures/items')
                        if 'gunpowder.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'gunpowder.png'),
                                      os.path.join(b + '/textures/items', str('sulphur.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/diamond_sword.png', b + '/textures/items')
                        if 'diamond_sword.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'diamond_sword.png'),
                                      os.path.join(b + '/textures/items', str('swordDiamond.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/gold_sword.png', b + '/textures/items')
                        if 'gold_sword.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'gold_sword.png'),
                                      os.path.join(b + '/textures/items', str('swordGold.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/iron_sword.png', b + '/textures/items')
                        if 'iron_sword.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'iron_sword.png'),
                                      os.path.join(b + '/textures/items', str('swordIron.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/stone_sword.png', b + '/textures/items')
                        if 'stone_sword.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'stone_sword.png'),
                                      os.path.join(b + '/textures/items', str('swordStone.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/wood_sword.png', b + '/textures/items')
                        if 'wood_sword.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'wood_sword.png'),
                                      os.path.join(b + '/textures/items', str('swordWood.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/wheat.png', b + '/textures/items')
                        if 'wheat.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'wheat.png'),
                                      os.path.join(b + '/textures/items', str('wheat.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/book_writable.png', b + '/textures/items')
                        if 'book_writable.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'book_writable.png'),
                                      os.path.join(b + '/textures/items', str('writingBook.png')))
                    except:
                        pass

                    try:
                        file_path = a + '/assets/minecraft/textures/items'
                        file_names = os.listdir(file_path)
                        shutil.copy(file_path + '/book_written.png', b + '/textures/items')
                        if 'book_written.png' in file_names:
                            os.rename(os.path.join(b + '/textures/items', 'book_written.png'),
                                      os.path.join(b + '/textures/items', str('writtenBook.png')))
                    except:
                        pass
                    messagebox.showinfo("Successful", "마크텍팩에 폴더 생성완료")
                else:
                    root.quit()


# GUI생성
root = Tk()
root.title("Transform 1.8.9 to 1.5.2")
root.geometry("500x400")
root.option_add("Font", "맑은고딕 20")

# 비밀번호 라벨
pwlab = Label(root)
pwlab.config(text="비밀번호입력")
pwlab.pack()

# 비밀번호 입력
pwent = Entry(root)
pwent = ttk.Entry(root)
pwent.config(show="*")
pwent.pack()

# 공백1
cleanlab1 = Label(root)
cleanlab1.config(text="")
cleanlab1.pack()

# 이름 라벨
NameLabel1 = Label(root)
NameLabel1.config(text="이름")
NameLabel1.pack()

# 이름 적기
name = Entry(root)
name = ttk.Entry(root)
name.pack()

# 공백2
cleanlab = Label(root)
cleanlab.config(text="")
cleanlab.pack()

# 복사 폴더 라벨
CopyLabel = Label(root)
CopyLabel.config(text="[ 복사할 경로 선택 ]")
CopyLabel.pack()

# 복사 폴더 선택
CopyEntry = Button(root)
CopyEntry.config(text="Click Me!", command=CopyLocation, )
CopyEntry.pack()

# 에러 메시지
CopylocationError = Label(root)
CopylocationError.config(text="", )
CopylocationError.pack()

# 저장폴더 라벨
var = IntVar()
rb1 = Radiobutton(root, text="자유", variable=var, value=1, command=myfunc)
rb2 = Radiobutton(root, text="마크", variable=var, value=2, command=myfunc)

path = Label(root, text="선택경로 : ")
path.pack()
rb1.pack()
rb2.pack()

# 저장폴더 오류발생
MakelocationError = Label(root)
MakelocationError.pack()

# 실행 라벨
btnLabel = Label(root)
btnLabel.config(text="[ 실행 ]")
btnLabel.pack()

# 실행 버튼
btnEnt = Button(root)
btnEnt.config(text="Click Me!", command=EXE)
btnEnt.pack()


root.bind("<Escape>", Quit)  # 들어가야함
root.mainloop()