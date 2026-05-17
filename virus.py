import os
import webbrowser

from time import sleep
from alive_progress import alive_bar
from colorama import init, Fore


class Virus:
    init(autoreset=True)

    list_commands: list[str] = [
        "color 3",
        'ipconfig | find "192"',
        "curl ipinfo.io",
        "echo ваши IP получины :)",
        "echo подготовка программ к установке :)",
    ]

    list_programm: list[str] = [
        "DarkSoulExtractor — программа для копирования логов и паролей от игровых аккаунтов",
        "CryptKeeper — поиск зашифрованных и секретных файлов",
        "ShadowCrawler — теневой краулер для сбора паролей",
        "GhostHunter — охотник за открытыми портами в сети",
        "BloodParser — парсер кровавых логов",
        "PhantomSpy — фантомный шпион для мониторинга",
        "DemonDownloader — демонический вредоносный загрузчик файлов",
        "WitchCraft — колдовская программа для обработки и шифровки данных",
        "ZombieArmy — добавления вашего компьютера в армия зомби для DDoS-атак",
        "GhostWalker — раздачик вашей информации по сети",
        "DeathWhisper — шёпот смерти вашего компьютера для мониторинга системы",
        "PhantomProwler — призрачный охотник для сканирования local сети",
        "ShadowStalker — теневой сталкер для отслеживания активности устройства",
        "VampireVault — отправка данных в вампирский архив данных",
        "BloodBender — изгибатель процессорных потоков",
        "DemonDweller — загрузка вечного обитателя в систему",
        "ZombieZapper — уничтожитель системных-процессов",
        "ZombieZephyr — зомби-ветер для передачи данных",
        "DeathDigger — копатель могил данных чтоб точно нельзя было востановить",
        "PhantomPhoenix — фантомный феникс для возрождения вредоносных программ",
        "ZombieZapper — уничтожитель зомби-логов",
    ]

    url_paths: list[str] = [
        "",
        "100/index.html",
        "../beta/untitled/4.html",
        "hqx/i802.html",
        "../beta/index.html",
        "id.html",
        "100/00.html",
        "../goodtimes/index.html",
        "../id.html",
        "hqx/index.html",
        "indexx.html",
    ]

    url_paths__www_jobs_org: set[list[str]] = set(url_paths)

    def run(self) -> None:
        self.clear_terminal()
        print("УСТАНОВКА ВРЕДОНОСНЫХ ПРОГРАМм ДЛЯ УДАЛЕНИЯ И ПРОДАЖИ ВАШИХ ДАнНЫХ")
        self.run_commands()
        sleep(8)
        self.programs_install__joke()

        # self.virus_notification()
        # os.system('shutdown /r /t 10 /c "для усвоения всех программ требуется перезагрузка, счастливого пользования!"') # перезагрузка системы

    def run_commands(self) -> None:
        for command in Virus.list_commands:
            os.system(command)
            sleep(2)

    def open_browser(self) -> None:
        for url in Virus.url_paths__www_jobs_org:
            webbrowser.open(f"https://wwwww.jodi.org/{url}")

    def programs_install__joke(self) -> None:
        with alive_bar(len(Virus.list_programm)) as bar:
            for name_and_description_programm in Virus.list_programm:
                print(Fore.RED + name_and_description_programm)
                bar()
                sleep(1)
                print(Fore.LIGHTGREEN_EX + "установка завершена")
            else:
                self.clear_terminal()

    def clear_terminal(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")

    def virus_notification(self) -> None:
        self.clear_terminal()
        print(r"""
  ______                    _   _     _               _           _     _ _                    _                             _               _ 
 |  ____|                  | | | |   (_)             (_)         | |   (_) |                  ( )                           (_)             | |
 | |____   _____ _ __ _   _| |_| |__  _ _ __   __ _   _ ___   ___| |__  _| |_    __      _____|/__   _____    __ _ _ __ _ __ ___   _____  __| |
 |  __\ \ / / _ \ '__| | | | __| '_ \| | '_ \ / _` | | / __| / __| '_ \| | __|   \ \ /\ / / _ \ \ \ / / _ \  / _` | '__| '__| \ \ / / _ \/ _` |
 | |___\ V /  __/ |  | |_| | |_| | | | | | | | (_| | | \__ \ \__ \ | | | | |_ _   \ V  V /  __/  \ V /  __/ | (_| | |  | |  | |\ V /  __/ (_| |
 |______\_/ \___|_|   \__, |\__|_| |_|_|_| |_|\__, | |_|___/ |___/_| |_|_|\__( )   \_/\_/ \___|   \_/ \___|  \__,_|_|  |_|  |_| \_/ \___|\__,_|
                       __/ |                   __/ |                         |/                                                                
                      |___/                   |___/                                                                                                         
                                                            Всё — дерьмо, мы приехали.
        """)

        sleep(5)
        self.clear_terminal()
        print(r"""
                                                           _              _       _        __          _           _ 
                                                          | |            (_)     (_)      / _|        | |         | |
  _   _  ___  _   _ _ __    ___ ___  _ __ ___  _ __  _   _| |_ ___ _ __   _ ___   _ _ __ | |_ ___  ___| |_ ___  __| |
 | | | |/ _ \| | | | '__|  / __/ _ \| '_ ` _ \| '_ \| | | | __/ _ \ '__| | / __| | | '_ \|  _/ _ \/ __| __/ _ \/ _` |
 | |_| | (_) | |_| | |    | (_| (_) | | | | | | |_) | |_| | ||  __/ |    | \__ \ | | | | | ||  __/ (__| ||  __/ (_| |
  \__, |\___/ \__,_|_|     \___\___/|_| |_| |_| .__/ \__,_|\__\___|_|    |_|___/ |_|_| |_|_| \___|\___|\__\___|\__,_|
   __/ |                                      | |                                                                    
  |___/                                       |_|    
                                                                                  
                                                    твой компютер заражен
                """)
        sleep(5)
        self.clear_terminal()
        print(r"""
                  _                             _   _       _                                                          _ _   
                 | |                           | | (_)     (_)                                                        (_) |  
   __ _ _ __   __| |  _ __   ___     __ _ _ __ | |_ ___   ___ _ __ _   _ ___    ___ __ _ _ __     ___ _   _ _ __ ___   _| |_ 
  / _` | '_ \ / _` | | '_ \ / _ \   / _` | '_ \| __| \ \ / / | '__| | | / __|  / __/ _` | '_ \   / __| | | | '__/ _ \ | | __|
 | (_| | | | | (_| | | | | | (_) | | (_| | | | | |_| |\ V /| | |  | |_| \__ \ | (_| (_| | | | | | (__| |_| | | |  __/ | | |_ 
  \__,_|_| |_|\__,_| |_| |_|\___/   \__,_|_| |_|\__|_| \_/ |_|_|   \__,_|___/  \___\__,_|_| |_|  \___|\__,_|_|  \___| |_|\__|
                                                                                                                                                                                                                                                          
                                            и ни один антивирус не сможет это вылечить
        """)
        sleep(10)


if __name__ == "__main__":
    virus = Virus()
    virus.run()
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
