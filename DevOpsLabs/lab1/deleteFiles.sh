#!/bin/bash

show_help() {
    echo "Использование: $0 [-p] <имя_файла|шаблон>"
    echo ""
    echo "Параметры:"
    echo "  Без флага     - Удалить файл с точным именем"
    echo "  -p            - Удалить файлы по шаблону (подстрока в имени)"
    echo ""
    echo "Примеры:"
    echo "  $0 document.txt"
    echo "  $0 -p file"
    echo ""
    echo "Важно: Шаблон регистрозависимый (file ≠ FILE)"
    exit 1
}

if [ $# -lt 1 ]; then
    echo "Ошибка: недостаточно аргументов"
    show_help
fi

if [ "$1" == "-p" ]; then
    if [ $# -lt 2 ]; then
        echo "Ошибка: после флага -p необходимо указать шаблон"
        show_help
    fi

    pattern="$2"
    deleted_count=0

    echo "Поиск файлов по шаблону: '$pattern' (регистрозависимо)"
    echo "============================================"

    for file in ./*; do
        if [ -f "$file" ]; then
            filename=$(basename "$file")
            if [[ "$filename" == *"$pattern"* ]]; then
                rm "./$filename"
                echo "✓ Удалён: $filename"
                deleted_count=$((deleted_count + 1))
            fi
        fi
    done

    echo "============================================"
    echo "Всего удалено файлов: $deleted_count"

    if [ $deleted_count -eq 0 ]; then
        echo "Файлы, соответствующие шаблону, не найдены"
    fi
else
    filename="$1"

    if [ -f "./$filename" ]; then
        rm "./$filename"
        echo "Файл '$filename' успешно удалён"
    else
        echo "Ошибка: файл '$filename' не найден в текущей директории"
        exit 1
    fi
fi

