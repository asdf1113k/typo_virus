import os
import webbrowser
import threading

import progressbar

class Virus:
    list_commands:list[str] = [
'explorer.exe',
'msconfig.exe',
'msinfo32.exe',
'cleanmgr.exe',
'mstsc.exe',
'charmap.exe',
'eventvwr.msc',
'ncpa.cpl',
'appwiz.cpl',
'sfc /scannow',
'ipconfig'
]
    
    list_virus = [
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

    list_url_www_jobs_org:list[str] = [
'',
'100/index.html',
'id.html',
'indexx.html',
'100/00.html',
'',
]

    @staticmethod
    def run():
        print('ЗАПУСК ВРЕДОНОСНЫХ ПРОГРАМм ДЛЯ УДАЛЕНИЯ И ПРОДАЖИ ВАШИХ ДАнНЫХ')
        # ProgressBar = progressbar.ProgressBar(max_value=len(Virus.list_virus))
        Thread1 = threading.Thread(target=Virus._open_windows_programm)
        Thread2 = threading.Thread(target=Virus._open_browser)

        Thread1.start()
        Thread2.start()

        Thread1.join()
        Thread2.join()



    def _open_windows_programm():
        for command in Virus.list_commands:
            os.system(command)


    def _open_browser(quantity:int = 101): # quantity = количество
        for url in Virus.list_url:
            webbrowser.open(f'https://wwwww.jodi.org/{url}')


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