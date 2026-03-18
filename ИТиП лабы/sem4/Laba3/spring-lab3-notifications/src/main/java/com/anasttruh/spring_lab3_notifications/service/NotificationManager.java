package com.anasttruh.spring_lab3_notifications.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class NotificationManager {

    // ФИНАЛЬНАЯ ВЕРСИЯ (Часть 5): Внедрение коллекции всех сервисов
    private final List<MessageService> messageServices;

    @Autowired
    public NotificationManager(List<MessageService> messageServices) {
        this.messageServices = messageServices;
    }

    public void notify(String message, String recipient) {
        messageServices.forEach(service ->
                service.sendMessage(message, recipient)
        );
    }
}

/*
// -------------------------------------------------------------------------
// ВАРИАНТ ЧАСТИ 4 (Проблемный): Внедрение одного интерфейса
// -------------------------------------------------------------------------
// @Service
// public class NotificationManager {
//
//     private final MessageService messageService;
//
//     @Autowired
//     public NotificationManager(MessageService messageService) {
//         this.messageService = messageService;
//     }
//
//     public void notify(String message, String recipient) {
//         messageService.sendMessage(message, recipient);
//     }
// }
//
// ПОЧЕМУ ОТКАЗАЛИСЬ ОТ ЭТОГО ВАРИАНТА:
// 1. Возникает ошибка NoUniqueBeanDefinitionException: Spring находит несколько
//    бинов типа MessageService (EmailService, SmsService, PushService) и не знает,
//    какой выбрать для внедрения.
// 2. Требует дополнительных аннотаций (@Primary/@Qualifier) для разрешения конфликта.
// 3. Менее гибко: нельзя отправить уведомление сразу по всем каналам без доработок.
//
// -------------------------------------------------------------------------
// ВАРИАНТ ЧАСТИ 3 (Java Config): Зависимость через конструктор
// -------------------------------------------------------------------------
// (Код конструктора такой же, но бин создавался вручную в AppConfig)
//
// ПОЧЕМУ ОТКАЗАЛИСЬ ОТ ЭТОГО ВАРИАНТА:
// 1. При переходе на @ComponentScan ручная конфигурация становится избыточной.
// 2. Нарушает принцип: "конфигурация рядом с кодом", а не в отдельном классе.
// 3. Автоматическое сканирование упрощает поддержку и расширение приложения.
//
// -------------------------------------------------------------------------
// ВАРИАНТ ЧАСТИ 2 (Проблемный): Жесткая связь (Hardcoded)
// -------------------------------------------------------------------------
// public class NotificationManager {
//
//     private final EmailService emailService;
//
//     public NotificationManager() {
//         this.emailService = new EmailService(); // new внутри класса!
//     }
//
//     public void notify(String message, String recipient) {
//         emailService.sendMessage(message, recipient);
//     }
// }
//
// ПОЧЕМУ ОТКАЗАЛИСЬ ОТ ЭТОГО ВАРИАНТА:
// 1. Жесткая связность (Tight Coupling): нельзя заменить сервис без правки кода.
// 2. Объект не управляется Spring → игнорируются @Autowired внутри него.
// 3. Невозможно протестировать с мок-объектом.
// 4. Нарушен принцип инверсии управления (IoC).
// 5. При добавлении нового типа уведомлений нужно менять код класса.
*/