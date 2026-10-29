"""Сколько дней осталось до сдачи заданий.

Учебный пример к ЛР5 по информатике: та же логика, что в демо
лендинга «Учебный планировщик студента», но на Python.
Запуск: python days_left.py
"""
from datetime import date

# задания: дисциплина, что сдать, срок
TASKS = [
    ("Информатика", "Отчет по ЛР5 (Git и GitHub)", date(2026, 11, 8)),
    ("Информатика", "Отчет по ЛР6 (CI/CD)", date(2026, 11, 15)),
    ("Информатика", "Итоговый отчет по Obsidian", date(2026, 12, 20)),
]


def plural(n, one, few, many):
    """Русское окончание: 1 день, 2 дня, 5 дней."""
    n10, n100 = n % 10, n % 100
    if n10 == 1 and n100 != 11:
        return one
    if 2 <= n10 <= 4 and not 12 <= n100 <= 14:
        return few
    return many


def left_text(days):
    if days < 0:
        return f"просрочено на {-days} {plural(-days, 'день', 'дня', 'дней')}"
    if days == 0:
        return "сдать сегодня"
    return f"осталось {days} {plural(days, 'день', 'дня', 'дней')}"


def main(today=None):
    today = today or date.today()
    for subject, title, deadline in sorted(TASKS, key=lambda t: t[2]):
        days = (deadline - today).days
        print(f"{deadline:%d.%m.%Y}  {subject}: {title} – {left_text(days)}")


if __name__ == "__main__":
    main()
