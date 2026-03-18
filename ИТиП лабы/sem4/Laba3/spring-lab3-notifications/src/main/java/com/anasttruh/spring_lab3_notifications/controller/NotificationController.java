package com.anasttruh.spring_lab3_notifications.controller;

import com.anasttruh.spring_lab3_notifications.service.NotificationManager;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class NotificationController {

    // ФИНАЛЬНАЯ ВЕРСИЯ (Часть 4-5): Прямое внедрение зависимости через конструктор
    private final NotificationManager notificationManager;

    public NotificationController(NotificationManager notificationManager) {
        this.notificationManager = notificationManager;
    }

    @GetMapping("/notify")
    public String notify(@RequestParam String message, @RequestParam String email) {
        notificationManager.notify(message, email);
        return "Уведомление отправлено (аннотации)";
    }
}

/*
// -------------------------------------------------------------------------
// ВАРИАНТ ЧАСТИ 3 (Java Config): Получение бина через ApplicationContext
// -------------------------------------------------------------------------
// @RestController
// public class NotificationController {
//
//     private final ApplicationContext context;
//
//     public NotificationController(ApplicationContext context) {
//         this.context = context;
//     }
//
//     @GetMapping("/notify")
//     public String notify(@RequestParam String message, @RequestParam String email) {
//         NotificationManager manager = context.getBean(NotificationManager.class);
//         manager.notify(message, email);
//         return "Уведомление отправлено через Java Config";
//     }
// }
//
// ПОЧЕМУ ОТКАЗАЛИСЬ ОТ ЭТОГО ВАРИАНТА:
// 1. Антипаттерн "Service Locator": контроллер зависит от API контейнера Spring.
// 2. Скрывает реальные зависимости класса (не видно, что нужен NotificationManager).
// 3. Усложняет тестирование (нужно моковать весь ApplicationContext).
// 4. Прямое внедрение через конструктор чище и соответствует принципам DI.
//
// -------------------------------------------------------------------------
// ВАРИАНТ ЧАСТИ 2 (Проблемный): Ручное создание объекта
// -------------------------------------------------------------------------
// @RestController
// public class NotificationController {
//
//     @GetMapping("/notify")
//     public String notify(@RequestParam String message, @RequestParam String email) {
//         NotificationManager manager = new NotificationManager();
//         manager.notify(message, email);
//         return "Уведомление отправлено (жесткая связь)";
//     }
// }
//
// ПОЧЕМУ ОТКАЗАЛИСЬ ОТ ЭТОГО ВАРИАНТА:
// 1. Объект не управляется Spring (игнорируются @Autowired внутри него).
// 2. Дублирование жесткой связности (контроллер тоже создает объекты вручную).
// 3. Невозможно использовать преимущества DI во всей цепочке вызовов.
// 4. Нарушен принцип инверсии управления (IoC).
*/