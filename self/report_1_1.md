# Исследование стандартного пакета os :tada:

```
Модуль содержит 1079 строк кода, учитывая комментарии и пустые строки
```

Function | Description
------------ | -------------
_os.name_ | Имя операционной системы. Доступные варианты: 'posix', 'nt', 'mac', 'os2', 'ce', 'java'.
_os.environ_ | Словарь переменных окружения. Изменяемый (можно добавлять и удалять переменные окружения).
_os.getlogin()_ | Имя пользователя, вошедшего в терминал (Unix).
_os.getpid()_ | Текущий id процесса.
_os.uname()_ | Информация об ОС. возвращает объект с атрибутами: sysname - имя операционной системы, nodename - имя машины в сети (определяется реализацией), release - релиз, version - версия, machine - идентификатор машины.
_os.access(path, mode, *, dir_fd=None, effective_ids=False, follow_symlinks=True)_ | Проверка доступа к объекту у текущего пользователя. Флаги: os.F_OK - объект существует, os.R_OK - доступен на чтение, os.W_OK - доступен на запись, os.X_OK - доступен на исполнение.
_os.chdir(path)_ | Смена текущей директории.
_os.chmod(path, mode, *, dir_fd=None, follow_symlinks=True)_ | Смена прав доступа к объекту (mode - восьмеричное число).
_os.chown(path, uid, gid, *, dir_fd=None, follow_symlinks=True)_ | Меняет id владельца и группы (Unix).
_os.getcwd()_ | Текущая рабочая директория.
_os.link(src, dst, *, src_dir_fd=None, dst_dir_fd=None, follow_symlinks=True)_ | Создаёт жёсткую ссылку.
_os.listdir(path=".")_ | Список файлов и директорий в папке.
_os.mkdir(path, mode=0o777, *, dir_fd=None)_ | Создаёт директорию. OSError, если директория существует.
_os.makedirs(path, mode=0o777, exist_ok=False)_ | Создаёт директорию, создавая при этом промежуточные директории.
_os.remove(path, *, dir_fd=None)_ | Удаляет путь к файлу.
_os.rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)_ | Переименовывает файл или директорию из src в dst.
_os.renames(old, new)_ | Переименовывает old в new, создавая промежуточные директории.
_os.replace(src, dst, *, src_dir_fd=None, dst_dir_fd=None)_ | Переименовывает из src в dst с принудительной заменой.
_os.rmdir(path, *, dir_fd=None)_ | Удаляет пустую директорию.
_os.removedirs(path)_ | Удаляет директорию, затем пытается удалить родительские директории, и удаляет их рекурсивно, пока они пусты.
_os.symlink(source, link_name, target_is_directory=False, *, dir_fd=None)_ | Создаёт символическую ссылку на объект.
_os.sync()_ | Записывает все данные на диск (Unix).
_os.truncate(path, length) _ | Обрезает файл до длины length.
_os.utime(path, times=None, *, ns=None, dir_fd=None, follow_symlinks=True)_ | Модификация времени последнего доступа и изменения файла. Либо times - кортеж (время доступа в секундах, время изменения в секундах), либо ns - кортеж (время доступа в наносекундах, время изменения в наносекундах).
_os.walk(top, topdown=True, onerror=None, followlinks=False)_ | Генерация имён файлов в дереве каталогов, сверху вниз (если topdown равен True), либо снизу вверх (если False). Для каждого каталога функция walk возвращает кортеж (путь к каталогу, список каталогов, список файлов).
_os.system(command)_ | Исполняет системную команду, возвращает код её завершения (в случае успеха 0).
_os.urandom(n)_ | n случайных байт. Возможно использование этой функции в криптографических целях.
