import time
import os
import webbrowser
import threading

from alive_progress import alive_bar

class Virus:
    list_commands:list[str] = [
# 'explorer.exe',
# 'msconfig.exe',
# 'msinfo32.exe',
# 'cleanmgr.exe',
# 'mstsc.exe',
# 'charmap.exe',
# 'eventvwr.msc',
# 'ncpa.cpl',
# 'appwiz.cpl',
# 'sfc /scannow',
'ipconfig',
]
    
    list_programm = [
'DarkSoulExtractor — программа для извлечения тёмных душ из игровых файлов',
'CryptKeeper — хранитель зашифрованных секретов',
'NightmareInjector — инъектор ночных кошмаров',
'ShadowCrawler — теневой краулер для сбора данных',
'GhostHunter — охотник за призраками в сети',
'BloodParser — парсер кровавых логов',
'DeathRider — наездник смерти для автоматизации задач',
'SoulEater — пожиратель душ для анализа данных',
'PhantomSpy — фантомный шпион для мониторинга',
'DemonDownloader — демонический загрузчик файлов',
"WitchCraft — колдовская программа для обработки данных",
'ZombieArmy — армия зомби для DDoS-атак',
'VampireVortex — вампирский вихрь для сбора информации',
'HellBender — адский изгибатель для трансформации данных',
'Necromancer — некромант для работы с устаревшими системами',
'GhostWalker — призрачный странник по сети',
'DarkMatter — тёмная материя для анализа данных',
'SoulSiphon — сифон душ для извлечения информации',
'DeathWhisper — шёпот смерти для мониторинга системы',
'PhantomProwler — призрачный охотник для сканирования',
'ShadowStalker — теневой сталкер для отслеживания',
'BloodHarvester — сборщик кровавых данных',
'DemonDriver — демонический драйвер системы',
'WitchWeaver — ткач колдовских сетей',
'ZombieZero — нулевое состояние зомби',
'VampireVault — вампирский архив данных',
'HellHound — адская гончая для поиска',
'NecroNet — некросеть для анализа',
'GhostGripper — призрачный захват данных',
'DarkDigger — тёмный копатель информации',
'SoulSnatcher — похититель душ для сбора данных',
'DeathDigger — копатель могил данных',
'PhantomPhoenix — фантомный феникс для возрождения данных',
'ShadowShifter — теневой изменчивый анализатор',
'BloodBender — изгибатель кровавых потоков',
'DemonDweller — обитатель демонических систем',
'WitchWarden — страж колдовских данных',
'ZombieZapper — уничтожитель зомби-процессов',
'VampireVigil — вампирский дозор',
'HellHammer — адский молот для взлома',
'NecroNexus — некротический узел данных',
'GhostGatherer — собиратель призрачных данных',
'DarkDragon — тёмный дракон для защиты',
'SoulSeeker — искатель душ для анализа',
'DeathDart — смертельная стрела данных',
'PhantomPirate — призрачный пират',
'ShadowSnake — теневой змей для сканирования',
'BloodBride — кровавая невеста для сбора данных',
'DemonDancer — демонический танцор данных',
'WitchWitcher — ведьмовской фильтр',
'ZombieZephyr — зомби-ветер для передачи данных',
'VampireVortex — вампирский вихрь для обработки',
'HellHawk — адский ястреб для поиска',
'NecroNet — некросеть для анализа',
'GhostGolem — призрачный голем для автоматизации',
'DarkDrake — тёмный дракон для защиты',
'SoulSlayer — убийца душ для анализа',
'DeathDigger — копатель могил данных',
'PhantomPhoenix — фантомный феникс для возрождения',
'ShadowShifter — теневой изменчивый анализатор',
'BloodBender — изгибатель кровавых потоков',
'DemonDweller — обитатель демонических систем',
'WitchWarden — страж колдовских данных',
'ZombieZapper — уничтожитель зомби-процессов',
'VampireVigil — вампирский дозор',
"HellHammer — адский молот"
]

    set_url_www_jobs_org:set[str] = set([
'',
'100/index.html',
'../beta/untitled/4.html',
'hqx/i802.html',
'../beta/index.html',
'id.html',
'100/00.html',
'../goodtimes/index.html',
'../id.html',
'hqx/index.html',
'indexx.html',
])

    @staticmethod
    def run():
        print('УСТАНОВКА ВРЕДОНОСНЫХ ПРОГРАМм ДЛЯ УДАЛЕНИЯ И ПРОДАЖИ ВАШИХ ДАнНЫХ')
        time.sleep(5)
        Virus.programs_installed_joke()
        open_windows_programm = threading.Thread(target=Virus.open_windows_programm)
        open_browser = threading.Thread(target=Virus.open_browser)
        virus_notification = threading.Thread(target=Virus.virus_notification)

        # open_windows_programm.start()
        # open_browser.start()
        virus_notification.start()

        # open_windows_programm.join()
        # open_browser.join()
        virus_notification.join()

    def open_windows_programm():
        for command in Virus.list_commands:
            os.system(command)

    def open_browser():
        for url in Virus.set_url_www_jobs_org:
            webbrowser.open(f'https://wwwww.jodi.org/{url}')

    def programs_installed_joke():
        with alive_bar(len(Virus.list_programm)) as bar:
            bar()
            for name_and_description_programm in Virus.list_programm:
                print(name_and_description_programm)
                bar()
                time.sleep(0.1)
            else:
                Virus.clear_terminal()

    def clear_terminal():
        print("\033[H\033[J", end="")

    def virus_notification():
        Virus.clear_terminal()
        print(r'''
  ______                    _   _     _               _           _     _ _                    _                             _               _ 
 |  ____|                  | | | |   (_)             (_)         | |   (_) |                  ( )                           (_)             | |
 | |____   _____ _ __ _   _| |_| |__  _ _ __   __ _   _ ___   ___| |__  _| |_    __      _____|/__   _____    __ _ _ __ _ __ ___   _____  __| |
 |  __\ \ / / _ \ '__| | | | __| '_ \| | '_ \ / _` | | / __| / __| '_ \| | __|   \ \ /\ / / _ \ \ \ / / _ \  / _` | '__| '__| \ \ / / _ \/ _` |
 | |___\ V /  __/ |  | |_| | |_| | | | | | | | (_| | | \__ \ \__ \ | | | | |_ _   \ V  V /  __/  \ V /  __/ | (_| | |  | |  | |\ V /  __/ (_| |
 |______\_/ \___|_|   \__, |\__|_| |_|_|_| |_|\__, | |_|___/ |___/_| |_|_|\__( )   \_/\_/ \___|   \_/ \___|  \__,_|_|  |_|  |_| \_/ \___|\__,_|
                       __/ |                   __/ |                         |/                                                                
                      |___/                   |___/                                                                                                         
                                                            Всё — дерьмо, мы приехали.
        ''')
        
            
        
        time.sleep(5)
        print(r'''
                                                           _              _       _        __          _           _ 
                                                          | |            (_)     (_)      / _|        | |         | |
  _   _  ___  _   _ _ __    ___ ___  _ __ ___  _ __  _   _| |_ ___ _ __   _ ___   _ _ __ | |_ ___  ___| |_ ___  __| |
 | | | |/ _ \| | | | '__|  / __/ _ \| '_ ` _ \| '_ \| | | | __/ _ \ '__| | / __| | | '_ \|  _/ _ \/ __| __/ _ \/ _` |
 | |_| | (_) | |_| | |    | (_| (_) | | | | | | |_) | |_| | ||  __/ |    | \__ \ | | | | | ||  __/ (__| ||  __/ (_| |
  \__, |\___/ \__,_|_|     \___\___/|_| |_| |_| .__/ \__,_|\__\___|_|    |_|___/ |_|_| |_|_| \___|\___|\__\___|\__,_|
   __/ |                                      | |                                                                    
  |___/                                       |_|    
                                                                                  
                                                    твой компютер заражен
                ''')
        time.sleep(5)
        print(r'''
                  _                             _   _       _                                                          _ _   
                 | |                           | | (_)     (_)                                                        (_) |  
   __ _ _ __   __| |  _ __   ___     __ _ _ __ | |_ ___   ___ _ __ _   _ ___    ___ __ _ _ __     ___ _   _ _ __ ___   _| |_ 
  / _` | '_ \ / _` | | '_ \ / _ \   / _` | '_ \| __| \ \ / / | '__| | | / __|  / __/ _` | '_ \   / __| | | | '__/ _ \ | | __|
 | (_| | | | | (_| | | | | | (_) | | (_| | | | | |_| |\ V /| | |  | |_| \__ \ | (_| (_| | | | | | (__| |_| | | |  __/ | | |_ 
  \__,_|_| |_|\__,_| |_| |_|\___/   \__,_|_| |_|\__|_| \_/ |_|_|   \__,_|___/  \___\__,_|_| |_|  \___|\__,_|_|  \___| |_|\__|
                                                                                                                                                                                                                                                          
                                            и ни один антивирус не сможет это вылечить
        ''')
        time.sleep(10)
    
    

if __name__ == "__main__":
    Virus.run()
# def removal_process():
#     print("ЗАПУСК ВРЕДОНОСНЫХ ПРОГРАМм ДЛЯ УДАЛЕНИЯ И ПРОДаЖИ ВАШИХ ДАННЫХ")
#     time.sleep(3)

#     bar = progressbar.ProgressBar(max_value=len(list_virus))
#     for index in range(len(list_virus)):
#         time.sleep(0.03)
#         try:
#             print(list_virus[index])
#         except IndexError:
#             pass
#         bar.update(index)
#     else:
#         for count in range(1000): # сколько раз открыть браузер
#             webbrowser.open("wwwww.jodi.org", new=2, autoraise=True)


# def open_windows():
#     for count in range(100): # !!! range(100)
#         for index in range(len(list_command)):
#             os.system(list_command[index])


# if __name__ == '__main__':
#     thread1 = threading.Thread(target=removal_process)
#     thread2 = threading.Thread(target=open_windows)

#     thread1.start()
#     thread2.start()

#     thread1.join()
#     thread2.join()